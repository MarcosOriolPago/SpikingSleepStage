"""
Ben's Spiker Algorithm (BSA) spike encoding.

Reference: B. Schrauwen and J. Van Campenhout, "BSA, a fast and accurate spike
train encoding scheme," Proceedings of the International Joint Conference on
Neural Networks, 2003.

The two public Python implementations available on PyPI (``pyspikes`` and
``spike-encoding``) both encode one signal at a time with pure-Python triple
nested loops (sample x timestep x filter-tap), which is far too slow to encode
an entire multi-patient dataset. This module reimplements BSA vectorized with
numpy: the only Python-level loop is over time (bounded by the FIR filter
length being subtracted off the tail), and every signal in the batch
(windows x channels x bands) is encoded simultaneously as one big array op
per timestep.
"""

import numpy as np
from scipy.signal import firwin


def build_bsa_filter(filter_order: int, cutoff: float) -> np.ndarray:
    """FIR low-pass filter kernel used as the BSA "matched filter"."""
    cutoff = float(np.clip(cutoff, 1e-4, 0.999))
    return firwin(filter_order + 1, cutoff).astype(np.float32)


def _normalize_unit_range(x: np.ndarray, eps: float = 1e-8) -> np.ndarray:
    """Min-max normalizes each signal (last axis) independently into [0, 1]."""
    x_min = x.min(axis=-1, keepdims=True)
    x_max = x.max(axis=-1, keepdims=True)
    return (x - x_min) / np.maximum(x_max - x_min, eps)


def bsa_encode(signals: np.ndarray, fir_filter: np.ndarray, threshold: float = 0.9) -> np.ndarray:
    """
    Encodes a batch of independent 1D signals into binary spike trains with BSA.

    Each signal is treated independently ("for each window"): it is first
    min-max normalized into [0, 1], then greedily matched against the FIR
    filter kernel. At every timestep t, if placing a spike (i.e. subtracting
    the filter response starting at t) reduces the residual error more than
    ``threshold`` allows, a spike is emitted and the residual is updated.

    Args:
        signals: (..., n_samples) array. Any number of leading batch dims.
        fir_filter: (F,) FIR filter kernel (see ``build_bsa_filter``).
        threshold: multiplicative error threshold. Lower -> more spikes.
    Returns:
        Spike train array with the same shape as ``signals``, dtype uint8.
    """
    orig_shape = signals.shape
    n_samples = orig_shape[-1]

    residual = _normalize_unit_range(signals.reshape(-1, n_samples)).astype(np.float32)
    n_signals = residual.shape[0]
    fir = np.asarray(fir_filter, dtype=np.float32)
    F = len(fir)

    spikes = np.zeros((n_signals, n_samples), dtype=np.uint8)

    last_t = max(n_samples - F, 0)
    for t in range(last_t):
        window = residual[:, t:t + F]
        err1 = np.sum(np.abs(window - fir), axis=1)
        err2 = np.sum(np.abs(window), axis=1)

        fire = err1 <= err2 * threshold
        if np.any(fire):
            spikes[fire, t] = 1
            residual[fire, t:t + F] -= fir

    return spikes.reshape(orig_shape)


def bsa_encode_band_signals(
    band_signals: np.ndarray,
    band_defs: list[tuple[float, float]],
    fs: int,
    threshold: float | list[float] = 0.9,
    filter_order: int = 20,
) -> np.ndarray:
    """
    Applies BSA to a stack of band-filtered signals, using one FIR kernel per
    band whose cutoff tracks that band's upper frequency. This keeps the BSA
    "matched filter" aligned with the oscillations actually present in each
    band, instead of forcing every band through the same generic low-pass
    kernel.

    Args:
        band_signals: (..., n_bands, n_samples), where n_bands == len(band_defs).
        band_defs: list of (low_hz, high_hz) tuples, matching ``PreprocessConfig.bands``.
        fs: sampling rate (Hz) of ``band_signals``.
        threshold: a single value shared by all bands, or one value per band
            (see ``PreprocessConfig.bsa_threshold`` -- BSA's firing rate is highly
            sensitive to threshold and that sensitivity shifts per band, so a
            per-band threshold is strongly recommended).
    Returns:
        Spike array with the same shape as ``band_signals``, dtype uint8.
    """
    n_bands = band_signals.shape[-2]
    if n_bands != len(band_defs):
        raise ValueError(f"band_signals has {n_bands} bands but {len(band_defs)} band_defs were given")

    thresholds = np.broadcast_to(np.asarray(threshold, dtype=np.float64), (n_bands,))

    nyq = fs / 2.0
    spikes = np.zeros(band_signals.shape, dtype=np.uint8)

    for b, (_low_hz, high_hz) in enumerate(band_defs):
        cutoff = min(high_hz / nyq, 0.99)
        fir = build_bsa_filter(filter_order, cutoff)
        spikes[..., b, :] = bsa_encode(band_signals[..., b, :], fir_filter=fir, threshold=thresholds[b])

    return spikes


class ChunkedBSAEncoder:
    """
    Streams per-patient float window batches through ``bsa_encode_band_signals``
    in bounded-size chunks.

    Holding every patient's raw float band-filtered windows in memory before a
    single big BSA call would blow up RAM for large datasets (e.g. ~16GB+ for
    the full sleep-stage split). Buffering only ``max_buffer_windows`` windows
    at a time keeps peak memory bounded while still amortizing the per-call
    Python-loop overhead of BSA across many windows at once (as opposed to
    encoding one patient at a time, which multiplies that overhead by the
    number of patients).
    """

    def __init__(self, band_defs, fs: int, threshold: float, filter_order: int, max_buffer_windows: int = 4000):
        self.band_defs = band_defs
        self.fs = fs
        self.threshold = threshold
        self.filter_order = filter_order
        self.max_buffer_windows = max_buffer_windows

        self._buffer = []
        self._buffer_count = 0
        self._spike_chunks = []

    def add(self, window_batch: np.ndarray) -> None:
        """Buffers a (n_windows, ..., n_bands, n_samples) float batch, flushing if full."""
        if window_batch.shape[0] == 0:
            return
        self._buffer.append(window_batch)
        self._buffer_count += window_batch.shape[0]
        if self._buffer_count >= self.max_buffer_windows:
            self._flush()

    def _flush(self) -> None:
        if not self._buffer:
            return
        batch = np.concatenate(self._buffer, axis=0).astype(np.float32)
        spikes = bsa_encode_band_signals(
            batch, self.band_defs, fs=self.fs,
            threshold=self.threshold, filter_order=self.filter_order
        )
        self._spike_chunks.append(spikes)
        self._buffer = []
        self._buffer_count = 0

    def finalize(self) -> np.ndarray:
        """Flushes any remaining buffered windows and returns the full concatenated spike array."""
        self._flush()
        if not self._spike_chunks:
            return np.empty((0,), dtype=np.uint8)
        result = np.concatenate(self._spike_chunks, axis=0)
        self._spike_chunks = []
        return result
