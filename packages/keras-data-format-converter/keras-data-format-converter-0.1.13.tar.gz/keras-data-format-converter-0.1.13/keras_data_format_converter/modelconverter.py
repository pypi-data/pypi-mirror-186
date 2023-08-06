import logging
from typing import List, Dict, Union, Tuple, Type

import tensorflow as tf
from keras.engine.keras_tensor import KerasTensor
from keras.layers.core import TFOpLambda

from tensorflow import keras, TensorShape
from keras.layers import Layer, InputLayer, Input, MultiHeadAttention
from tensorflow.python.keras.engine.node import Node

from keras_data_format_converter.layers.layer_utils import convert_layer, onnx_channel_first_cant_run_on_cpu_layers


def calculate_permute_values(input_shape: TensorShape, to_channel_first: bool) -> List[int]:
    n_dims = len(input_shape)
    if to_channel_first:
        return [n_dims - 1] + list(range(1, n_dims - 1))
    else:
        return list(range(2, n_dims)) + [1]


class ModelConverter:
    """The ModelConverter object converts keras models to the requested data_format

    The conversion process is handling special layers with data_format specific values like Concatenate,
    BatchNormalization, Reshape, etc. The logic of handling those layers is as follows:
    every special layer after an input from inputs_to_transpose until a layer with shape rank of 2 is being handled.

    :param model: The model to convert
    :type model: tensorflow.keras.Model
    """

    def __init__(self, model: keras.Model, custom_layers: Dict[str, Type[tf.keras.layers.Layer]]):
        self.model: keras.Model = model

        # cache properties
        self._clear_cache()

        # logger
        self._logger = logging.getLogger(__name__)

        self.custom_layers = custom_layers

    def convert_model(self) -> keras.Model:
        """
        Converting model to the requested target_data_format

        :return: Converted model
        :rtype: tensorflow.keras.Model
        """

        self._clear_cache()
        output_tensors: List[tf.Tensor] = []
        for out_tensor in self.model.outputs:
            converted_tensor = self._convert_tensor(out_tensor)
            output_tensors.append(converted_tensor)
        converted_model = tf.keras.Model(inputs=self._model_input_tensors, outputs=output_tensors)
        return converted_model

    def _find_tensor_index_by_name(self, node_input_tensors: List[KerasTensor], tensor_name: str) -> int:
        node_input_tensor_names = []
        for tensor in node_input_tensors:
            if tensor.name in self._tensor_name_to_original_tensor_name:
                node_input_tensor_names.append(self._tensor_name_to_original_tensor_name[tensor.name])
            else:
                node_input_tensor_names.append(tensor.name)

        return node_input_tensor_names.index(tensor_name)

    def _replace_tensors_in_call_args(self, call_args: Union[List, Dict], node_input_tensors: List[KerasTensor]
                                      ) -> Tuple[Union[List, Dict], List[KerasTensor]]:
        new_args = call_args.copy()
        if isinstance(new_args, dict):
            args_to_enumerate = new_args.values()
            args_keys = new_args.keys()
        else:
            args_to_enumerate = new_args
            args_keys = range(len(args_to_enumerate))

        for i_k, arg in zip(args_keys, args_to_enumerate):
            if isinstance(arg, (dict, list)):
                new_arg, node_input_tensors = self._replace_tensors_in_call_args(arg, node_input_tensors)
                new_args[i_k] = new_arg
            elif isinstance(arg, KerasTensor):
                try:
                    tensor_index = self._find_tensor_index_by_name(node_input_tensors, arg.name)
                    new_args[i_k] = node_input_tensors.pop(tensor_index)
                except (IndexError, ValueError):
                    pass
        return new_args, node_input_tensors

    def _default_call_layer_by_args(self,
                                    converted_layer: Layer, call_args: Tuple, call_kwargs: Dict,
                                    node_input_tensors: List[KerasTensor]) -> KerasTensor:
        new_call_args, input_tensors = self._replace_tensors_in_call_args(list(call_args), node_input_tensors)
        new_kwargs, input_tensors = self._replace_tensors_in_call_args(call_kwargs, node_input_tensors)
        if len(node_input_tensors) > 0:
            raise Exception(f"Failed to call layer {converted_layer.name}. "
                            f"Couldn't find a match for some input tensors")

        return converted_layer(*new_call_args, **new_kwargs)

    def _call_layer_by_args(
            self, converted_layer: Layer, node_input_tensors: Union[KerasTensor, List[KerasTensor]],
            current_layer: Layer) -> KerasTensor:

        call_args = current_layer.inbound_nodes[0].call_args
        call_kwargs = current_layer.inbound_nodes[0].call_kwargs
        if not isinstance(node_input_tensors, list):
            node_input_tensors = [node_input_tensors]

        return self._default_call_layer_by_args(converted_layer, call_args, call_kwargs, node_input_tensors)

    def _convert_tensor(self, tensor: tf.Tensor) -> tf.Tensor:
        tensor_id = id(tensor)
        converted_tensor = self._tensor_cache.get(tensor_id)
        if converted_tensor is not None:
            return converted_tensor

        current_node = self._get_node_from_tensor(tensor)
        current_layer = self._get_layer_from_tensor(tensor)
        # Creating first model input layer
        if isinstance(current_layer, InputLayer):
            input_tensor = self._convert_input_tensor(tensor)
            self._tensor_cache[tensor_id] = input_tensor
            self._model_input_tensors.append(input_tensor)
            return input_tensor

        # get all input tensors
        node_input_tensors = []
        parent_nodes = current_node.parent_nodes
        for parent_node in parent_nodes:
            output_tensor = parent_node.outputs
            node_input_tensor = self._convert_tensor(output_tensor)
            node_input_tensors.append(node_input_tensor)

        layer_input_shape = [node_input_tensor.shape for node_input_tensor in node_input_tensors]

        if len(node_input_tensors) == 1:
            node_input_tensors = node_input_tensors[0]
            layer_input_shape = layer_input_shape[0]

        layer_name = current_layer.name
        converted_layer = self._layer_cache.get(layer_name)
        converted_layer_built = True
        if converted_layer is None:
            # special case of build layers:
            converted_layer, converted_layer_built = convert_layer(current_layer, layer_input_shape, self.custom_layers)
            self._layer_cache[layer_name] = converted_layer

        if converted_layer_built:
            if isinstance(converted_layer, TFOpLambda):
                converted_tensor = self._call_layer_by_args(converted_layer, node_input_tensors, current_layer)
            else:
                converted_tensor = converted_layer(node_input_tensors)
        elif isinstance(current_layer, MultiHeadAttention):
            weights = current_layer.get_weights()
            converted_tensor = converted_layer(*node_input_tensors)
            converted_layer.set_weights(weights)
        elif isinstance(converted_layer, onnx_channel_first_cant_run_on_cpu_layers) and \
                current_layer.get_config()['data_format'] == 'channels_first':
            perm_values = calculate_permute_values(node_input_tensors.shape, to_channel_first=False)
            permute_before = tf.keras.layers.Permute(perm_values)(node_input_tensors)
            tensor = converted_layer(permute_before)
            weights = current_layer.get_weights()
            converted_layer.set_weights(weights)
            perm_values = calculate_permute_values(tensor.shape, to_channel_first=True)
            permute_after = tf.keras.layers.Permute(perm_values)(tensor)
            self._tensor_name_to_original_tensor_name[permute_after.name] = tensor.name
            converted_tensor = permute_after
        elif type(converted_layer) in self.custom_layers.values():
            converted_tensor = self._call_layer_by_args(converted_layer, node_input_tensors, current_layer)
            weights = current_layer.get_weights()
            converted_layer.set_weights(weights)
        else:
            weights = current_layer.get_weights()
            converted_tensor = converted_layer(node_input_tensors)
            converted_layer.set_weights(weights)

        self._tensor_cache[tensor_id] = converted_tensor

        # for layers that don't implements the name override
        self._tensor_name_to_original_tensor_name[converted_tensor.name] = tensor.name

        return converted_tensor

    @staticmethod
    def _get_layer_from_tensor(tensor: tf.Tensor) -> Layer:
        history = tensor._keras_history
        layer = history.layer
        return layer

    @staticmethod
    def _get_node_from_tensor(tensor: tf.Tensor) -> Node:
        history = tensor._keras_history
        layer = history.layer
        node_index = history.node_index
        node = layer.inbound_nodes[node_index]
        return node

    def _convert_input_tensor(self, input_tensor: tf.Tensor) -> tf.Tensor:
        input_layer = input_tensor._keras_history.layer
        inp_config = input_layer.get_config()
        if 'name' in inp_config and '.' in inp_config['name']:
            new_name_without_dots = inp_config['name'].replace(".", "_")
            self._tensor_name_to_original_tensor_name[new_name_without_dots] = inp_config['name']
            inp_config['name'] = new_name_without_dots
        new_input_tensor = Input(**inp_config)
        self._logger.debug(f"Input created, name: {new_input_tensor.name}, shape: {new_input_tensor.shape}")
        return new_input_tensor

    def _clear_cache(self) -> None:
        self._layer_cache: Dict[str, Layer] = {}
        self._tensor_cache: Dict[int, tf.Tensor] = {}
        self._model_input_tensors: List[tf.Tensor] = []
        self._tensor_name_to_original_tensor_name: Dict[str, str] = {}
