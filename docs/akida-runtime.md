Title: Akida runtime API — Akida Examples documentation

URL Source: https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html

Published Time: Tue, 01 Aug 2023 22:18:23 GMT

Markdown Content:
akida. __version__ [](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.__version__ "Permalink to this definition")
Returns the current version of the akida module.

## Model[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#model "Permalink to this headline")

_class_ akida.Model[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model "Permalink to this definition")
An Akida neural `Model`, represented as a hierarchy of layers.

The `Model` class is the main interface to Akida and allows:

*   to create an empty `Model` to which you can add layers programmatically using the sequential API,

*   to reload a full `Model` from a serialized file or a memory buffer,

*   to create a new `Model` from a list of layers taken from an existing `Model`.

It provides methods to instantiate, train, test and save models.

The `Model` input and output shapes have 4 dimensions, the first one being the number of samples.

The `Model` accepts only uint8 tensors as inputs, whose values are encoded using either 1, 2, 4 or 8-bit precision (i.e. whose max value is 1, 3, 15 or 255 respectively).

If the inputs are 8-bit, then the first layer of the `Model` must be a convolutional layer with either 1 or 3 input channels.

The `Model` output is an int8 our uint8 numpy array if activations are enabled for the last layer, otherwise it is an int32 numpy array.

Parameters
*   **filename** (_str_ _,_ _optional_) – path to the serialized Model. If None, an empty sequential model will be created, or filled with the layers in the layers parameter.

*   **layers** (`list`, optional) – list of layers that will be copied to the new model. If the list does not start with an input layer, it will be added automatically.

**Methods:**

[`add`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.add "akida.Model.add")(self,layer,inbound_layers)Add a layer to the current model.
[`add_classes`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.add_classes "akida.Model.add_classes")(self,num_add_classes)Adds classes to the last layer of the model.
[`compile`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.compile "akida.Model.compile")(self,optimizer)Select and prepare the optimizer for learning of the last layer.
[`evaluate`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.evaluate "akida.Model.evaluate")(self,inputs,labels[,...])Returns the model class accuracy.
[`fit`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.fit "akida.Model.fit")(*args,**kwargs)Overloaded function.
[`forward`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.forward "akida.Model.forward")(self,inputs[,batch_size])Forwards a set of inputs through the model.
[`from_dict`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.from_dict "akida.Model.from_dict")(model_dict)Instantiate a Model from a dict representation
[`from_json`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.from_json "akida.Model.from_json")(model_str)Instantiate a Model from a JSON representation
[`get_layer`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.get_layer "akida.Model.get_layer")(*args,**kwargs)Overloaded function.
[`get_layer_count`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.get_layer_count "akida.Model.get_layer_count")(self)The number of layers.
[`map`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.map "akida.Model.map")(self,device,hw_only)Map the model to a Device using a target backend.
[`pop_layer`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.pop_layer "akida.Model.pop_layer")(self)Remove the last layer of the current model.
[`predict`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.predict "akida.Model.predict")(self,inputs[,batch_size])Predicts a set of inputs through the model.
[`predict_classes`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.predict_classes "akida.Model.predict_classes")(inputs[,num_classes,...])Predicts the class labels for the specified inputs.
[`save`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.save "akida.Model.save")(self,arg0)Saves all the model configuration (all layers and weights) to a file on disk.
[`summary`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.summary "akida.Model.summary")()Prints a string summary of the model.
[`to_buffer`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.to_buffer "akida.Model.to_buffer")(self)Serializes all the model configuration (all layers and weights) to a bytes buffer.
[`to_dict`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.to_dict "akida.Model.to_dict")()Provide a dict representation of the Model
[`to_json`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.to_json "akida.Model.to_json")()Provide a JSON representation of the Model

**Attributes:**

[`input_shape`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.input_shape "akida.Model.input_shape")The model input dimensions.
[`layers`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.layers "akida.Model.layers")Get a list of layers in current model.
[`learning`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.learning "akida.Model.learning")The learning parameters set.
[`metrics`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.metrics "akida.Model.metrics")The model metrics.
[`output_shape`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.output_shape "akida.Model.output_shape")The model output dimensions.
[`power_events`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.power_events "akida.Model.power_events")Copy of power events logged after inference
[`sequences`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.sequences "akida.Model.sequences")The list of layer sequences in the Model
[`statistics`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.statistics "akida.Model.statistics")Get statistics by sequence for this model.

add(_self:akida.core.Model_, _layer:akida::Layer_, _inbound\_layers:List[akida::Layer]=[]_)→None[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.add "Permalink to this definition")
Add a layer to the current model.

A list of inbound layers can optionally be specified. These layers must already be included in the model. if no inbound layer is specified, and the layer is not the first layer in the model, the last included layer will be used as inbound layer.

Parameters
*   **layer** (_one of the available layers_) – layer instance to be added to the model

*   **inbound_layers** (a list of Layer) – an optional list of inbound layers

