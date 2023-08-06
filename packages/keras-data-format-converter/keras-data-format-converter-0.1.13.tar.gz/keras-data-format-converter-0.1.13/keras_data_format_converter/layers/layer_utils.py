import logging
from typing import List, Dict, Type, Tuple
import tensorflow as tf
from keras.layers import Layer, MultiHeadAttention

from keras.layers.pooling.base_pooling1d import Pooling1D
from keras.layers.pooling.base_pooling2d import Pooling2D
from keras.layers.pooling.base_pooling3d import Pooling3D
from keras.saving.legacy.saved_model.load import RevivedLayer
from keras.layers.convolutional.base_conv import Conv
from keras_data_format_converter.layers.confighandlers.dataformat import handle_data_format


onnx_channel_first_cant_run_on_cpu_layers = (Conv, Pooling1D, Pooling2D, Pooling3D)
layers_to_build_on_call = onnx_channel_first_cant_run_on_cpu_layers + (MultiHeadAttention,)


def convert_layer(current_layer: Layer, input_shape: List[int],
                  custom_layers: Dict[str, Type[tf.keras.layers.Layer]]) \
        -> Tuple[Layer, bool]:
    logger = logging.getLogger(__name__)
    config = current_layer.get_config()

    if isinstance(current_layer, RevivedLayer):
        logger.debug(f"Layer skipped, name: {current_layer.name}, type: {current_layer.__class__.__name__},"
                     f" input_shape: {current_layer.input_shape}, output_shape: {current_layer.output_shape}")
        is_built = True
        return current_layer, is_built

    if isinstance(current_layer, onnx_channel_first_cant_run_on_cpu_layers):
        config = handle_data_format('channels_last', config)

    converted_layer = type(current_layer).from_config(config)
    is_built = True
    if isinstance(current_layer, layers_to_build_on_call) or isinstance(current_layer, tuple(custom_layers.values())):
        is_built = False
        return converted_layer, is_built

    weights = current_layer.get_weights()
    converted_layer.build(input_shape)
    converted_layer.set_weights(weights)
    logger.debug(f"Layer created, name: {converted_layer.name}, type: {current_layer.__class__.__name__},"
                 f" input_shape: {current_layer.input_shape}, output_shape: {current_layer.output_shape}")
    return converted_layer, is_built
