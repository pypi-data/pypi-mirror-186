import logging
from typing import Type, Dict, Optional, Set

import tensorflow as tf
from keras import Model
from keras.layers import Permute, TFOpLambda
from tensorflow import keras

from keras_data_format_converter.modelconverter import ModelConverter, calculate_permute_values
from keras_data_format_converter.utils import configure_logger


def convert_channels_first_to_last(model: keras.Model,
                                   should_transform_inputs_and_outputs=False,
                                   custom_layers: Optional[Dict[str, Type[tf.keras.layers.Layer]]] = None,
                                   verbose: bool = False) -> keras.Model:
    """
        Convert keras models from channels first to last

        :param model: keras model to convert in channels first format
        :type model: tensorflow.keras.Model
        :param should_transform_inputs_and_outputs: set to transfrom data format of inputs and outputs, by default False
        :type should_transform_inputs_and_outputs: bool
        :param custom_layers: dictionary of custom layers
        :type custom_layers: Optional[Dict[str, Type[tf.keras.layers.Layer]]]
        :param verbose: by default true, set to False to lower the logging level
        :type verbose: bool
        :return: converted keras model in channels last format
        :rtype: tensorflow.keras.Model
    """

    custom_layer_names = set(custom_layers.keys()) if custom_layers else set()
    model = _add_identity_layers_after_inputs(model, custom_layer_names)
    converted_model = _convert_channels(model, custom_layers, verbose)
    if should_transform_inputs_and_outputs:
        converted_model = _transform_inputs_and_outputs(converted_model)

    return converted_model


def _convert_channels(model: tf.keras.Model,
                      custom_layers: Optional[Dict[str, Type[tf.keras.layers.Layer]]], verbose: bool) \
        -> tf.keras.Model:
    # configure logger
    configure_logger(verbose)
    logger = logging.getLogger(__name__)

    if custom_layers is None:
        custom_layers = {}

    model_converter = ModelConverter(model, custom_layers)
    converted_model = model_converter.convert_model()
    return converted_model


def _add_identity_layers_after_inputs(k_model: Model, custom_layers_names: Set[str]) -> Model:
    def _is_input_connected_to_call_args_layer(_input_tensor):
        for outbound_node in _input_tensor.node.layer.outbound_nodes:
            if isinstance(outbound_node.layer, TFOpLambda) or \
                    outbound_node.layer.__class__.__name__ in custom_layers_names:
                return True
        return False

    new_inputs = []
    new_call_inputs = []
    for k_input in k_model.inputs:
        if k_input.shape[0] is None:
            new_input_tensor = tf.keras.Input(k_input.shape[1:], name=k_input.name)
        else:
            new_input_tensor = tf.keras.Input(k_input.shape[1:], name=k_input.name, batch_size=k_input.shape[0])
        new_inputs.append(new_input_tensor)
        if not _is_input_connected_to_call_args_layer(k_input):
            new_call_inputs.append(new_input_tensor)
            continue

        new_call_inputs.append(tf.identity(new_input_tensor))

    # clear the old inbound_nodes
    for layer in k_model.layers:
        layer.inbound_nodes.clear()

    new_outputs = k_model.call(new_call_inputs)

    return Model(inputs=new_inputs, outputs=new_outputs)


def _transform_inputs_and_outputs(k_model: Model) -> Model:
    new_inputs = []
    new_old_inputs = []
    for k_input in k_model.inputs:
        new_input_shape = Permute(
            calculate_permute_values(k_input.shape, to_channel_first=False))(k_input).shape[1:]
        if k_input.shape[0] is None:
            new_input_tensor = tf.keras.Input(new_input_shape, name=k_input.name)
        else:
            new_input_tensor = tf.keras.Input(new_input_shape, name=k_input.name, batch_size=k_input.shape[0])
        back_to_channel_first_perm_values = calculate_permute_values(new_input_tensor.shape, to_channel_first=True)
        permute_after = Permute(back_to_channel_first_perm_values)(new_input_tensor)
        new_inputs.append(new_input_tensor)
        new_old_inputs.append(permute_after)

    # clear the old inbound_nodes
    for layer in k_model.layers:
        layer.inbound_nodes.clear()

    new_outputs = []
    new_old_outputs = k_model.call(new_old_inputs)
    if not isinstance(new_old_outputs, list):
        new_old_outputs = [new_old_outputs]
    for output in new_old_outputs:
        perm_values = calculate_permute_values(output.shape, to_channel_first=False)
        new_outputs.append(Permute(perm_values)(output))

    return Model(inputs=new_inputs, outputs=new_outputs)