add_classes(_self:[akida.core.Model](https://brainchip-inc.github.io/akida\_examples\_2.3.0-doc-1/api\_reference/akida\_apis.html#akida.Model "akida.core.Model")_, _num\_add\_classes:int_)→None[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.add_classes "Permalink to this definition")
Adds classes to the last layer of the model.

A model with a compiled last layer is ready to learn using the Akida built-in learning algorithm. This function allows to add new classes (i.e. new neurons) to the last layer, keeping the previously learned neurons.

Parameters
**num_add_classes** (_int_) – number of classes to add to the last layer

Raises
**RuntimeError** – if the last layer is not compiled

compile(_self:akida.core.Model_, _optimizer:akida::LearningParams_)→None[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.compile "Permalink to this definition")
Select and prepare the optimizer for learning of the last layer.

Parameters
**optimizer** (`akida.LearningParams`) – the optimizer used for learning

evaluate(_self:[akida.core.Model](https://brainchip-inc.github.io/akida\_examples\_2.3.0-doc-1/api\_reference/akida\_apis.html#akida.Model "akida.core.Model")_, _inputs:numpy.ndarray[numpy.uint8]_, _labels:numpy.ndarray[numpy.int32]_, _num\_classes:int=0_, _batch\_size:int=0_)→float[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.evaluate "Permalink to this definition")
Returns the model class accuracy.

Forwards an input tensor through the model and compute accuracy based on labels. If the number of output neurons is greater than the number of classes, the neurons are automatically assigned to a class by dividing their id by the number of classes.

Note that the evaluation is based on the activation values of the last layer: for most use cases, you may want to disable activations for that layer (ie setting `activation=False`) to get a better accuracy.

Parameters
*   **inputs** (`numpy.ndarray`) – a (n, x, y, c) uint8 tensor

*   **labels** (`numpy.ndarray`) – a (n) tensor of labels for the inputs

*   **num_classes** (_int_ _,_ _optional_) – optional parameter (defaults to the number of neurons in the last layer).

*   **batch_size** (_int_ _,_ _optional_) – maximum number of inputs that should be processed at a time

Returns
the accuracy of the model to predict the labels based on the inputs.

Return type
float

fit(_*args_, _**kwargs_)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.fit "Permalink to this definition")
Overloaded function.

1.   fit(self: akida.core.Model, inputs: numpy.ndarray, input_labels: float, batch_size: int = 0) -> numpy.ndarray

Trains a set of images or events through the model.

Trains the model with the specified input tensor (numpy array).

Parameters
*   **inputs** (`numpy.ndarray`) – a (n, x, y, c) uint8 tensor

*   **input_labels** (_float_ _,_ _optional_) – input label

*   **batch_size** (_int_ _,_ _optional_) – maximum number of inputs that should be processed at a time.

Returns
a (n, out_x, out_y, out_c) int8 or uint8 or int32 tensor.

Return type
`numpy.ndarray`

Raises
*   **TypeError** – if the input is not a numpy.ndarray.

*   **ValueError** – if the input doesn’t match the required shape, format, etc.

1.   fit(self: akida.core.Model, inputs: numpy.ndarray, input_labels: numpy.ndarray, batch_size: int = 0) -> numpy.ndarray

Trains a set of images or events through the model.

Trains the model with the specified input tensor (numpy array).

Parameters
*   **inputs** (`numpy.ndarray`) – a (n, x, y, c) uint8 tensor

*   **input_labels** (`numpy.ndarray`, optional) – input labels. Must have one label per input, or a single label for all inputs. If a label exceeds the defined number of classes, the input will be discarded. (Default value = None).

*   **batch_size** (_int_ _,_ _optional_) – maximum number of inputs that should be processed at a time.

Returns
a (n, out_x, out_y, out_c) int8 or int8 or int32 tensor.

Return type
`numpy.ndarray`

Raises
*   **TypeError** – if the input is not a numpy.ndarray.

*   **ValueError** – if the input doesn’t match the required shape, format, etc.

1.   fit(self: akida.core.Model, inputs: numpy.ndarray, input_labels: list = [], batch_size: int = 0) -> numpy.ndarray

Trains a set of images or events through the model.

Trains the model with the specified input tensor (numpy array).

Parameters
*   **inputs** (`numpy.ndarray`) – a (n, x, y, c) uint8 tensor

*   **input_labels** (_list_ _(_ _int_ _)_ _,_ _optional_) – input labels. Must have one label per input, or a single label for all inputs. If a label exceeds the defined number of classes, the input will be discarded. (Default value = None).

*   **batch_size** (_int_ _,_ _optional_) – maximum number of inputs that should be processed at a time.

Returns
a (n, out_x, out_y, out_c) int8 or int8 or int32 tensor.

Return type
`numpy.ndarray`

Raises
*   **TypeError** – if the input is not a numpy.ndarray.

*   **ValueError** – if the input doesn’t match the required shape, format, etc.

forward(_self:[akida.core.Model](https://brainchip-inc.github.io/akida\_examples\_2.3.0-doc-1/api\_reference/akida\_apis.html#akida.Model "akida.core.Model")_, _inputs:numpy.ndarray_, _batch\_size:int=0_)→numpy.ndarray[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.forward "Permalink to this definition")
Forwards a set of inputs through the model.

Forwards an input tensor through the model and returns an output tensor.

Parameters
*   **inputs** (`numpy.ndarray`) – a (n, x, y, c) uint8 tensor

*   **batch_size** (_int_ _,_ _optional_) – maximum number of inputs that should be processed at a time

Returns
a (n, out_x, out_y, out_c) uint8, int8 or int32 tensor.

Return type
`numpy.ndarray`

Raises
*   **TypeError** – if the input is not a numpy.ndarray.

*   **ValueError** – if the inputs doesn’t match the required shape, format, etc.

_static_ from_dict(_model\_dict_)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.from_dict "Permalink to this definition")
Instantiate a Model from a dict representation

Parameters
**model_dict** (_dict_) – a Model dictionary.

Returns
a Model.

Return type
[`Model`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model "akida.Model")

_static_ from_json(_model\_str_)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.from_json "Permalink to this definition")
Instantiate a Model from a JSON representation

Parameters
**model_str** (_str_) – a JSON-formatted string corresponding to a Model.

Returns
a Model.

Return type
[`Model`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model "akida.Model")

get_layer(_*args_, _**kwargs_)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.get_layer "Permalink to this definition")
Overloaded function.

1.   get_layer(self: akida.core.Model, layer_name: str) -> akida::Layer

> Get a reference to a specific layer.
> 
> 
> This method allows a deeper introspection of the model by providing access to the underlying layers.
> 
> param layer_name
> name of the layer to retrieve
> 
> type layer_name
> str
> 
> return
> a `Layer`

2.   get_layer(self: akida.core.Model, layer_index: int) -> akida::Layer

> Get a reference to a specific layer.
> 
> 
> This method allows a deeper introspection of the model by providing access to the underlying layers.
> 
> param layer_index
> index of the layer to retrieve
> 
> type layer_index
> int
> 
> return
> a `Layer`

get_layer_count(_self:[akida.core.Model](https://brainchip-inc.github.io/akida\_examples\_2.3.0-doc-1/api\_reference/akida\_apis.html#akida.Model "akida.core.Model")_)→int[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.get_layer_count "Permalink to this definition")
The number of layers.

_property_ input_shape[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.input_shape "Permalink to this definition")
The model input dimensions.

_property_ layers[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.layers "Permalink to this definition")
Get a list of layers in current model.

_property_ learning[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.learning "Permalink to this definition")
The learning parameters set.

map(_self:akida.core.Model_, _device:akida::Device_, _hw\_only:bool=False_)→None[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.map "Permalink to this definition")
Map the model to a Device using a target backend.

This method tries to map a Model to the specified Device, implicitly identifying one or more layer sequences that are mapped individually on the Device Mesh.

An optional hw_only parameter can be specified to force the mapping strategy to use only one hardware sequence, thus reducing software intervention on the inference.

Parameters
*   **device** (Device) – the target Device or None

*   **hw_only** (_bool_) – when true, the model should be mapped in one sequence

_property_ metrics[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.metrics "Permalink to this definition")
The model metrics.

_property_ output_shape[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.output_shape "Permalink to this definition")
The model output dimensions.

pop_layer(_self:[akida.core.Model](https://brainchip-inc.github.io/akida\_examples\_2.3.0-doc-1/api\_reference/akida\_apis.html#akida.Model "akida.core.Model")_)→None[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.pop_layer "Permalink to this definition")
Remove the last layer of the current model.

_property_ power_events[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.power_events "Permalink to this definition")
Copy of power events logged after inference

predict(_self:[akida.core.Model](https://brainchip-inc.github.io/akida\_examples\_2.3.0-doc-1/api\_reference/akida\_apis.html#akida.Model "akida.core.Model")_, _inputs:numpy.ndarray_, _batch\_size:int=0_)→numpy.ndarray[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.predict "Permalink to this definition")
Predicts a set of inputs through the model.

Forwards an input tensor through the model and returns a float array.

It applies ONLY to models without an activation on the last layer. The output values are obtained from the model discrete potentials by applying a shift and a scale.

Parameters
*   **inputs** (`numpy.ndarray`) – a (n, x, y, c) uint8 tensor

*   **batch_size** (_int_ _,_ _optional_) – maximum number of inputs that should be processed at a time

Returns
a (n, w, h, c) float tensor.

Return type
`numpy.ndarray`

Raises
*   **TypeError** – if the input is not a numpy.ndarray.

*   **RuntimeError** – if the model last layer has an activation.

*   **ValueError** – if the input doesn’t match the required shape, format, or if the model only has an InputData layer.

predict_classes(_inputs_, _num\_classes=0_, _batch\_size=0_)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.predict_classes "Permalink to this definition")
Predicts the class labels for the specified inputs.

Parameters
*   **inputs** (`numpy.ndarray`) – a (n, x, y, c) uint8 tensor

*   **num_classes** (_int_ _,_ _optional_) – the number of output classes

*   **batch_size** (_int_ _,_ _optional_) – maximum number of inputs that should be processed at a time

Returns
an array of class labels

Return type
`numpy.ndarray`

save(_self:[akida.core.Model](https://brainchip-inc.github.io/akida\_examples\_2.3.0-doc-1/api\_reference/akida\_apis.html#akida.Model "akida.core.Model")_, _arg0:str_)→None[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.save "Permalink to this definition")
Saves all the model configuration (all layers and weights) to a file on disk.

Parameters
**model_file** (_str_) – full path of the serialized model (.fbz file).

_property_ sequences[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.sequences "Permalink to this definition")
The list of layer sequences in the Model

_property_ statistics[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.statistics "Permalink to this definition")
Get statistics by sequence for this model.

Returns
a dictionary of `SequenceStatistics` indexed by name.

summary()[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.summary "Permalink to this definition")
Prints a string summary of the model.

This method prints a summary of the model with details for every layer, grouped by sequences:

*   name and type in the first column

*   output shape

*   kernel shape

If there is any layer with unsupervised learning enabled, it will list them, with these details:

*   name of layer

*   number of incoming connections

*   number of weights per neuron

to_buffer(_self:[akida.core.Model](https://brainchip-inc.github.io/akida\_examples\_2.3.0-doc-1/api\_reference/akida\_apis.html#akida.Model "akida.core.Model")_)→bytes[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.to_buffer "Permalink to this definition")
Serializes all the model configuration (all layers and weights) to a bytes buffer.

to_dict()[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.to_dict "Permalink to this definition")
Provide a dict representation of the Model

Returns
a Model dictionary.

Return type
dict

to_json()[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model.to_json "Permalink to this definition")
Provide a JSON representation of the Model

Returns
a JSON-formatted string corresponding to a Model.

Return type
str

## Layer[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#layer "Permalink to this headline")

### Layer[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#id1 "Permalink to this headline")

_class_ akida.Layer[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer "Permalink to this definition")
**Methods:**

[`get_learning_histogram`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.get_learning_histogram "akida.Layer.get_learning_histogram")()Returns an histogram of learning percentages.
[`get_variable`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.get_variable "akida.Layer.get_variable")(name)Get the value of a layer variable.
[`get_variable_names`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.get_variable_names "akida.Layer.get_variable_names")()Get the list of variable names for this layer.
[`set_variable`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.set_variable "akida.Layer.set_variable")(name,values)Set the value of a layer variable.
[`to_dict`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.to_dict "akida.Layer.to_dict")()Provide a dict representation of the Layer

**Attributes:**

[`inbounds`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.inbounds "akida.Layer.inbounds")The layer inbound layers.
[`input_bits`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.input_bits "akida.Layer.input_bits")The layer input bits.
[`input_dims`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.input_dims "akida.Layer.input_dims")The layer input dimensions.
[`input_signed`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.input_signed "akida.Layer.input_signed")Whether input is signed or not.
[`mapping`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.mapping "akida.Layer.mapping")The layer hardware mapping.
[`name`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.name "akida.Layer.name")The layer name.
[`output_dims`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.output_dims "akida.Layer.output_dims")The layer output dimensions.
[`output_signed`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.output_signed "akida.Layer.output_signed")Whether output is signed or not.
[`parameters`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.parameters "akida.Layer.parameters")The layer parameters set.
[`variables`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.variables "akida.Layer.variables")The layer trainable variables.

get_learning_histogram()[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.get_learning_histogram "Permalink to this definition")
Returns an histogram of learning percentages.

Returns a list of learning percentages and the associated number of neurons.

Returns
a (n,2) numpy.ndarray containing the learning percentages and the number of neurons.

Return type
`numpy.ndarray`

get_variable(_name_)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.get_variable "Permalink to this definition")
Get the value of a layer variable.

Layer variables are named entities representing the weights or thresholds used during inference:

*   Weights variables are typically integer arrays of shape: (x, y, features/channels, num_neurons) row-major (‘C’).

*   Threshold variables are typically integer or float arrays of shape: (num_neurons).

Parameters
**name** (_str_) – the variable name.

Returns
an array containing the variable.

Return type
`numpy.ndarray`

get_variable_names()[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.get_variable_names "Permalink to this definition")
Get the list of variable names for this layer.

Returns
a list of variable names.

_property_ inbounds[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.inbounds "Permalink to this definition")
The layer inbound layers.

_property_ input_bits[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.input_bits "Permalink to this definition")
The layer input bits.

_property_ input_dims[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.input_dims "Permalink to this definition")
The layer input dimensions.

_property_ input_signed[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.input_signed "Permalink to this definition")
Whether input is signed or not.

_property_ mapping[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.mapping "Permalink to this definition")
The layer hardware mapping.

_property_ name[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.name "Permalink to this definition")
The layer name.

_property_ output_dims[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.output_dims "Permalink to this definition")
The layer output dimensions.

_property_ output_signed[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.output_signed "Permalink to this definition")
Whether output is signed or not.

_property_ parameters[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.parameters "Permalink to this definition")
The layer parameters set.

set_variable(_name_, _values_)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.set_variable "Permalink to this definition")
Set the value of a layer variable.

Layer variables are named entities representing the weights or thresholds used during inference:

*   Weights variables are typically integer arrays of shape:

(num_neurons, features/channels, y, x) col-major ordered (‘F’)

or equivalently:

> (x, y, features/channels, num_neurons) row-major (‘C’).

*   Threshold variables are typically integer or float arrays of shape: (num_neurons).

Parameters
*   **name** (_str_) – the variable name.

*   **values** (`numpy.ndarray`) – a numpy.ndarray containing the variable values.

to_dict()[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.to_dict "Permalink to this definition")
Provide a dict representation of the Layer

Returns
a Layer dictionary.

Return type
dict

_property_ variables[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.variables "Permalink to this definition")
The layer trainable variables.

### Mapping[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#mapping "Permalink to this headline")

_class_ akida.Layer.Mapping[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.Mapping "Permalink to this definition")
**Attributes:**

[`nps`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.Mapping.nps "akida.Layer.Mapping.nps")a list of `NP.Mapping` objects.

_property_ nps[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Layer.Mapping.nps "Permalink to this definition")
a list of `NP.Mapping` objects.

## InputData[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#inputdata "Permalink to this headline")

_class_ akida.InputData(_input\_shape_, _input\_bits=4_, _input\_signed=False_, _name=''_)[[source]](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/_modules/akida/layers/input_data.html#InputData)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.InputData "Permalink to this definition")
This layer is used to specify the input dimensions of a low bitwidth Model.

Models accepting 8-bit images must start with an InputConvolutional layer, but layers accepting integer inputs with a lower bitwidth (i.e. not images) and layers accepting signed inputs must start instead with an InputData layer. This layer does not modify its inputs: it just allows to define the Model input dimensions and bitwidth.

Parameters
*   **input_shape** (_tuple_) – the 3D input shape.

*   **input_bits** (_int_ _,_ _optional_) – input bitwidth. Defaults to 4.

*   **input_signed** (_bool_ _,_ _optional_) – whether the input is signed or not. Defaults to False.

*   **name** (_str_ _,_ _optional_) – name of the layer. Defaults to empty string.

## InputConvolutional[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#inputconvolutional "Permalink to this headline")

_class_ akida.InputConvolutional(_input\_shape_, _kernel\_size_, _filters_, _name=''_, _padding=<Padding.Same:1>_, _kernel\_stride=(1_, _1)_, _weights\_bits=1_, _pool\_size=(-1_, _-1)_, _pool\_type=<PoolType.NoPooling:0>_, _pool\_stride=(-1_, _-1)_, _activation=True_, _act\_bits=1_, _padding\_value=0_)[[source]](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/_modules/akida/layers/input_convolutional.html#InputConvolutional)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.InputConvolutional "Permalink to this definition")
The `InputConvolutional` layer is an image-specific input layer.

The InputConvolutional layer accepts images in 8-bit pixels, either grayscale or RGB. It is the only akida layer with 8-bit weights. It applies a ‘convolution’ (actually a cross-correlation) optionally followed by a pooling operation to the input images. It can optionally apply a step-wise ReLU activation to its outputs. The layer expects a 4D tensor whose first dimension is the sample index representing the 8-bit images as input. It returns a 4D tensor whose first dimension is the sample index and the last dimension is the number of convolution filters. The order of the input spatial dimensions is preserved, but their value may change according to the convolution and pooling parameters.

Parameters
*   **input_shape** (_tuple_) – the 3D input shape.

*   **kernel_size** (_list_) – list of 2 integer representing the spatial dimensions of the convolutional kernel.

*   **filters** (_int_) – number of filters.

*   **name** (_str_ _,_ _optional_) – name of the layer. Defaults to empty string.

*   **padding** ([`Padding`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Padding "akida.Padding"), optional) – type of convolution. Defaults to Padding.Same.

*   **kernel_stride** (_tuple_ _,_ _optional_) – tuple of integer representing the convolution stride (X, Y). Defaults to (1, 1).

*   **weights_bits** (_int_ _,_ _optional_) – number of bits used to quantize weights. Defaults to 1.

*   **pool_size** (_list_ _,_ _optional_) – list of 2 integers, representing the window size over which to take the maximum or the average (depending on pool_type parameter). Defaults to (-1, -1).

*   **pool_type** ([`PoolType`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PoolType "akida.PoolType"), optional) – pooling type (NoPooling, Max or Average). Defaults to PoolType.NoPooling.

*   **pool_stride** (_list_ _,_ _optional_) – list of 2 integers representing the stride dimensions. Defaults to (-1, -1)

*   **activation** (_bool_ _,_ _optional_) – enable or disable activation function. Defaults to True.

*   **act_bits** (_int_ _,_ _optional_) – number of bits used to quantize the neuron response. Defaults to 1.

*   **padding_value** (_int_ _,_ _optional_) – value used when padding. Defaults to 0.

## FullyConnected[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#fullyconnected "Permalink to this headline")

_class_ akida.FullyConnected(_units_, _name=''_, _weights\_bits=1_, _activation=True_, _act\_bits=1_)[[source]](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/_modules/akida/layers/fully_connected.html#FullyConnected)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.FullyConnected "Permalink to this definition")
This represents a Dense or Linear neural layer.

The FullyConnected layer accepts 1-bit, 2-bit or 4-bit input tensors. The FullyConnected can be configured with 1-bit, 2-bit or 4-bit weights. It multiplies the inputs by its internal unit weights, returning a 4D tensor of values whose first dimension is the number of samples and the last dimension represents the number of units. It can optionally apply a step-wise ReLU activation to its outputs.

Parameters
*   **units** (_int_) – number of units.

*   **name** (_str_ _,_ _optional_) – name of the layer. Defaults to empty string.

*   **weights_bits** (_int_ _,_ _optional_) – number of bits used to quantize weights. Defaults to 1.

*   **activation** (_bool_ _,_ _optional_) – enable or disable activation function. Defaults to True.

*   **act_bits** (_int_ _,_ _optional_) – number of bits used to quantize the neuron response. Defaults to 1.

## Convolutional[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#convolutional "Permalink to this headline")

_class_ akida.Convolutional(_kernel\_size_, _filters_, _name=''_, _padding=<Padding.Same:1>_, _kernel\_stride=(1_, _1)_, _weights\_bits=1_, _pool\_size=(-1_, _-1)_, _pool\_type=<PoolType.NoPooling:0>_, _pool\_stride=(-1_, _-1)_, _activation=True_, _act\_bits=1_)[[source]](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/_modules/akida/layers/convolutional.html#Convolutional)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Convolutional "Permalink to this definition")
This represents a standard Convolutional layer.

The Convolutional layer accepts 1-bit, 2-bit or 4-bit 3D input tensors with an arbitrary number of channels. The Convolutional layer can be configured with 1-bit, 2-bit or 4-bit weights. It applies a convolution (not a cross-correlation) optionally followed by a pooling operation to the input tensors. It can optionally apply a step-wise ReLU activation to its outputs. The layer expects a 4D tensor whose first dimension is the sample index as input. It returns a 4D tensor whose first dimension is the sample index and the last dimension is the number of convolution filters. The order of the input spatial dimensions is preserved, but their value may change according to the convolution and pooling parameters.

Parameters
*   **kernel_size** (_list_) – list of 2 integer representing the spatial dimensions of the convolutional kernel.

*   **filters** (_int_) – number of filters.

*   **name** (_str_ _,_ _optional_) – name of the layer. Defaults to empty string

*   **padding** ([`Padding`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Padding "akida.Padding"), optional) – type of convolution. Defaults to Padding.Same.

*   **kernel_stride** (_list_ _,_ _optional_) – list of 2 integer representing the convolution stride (X, Y). Defaults to (1, 1).

*   **weights_bits** (_int_ _,_ _optional_) – number of bits used to quantize weights. Defaults to 1.

*   **pool_size** (_list_ _,_ _optional_) – list of 2 integers, representing the window size over which to take the maximum or the average (depending on pool_type parameter). Defaults to (-1, -1).

*   **pool_type** ([`PoolType`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PoolType "akida.PoolType"), optional) – pooling type (NoPooling, Max or Average). Defaults to Pooling.NoPooling.

*   **pool_stride** (_list_ _,_ _optional_) – list of 2 integers representing the stride dimensions. Defaults to (-1, -1).

*   **activation** (_bool_ _,_ _optional_) – enable or disable activation function. Defaults to True.

*   **act_bits** (_int_ _,_ _optional_) – number of bits used to quantize the neuron response. Defaults to 1.

## SeparableConvolutional[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#separableconvolutional "Permalink to this headline")

_class_ akida.SeparableConvolutional(_kernel\_size_, _filters_, _name=''_, _padding=<Padding.Same:1>_, _kernel\_stride=(1_, _1)_, _weights\_bits=2_, _pool\_size=(-1_, _-1)_, _pool\_type=<PoolType.NoPooling:0>_, _pool\_stride=(-1_, _-1)_, _activation=True_, _act\_bits=1_)[[source]](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/_modules/akida/layers/separable_convolutional.html#SeparableConvolutional)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.SeparableConvolutional "Permalink to this definition")
This represents a separable convolution layer.

This layer accepts 1-bit, 2-bit or 4-bit 3D input tensors with an arbitrary number of channels. It can be configured with 1-bit, 2-bit or 4-bit weights. Separable convolutions consist in first performing a depthwise spatial convolution (which acts on each input channel separately) followed by a pointwise convolution which mixes together the resulting output channels. Note: this layer applies a real convolution, and not a cross-correlation. It can optionally apply a step-wise ReLU activation to its outputs. The layer expects a 4D tensor whose first dimension is the sample index as input. It returns a 4D tensor whose first dimension is the sample index and the last dimension is the number of convolution filters. The order of the input spatial dimensions is preserved, but their value may change according to the convolution and pooling parameters.

Parameters
*   **kernel_size** (_list_) – list of 2 integer representing the spatial dimensions of the convolutional kernel.

*   **filters** (_int_) – number of pointwise filters.

*   **name** (_str_ _,_ _optional_) – name of the layer. Defaults to empty string.

*   **padding** ([`Padding`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Padding "akida.Padding"), optional) – type of convolution. Defaults to Padding.Same.

*   **kernel_stride** (_list_ _,_ _optional_) – list of 2 integer representing the convolution stride (X, Y). Defaults to (1, 1).

*   **weights_bits** (_int_ _,_ _optional_) – number of bits used to quantize weights. Defaults to 2.

*   **pool_size** (_list_ _,_ _optional_) – list of 2 integers, representing the window size over which to take the maximum or the average (depending on pool_type parameter). Defaults to (-1, -1).

*   **pool_type** ([`PoolType`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PoolType "akida.PoolType"), optional) – pooling type (NoPooling, Max or Average). Defaults to PoolType.NoPooling.

*   **pool_stride** (_list_ _,_ _optional_) – list of 2 integers representing the stride dimensions. Defaults to (-1, -1).

*   **activation** (_bool_ _,_ _optional_) – enable or disable activation function. Defaults to True.

*   **act_bits** (_int_ _,_ _optional_) – number of bits used to quantize the neuron response. Defaults to 1.

## Layer parameters[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#layer-parameters "Permalink to this headline")

### LayerType[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#layertype "Permalink to this headline")

_class_ akida.LayerType[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.LayerType "Permalink to this definition")
The layer type

Members:

> Unknown
> 
> 
> InputData
> 
> 
> InputConvolutional
> 
> 
> FullyConnected
> 
> 
> Convolutional
> 
> 
> SeparableConvolutional
> 
> 
> Add
> 
> 
> Dense2D
> 
> 
> Shiftmax
> 
> 
> Attention
> 
> 
> Stem
> 
> 
> MadNorm
> 
> 
> Concatenate

### Padding[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#padding "Permalink to this headline")

_class_ akida.Padding[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Padding "Permalink to this definition")
Sets the effective padding of the input for convolution, thereby determining the output dimensions. Naming conventions are the same as Keras/Tensorflow.

Members:

> Valid : No padding
> 
> 
> Same : Padded so that output size is input size divided by the stride

### PoolType[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#pooltype "Permalink to this headline")

_class_ akida.PoolType[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PoolType "Permalink to this definition")
The pooling type

Members:

> NoPooling : No pooling applied
> 
> 
> Max : Maximum pixel value is selected
> 
> 
> Average : Average pixel value is selected

## Optimizers[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#optimizers "Permalink to this headline")

_class_ akida.core.Optimizer[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.core.Optimizer "Permalink to this definition")
Optimizer generic parameters

**Methods:**

[`get`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.core.Optimizer.get "akida.core.Optimizer.get")(self,key)Retrieve a value from the LearningParams object.

get(_self:[akida.core.Optimizer](https://brainchip-inc.github.io/akida\_examples\_2.3.0-doc-1/api\_reference/akida\_apis.html#akida.core.Optimizer "akida.core.Optimizer")_, _key:str_)→float[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.core.Optimizer.get "Permalink to this definition")
Retrieve a value from the LearningParams object.

Parameters
**key** (_str_) – key of the value.

Returns
value associated to the key.

Return type
int

Raises
**ValueError** – if the value is not present in the LearningParams object.

_class_ akida.AkidaUnsupervised(_num\_weights:int_, _num\_classes:int=1_, _initial\_plasticity:float=1.0_, _learning\_competition:float=0.0_, _min\_plasticity:float=0.10000000149011612_, _plasticity\_decay:float=0.25_)→[akida.core.Optimizer](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.core.Optimizer "akida.core.Optimizer")[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.AkidaUnsupervised "Permalink to this definition")
Prepare the Akida Unsupervised optimizer for learning of the last layer.

Parameters
*   **num_weights** (_int_) – number of connections for each neuron.

*   **num_classes** (_int_ _,_ _optional_) – number of classes when running in a ‘labeled mode’.

*   **initial_plasticity** (_float_ _,_ _optional_) – defines how easily the weights will change when learning occurs.

*   **learning_competition** (_float_ _,_ _optional_) – controls competition between neurons.

*   **min_plasticity** (_float_ _,_ _optional_) – defines the minimum level to which plasticity will decay.

*   **plasticity_decay** (_float_ _,_ _optional_) – defines the decay of plasticity with each learning step.

*   **optimizer** (`akida.LearningParams`) – the optimizer used for learning

## Sequence[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#sequence "Permalink to this headline")

### Sequence[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#id2 "Permalink to this headline")

_class_ akida.Sequence[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Sequence "Permalink to this definition")
Represents a sequence of layers.

Sequences can be mapped in Software or on a Device.

**Attributes:**

[`backend`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Sequence.backend "akida.Sequence.backend")The backend type for this Sequence.
[`name`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Sequence.name "akida.Sequence.name")The name of the sequence
[`passes`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Sequence.passes "akida.Sequence.passes")Get the list of passes in this sequence.
[`program`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Sequence.program "akida.Sequence.program")Get the hardware program for this sequence.

_property_ backend[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Sequence.backend "Permalink to this definition")
The backend type for this Sequence.

_property_ name[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Sequence.name "Permalink to this definition")
The name of the sequence

_property_ passes[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Sequence.passes "Permalink to this definition")
Get the list of passes in this sequence.

_property_ program[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Sequence.program "Permalink to this definition")
Get the hardware program for this sequence.

Returns None if the Sequence is not compatible with the selected Device.

Returns
a bytes buffer or None

### BackendType[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#backendtype "Permalink to this headline")

_class_ akida.BackendType[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.BackendType "Permalink to this definition")
Members:

Software

Hardware

Hybrid

### Pass[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#pass "Permalink to this headline")

_class_ akida.Pass[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Pass "Permalink to this definition")
Represents a subset of the Sequence.

Hardware Sequences can typically be split into multiple passes on devices that support hardware partial reconfiguration feature, reducing the intervention of the software during inference.

**Attributes:**

[`layers`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Pass.layers "akida.Pass.layers")Get the list of layers in this pass.

_property_ layers[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Pass.layers "Permalink to this definition")
Get the list of layers in this pass.

## Device[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#device "Permalink to this headline")

### Device[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#id3 "Permalink to this headline")

_class_ akida.Device[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Device "Permalink to this definition")
**Attributes:**

[`desc`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Device.desc "akida.Device.desc")Returns the Device description
[`mesh`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Device.mesh "akida.Device.mesh")The device Mesh layout
[`version`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Device.version "akida.Device.version")The device hardware version.

_property_ desc[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Device.desc "Permalink to this definition")
Returns the Device description

Returns
a string describing the Device

_property_ mesh[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Device.mesh "Permalink to this definition")
The device Mesh layout

_property_ version[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Device.version "Permalink to this definition")
The device hardware version.

akida.devices()→List[[akida.core.HardwareDevice](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice "akida.core.HardwareDevice")][](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.devices "Permalink to this definition")
Returns the full list of available hardware devices

Returns
list of Device

akida.AKD1000()[[source]](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/_modules/akida/virtual_devices.html#AKD1000)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.AKD1000 "Permalink to this definition")
Returns a virtual device for an AKD1000 NSoC.

This function returns a virtual device for the Brainchip’s AKD1000 NSoC.

Returns
a virtual device.

Return type
[`Device`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Device "akida.Device")

akida.TwoNodesIP()[[source]](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/_modules/akida/virtual_devices.html#TwoNodesIP)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.TwoNodesIP "Permalink to this definition")
Returns a virtual device for a two nodes Akida IP.

Returns
a virtual device.

Return type
[`Device`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Device "akida.Device")

### HwVersion[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#hwversion "Permalink to this headline")

_class_ akida.HwVersion[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HwVersion "Permalink to this definition")
**Attributes:**

[`major_rev`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HwVersion.major_rev "akida.HwVersion.major_rev")The hardware major revision
[`minor_rev`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HwVersion.minor_rev "akida.HwVersion.minor_rev")The hardware minor revision
[`product_id`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HwVersion.product_id "akida.HwVersion.product_id")The hardware product identifier
[`vendor_id`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HwVersion.vendor_id "akida.HwVersion.vendor_id")The hardware vendor identifier

_property_ major_rev[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HwVersion.major_rev "Permalink to this definition")
The hardware major revision

_property_ minor_rev[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HwVersion.minor_rev "Permalink to this definition")
The hardware minor revision

_property_ product_id[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HwVersion.product_id "Permalink to this definition")
The hardware product identifier

_property_ vendor_id[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HwVersion.vendor_id "Permalink to this definition")
The hardware vendor identifier

## HWDevice[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#hwdevice "Permalink to this headline")

### HWDevice[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#id4 "Permalink to this headline")

_class_ akida.HardwareDevice[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice "Permalink to this definition")
**Methods:**

[`fit`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.fit "akida.HardwareDevice.fit")(*args,**kwargs)Overloaded function.
[`forward`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.forward "akida.HardwareDevice.forward")(self,arg0)Processes inputs on a programmed device.
[`predict`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.predict "akida.HardwareDevice.predict")(self,arg0)Processes inputs on a programmed device, returns a float array.
[`reset_top_memory`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.reset_top_memory "akida.HardwareDevice.reset_top_memory")(self)Reset the device memory informations
[`unprogram`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.unprogram "akida.HardwareDevice.unprogram")(self)Clear current program from hardware device, restoring its initial state

**Attributes:**

[`inference_power_events`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.inference_power_events "akida.HardwareDevice.inference_power_events")Copy of power events logged after inference
[`learn_enabled`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.learn_enabled "akida.HardwareDevice.learn_enabled")Property that enables/disables learning on current program (if possible).
[`learn_mem`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.learn_mem "akida.HardwareDevice.learn_mem")Property that retrieves learning layer's memory or updates a device using a serialized learning layer memory buffer.
[`memory`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.memory "akida.HardwareDevice.memory")The device memory usage and top usage (in bytes)
[`metrics`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.metrics "akida.HardwareDevice.metrics")The metrics from this device
[`program`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.program "akida.HardwareDevice.program")Property that retrieves current program or programs a device using a serialized program bytes object.
[`soc`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.soc "akida.HardwareDevice.soc")The SocDriver interface used by the device, or None if the device is not a SoC

fit(_*args_, _**kwargs_)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.fit "Permalink to this definition")
Overloaded function.

1.   fit(self: akida.core.HardwareDevice, inputs: numpy.ndarray[numpy.uint8], input_labels: float) -> numpy.ndarray

Learn from inputs on a programmed device.

1.   fit(self: akida.core.HardwareDevice, inputs: numpy.ndarray[numpy.uint8], input_labels: numpy.ndarray) -> numpy.ndarray

Learn from inputs on a programmed device.

1.   fit(self: akida.core.HardwareDevice, inputs: numpy.ndarray[numpy.uint8], input_labels: list = []) -> numpy.ndarray

Learn from inputs on a programmed device.

forward(_self:[akida.core.HardwareDevice](https://brainchip-inc.github.io/akida\_examples\_2.3.0-doc-1/api\_reference/akida\_apis.html#akida.HardwareDevice "akida.core.HardwareDevice")_, _arg0:numpy.ndarray[numpy.uint8]_)→numpy.ndarray[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.forward "Permalink to this definition")
Processes inputs on a programmed device.

Parameters
**inputs** – `numpy.ndarray` with shape matching current program

:return `numpy.ndarray` with outputs from the device

_property_ inference_power_events[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.inference_power_events "Permalink to this definition")
Copy of power events logged after inference

_property_ learn_enabled[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.learn_enabled "Permalink to this definition")
Property that enables/disables learning on current program (if possible).

_property_ learn_mem[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.learn_mem "Permalink to this definition")
Property that retrieves learning layer’s memory or updates a device using a serialized learning layer memory buffer.

_property_ memory[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.memory "Permalink to this definition")
The device memory usage and top usage (in bytes)

_property_ metrics[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.metrics "Permalink to this definition")
The metrics from this device

predict(_self:[akida.core.HardwareDevice](https://brainchip-inc.github.io/akida\_examples\_2.3.0-doc-1/api\_reference/akida\_apis.html#akida.HardwareDevice "akida.core.HardwareDevice")_, _arg0:numpy.ndarray[numpy.uint8]_)→numpy.ndarray[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.predict "Permalink to this definition")
Processes inputs on a programmed device, returns a float array.

Parameters
**inputs** – `numpy.ndarray` with shape matching current program

:return `numpy.ndarray` with float outputs from the device

_property_ program[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.program "Permalink to this definition")
Property that retrieves current program or programs a device using a serialized program bytes object.

reset_top_memory(_self:[akida.core.HardwareDevice](https://brainchip-inc.github.io/akida\_examples\_2.3.0-doc-1/api\_reference/akida\_apis.html#akida.HardwareDevice "akida.core.HardwareDevice")_)→None[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.reset_top_memory "Permalink to this definition")
Reset the device memory informations

_property_ soc[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.soc "Permalink to this definition")
The SocDriver interface used by the device, or None if the device is not a SoC

unprogram(_self:[akida.core.HardwareDevice](https://brainchip-inc.github.io/akida\_examples\_2.3.0-doc-1/api\_reference/akida\_apis.html#akida.HardwareDevice "akida.core.HardwareDevice")_)→None[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.HardwareDevice.unprogram "Permalink to this definition")
Clear current program from hardware device, restoring its initial state

### SocDriver[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#socdriver "Permalink to this headline")

_class_ akida.core.SocDriver[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.core.SocDriver "Permalink to this definition")
**Attributes:**

[`clock_mode`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.core.SocDriver.clock_mode "akida.core.SocDriver.clock_mode")Clock mode of the NSoC.
[`power_measurement_enabled`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.core.SocDriver.power_measurement_enabled "akida.core.SocDriver.power_measurement_enabled")Power measurement is off by default.
[`power_meter`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.core.SocDriver.power_meter "akida.core.SocDriver.power_meter")Power meter associated to the SoC.

_property_ clock_mode[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.core.SocDriver.clock_mode "Permalink to this definition")
Clock mode of the NSoC.

_property_ power_measurement_enabled[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.core.SocDriver.power_measurement_enabled "Permalink to this definition")
Power measurement is off by default. Toggle it on to get power information in the statistics or when calling PowerMeter.events().

_property_ power_meter[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.core.SocDriver.power_meter "Permalink to this definition")
Power meter associated to the SoC.

### ClockMode[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#clockmode "Permalink to this headline")

_class_ akida.core.soc.ClockMode[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.core.soc.ClockMode "Permalink to this definition")
Clock mode configuration

Members:

> Performance
> 
> 
> Economy
> 
> 
> LowPower

## PowerMeter[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#powermeter "Permalink to this headline")

_class_ akida.PowerMeter[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PowerMeter "Permalink to this definition")
Gives access to power measurements.

When power measurements are enabled for a specific device, this object stores them as a list of `PowerEvent` objects. The events list cannot exceed a predefined size: when it is full, older events are replaced by newer events.

**Methods:**

[`events`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PowerMeter.events "akida.PowerMeter.events")(self)Retrieve all pending events

**Attributes:**

[`floor`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PowerMeter.floor "akida.PowerMeter.floor")Get the floor power

events(_self:[akida.core.PowerMeter](https://brainchip-inc.github.io/akida\_examples\_2.3.0-doc-1/api\_reference/akida\_apis.html#akida.PowerMeter "akida.core.PowerMeter")_)→List[[akida.core.PowerEvent](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PowerEvent "akida.core.PowerEvent")][](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PowerMeter.events "Permalink to this definition")
Retrieve all pending events

_property_ floor[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PowerMeter.floor "Permalink to this definition")
Get the floor power

_class_ akida.PowerEvent[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PowerEvent "Permalink to this definition")
A timestamped power measurement.

Each PowerEvent contains: - a voltage value in µV (microvolt), - a current value in mA (milliampere), - the corresponding power value in mW (milliwatt).

**Attributes:**

[`current`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PowerEvent.current "akida.PowerEvent.current")Current value in mA
[`power`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PowerEvent.power "akida.PowerEvent.power")Power value in mW
[`ts`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PowerEvent.ts "akida.PowerEvent.ts")Timestamp of the event
[`voltage`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PowerEvent.voltage "akida.PowerEvent.voltage")Voltage value in µV

_property_ current[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PowerEvent.current "Permalink to this definition")
Current value in mA

_property_ power[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PowerEvent.power "Permalink to this definition")
Power value in mW

_property_ ts[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PowerEvent.ts "Permalink to this definition")
Timestamp of the event

_property_ voltage[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.PowerEvent.voltage "Permalink to this definition")
Voltage value in µV

## NP[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#np "Permalink to this headline")

_class_ akida.NP.Mesh[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mesh "Permalink to this definition")
**Attributes:**

[`dma_conf`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mesh.dma_conf "akida.NP.Mesh.dma_conf")DMA configuration endpoint
[`dma_event`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mesh.dma_event "akida.NP.Mesh.dma_event")DMA event endpoint
[`nps`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mesh.nps "akida.NP.Mesh.nps")Neural processors

_property_ dma_conf[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mesh.dma_conf "Permalink to this definition")
DMA configuration endpoint

_property_ dma_event[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mesh.dma_event "Permalink to this definition")
DMA event endpoint

_property_ nps[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mesh.nps "Permalink to this definition")
Neural processors

_class_ akida.NP.Info[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Info "Permalink to this definition")
**Attributes:**

[`ident`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Info.ident "akida.NP.Info.ident")NP identifier
[`types`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Info.types "akida.NP.Info.types")NP supported types

_property_ ident[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Info.ident "Permalink to this definition")
NP identifier

_property_ types[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Info.types "Permalink to this definition")
NP supported types

_class_ akida.NP.Ident[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Ident "Permalink to this definition")
**Attributes:**

[`col`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Ident.col "akida.NP.Ident.col")NP column number
[`id`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Ident.id "akida.NP.Ident.id")NP id
[`row`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Ident.row "akida.NP.Ident.row")NP row number

_property_ col[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Ident.col "Permalink to this definition")
NP column number

_property_ id[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Ident.id "Permalink to this definition")
NP id

_property_ row[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Ident.row "Permalink to this definition")
NP row number

_class_ akida.NP.Type[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Type "Permalink to this definition")
Members:

HRC : High Resolution Convolution

CNP1 : Convolutional Neural Processor Type 1

CNP2 : Convolutional Neural Processor Type 2

FNP2 : FullyConnected Neural Processor (external memory)

FNP3 : FullyConnected Neural Processor (internal memory)

_class_ akida.NP.Mapping[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mapping "Permalink to this definition")
The mapping of a subset of a Layer on a Neural Processor”

**Attributes:**

[`filters`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mapping.filters "akida.NP.Mapping.filters")Number of filters processed by the Neural Processor
[`ident`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mapping.ident "akida.NP.Mapping.ident")Neural Processor identifier
[`single_buffer`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mapping.single_buffer "akida.NP.Mapping.single_buffer")Neural Processor uses a single or dual input buffer
[`type`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mapping.type "akida.NP.Mapping.type")Neural Processor type

_property_ filters[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mapping.filters "Permalink to this definition")
Number of filters processed by the Neural Processor

_property_ ident[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mapping.ident "Permalink to this definition")
Neural Processor identifier

_property_ single_buffer[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mapping.single_buffer "Permalink to this definition")
Neural Processor uses a single or dual input buffer

_property_ type[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.NP.Mapping.type "Permalink to this definition")
Neural Processor type

## Tools[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#tools "Permalink to this headline")

### Sparsity[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#sparsity "Permalink to this headline")

akida.evaluate_sparsity(_model_, _inputs_)[[source]](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/_modules/akida/sparsity.html#evaluate_sparsity)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.evaluate_sparsity "Permalink to this definition")
Evaluate the sparsity of a Model on a set of inputs

Parameters
*   **model** ([`Model`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.Model "akida.Model")) – the model to evaluate

*   **inputs** (`numpy.ndarray`) – a numpy.ndarray

Returns
a dictionary of float sparsity values indexed by layers

### Compatibility[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#compatibility "Permalink to this headline")

akida.compatibility.create_from_model(_model_)[[source]](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/_modules/akida/compatibility/conversion.html#create_from_model)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.compatibility.create_from_model "Permalink to this definition")
Tries to create a HW compatible model from an incompatible one

Tries to create a HW compatible model from an incompatible one, using SW workarounds for known limitations. It returns a converted model that is not guaranteed to be HW compatible, depending if workaround have been found.

Parameters
**model** (`Model`) – a Model object to convert

Returns
a new Model with no guarantee that it is HW compatible.

Return type
`Model`

akida.compatibility.transpose(_model_)[[source]](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/_modules/akida/compatibility/conversion.html#transpose)[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.compatibility.transpose "Permalink to this definition")
Transpose the weights of a legacy (pre-2.1.4) model

This only applies to:

*   models converted using cnn2snn,

*   models instantiated using the Sequential API starting with an InputConvolutional.

Models instantiated using the Sequential API starting with an InputData don’t need to have their weights transposed.

Parameters
**model** (`Model`) – a Model object whose weights need transposing

Returns
a new Model with transposed weights

Return type
`Model`

**Miscellaneous:**

[`statistics`](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.statistics "akida.statistics")Get statistics by sequence for this model.

akida.statistics[](https://brainchip-inc.github.io/akida_examples_2.3.0-doc-1/api_reference/akida_apis.html#akida.statistics "Permalink to this definition")
Get statistics by sequence for this model.

Returns
a dictionary of `SequenceStatistics` indexed by name.
