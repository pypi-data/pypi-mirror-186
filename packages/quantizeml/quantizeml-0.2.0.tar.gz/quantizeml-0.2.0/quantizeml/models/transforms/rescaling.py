#!/usr/bin/env python
# ******************************************************************************
# Copyright 2022 Brainchip Holdings Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ******************************************************************************
"""
Rescaling transformation for quantized models.
"""
import numpy as np

from keras.layers import Rescaling, Conv2D, Dense

from ...layers.convolution import PaddedConv2D
from ...models.utils import deep_clone_model

__all__ = ["align_rescaling"]


def align_rescaling(model):
    """Aligns the Rescaling layer of the model to make it quantization ready.

    This aligns the Rescaling scale to a single scalar, adjusting the weights of
    the next layer.

    This also folds the offset into the bias of next layer.

    The resulting Rescaling is therefore compatible with a quantization to a
    QuantizedRescaling.

    If the source model does not contain a Rescaling or if its Rescaling is already
    aligned, then the original model is returned.

    Args:
        model (keras.Model): the source Keras model

    Returns:
        keras.Model: the original model or a new model with Rescaling layer aligned
    """
    supported_dst_layers = [Conv2D, Dense]

    # Find the model has a Rescaling layer and check limitations on folding
    rescaling_layer = None
    dst_layer = None

    for ly in model.layers:
        if isinstance(ly, Rescaling):
            scale_per_axis = isinstance(ly.scale, list) and len(ly.scale) > 1
            if not scale_per_axis and ly.offset == 0:
                # Rescaling is already aligned: nothing to do
                break
            # Alignment is limited to single outbound node Rescaling layers
            if len(ly.outbound_nodes) != 1:
                raise ValueError("Found a non-aligned Rescaling layer in the model with multiple "
                                 "outbounds which is not supported.")
            # Retrieve the destination layer and check its type
            dst_layer = ly.outbound_nodes[0].layer
            if type(dst_layer) not in supported_dst_layers:
                raise ValueError(f"Layer type {type(dst_layer)} after Rescaling not supported, "
                                 "must be Conv2D or Dense.")
            # When destination layer is a Conv2D with padding 'same', reject:
            #   - offsets defined per axis,
            #   - scales defined per axis when offset is not null.
            # Otherwise it would require a padding value per-axis which is not supported.
            same_conv2d = (isinstance(dst_layer, Conv2D)
                           and dst_layer.get_config()['padding'].lower() == 'same')
            offset_per_axis = isinstance(ly.offset, list) and len(ly.offset) > 1
            if same_conv2d and (offset_per_axis or ly.offset != 0 and scale_per_axis):
                raise NotImplementedError("Folding an offset per-axis or with a scale per-axis "
                                          "into a Conv2D with 'same' padding is not supported.")
            # Rescaling was found, exit the loop
            rescaling_layer = ly
            break

    # If no Rescaling that required an aligment was found
    if rescaling_layer is None:
        # Simply return the original model
        return model

    # Clone model
    def replace_layer(layer):
        config = layer.get_config()
        if layer.name == dst_layer.name:
            # Force bias if there is a rescaling offset
            if rescaling_layer.offset != 0:
                config['use_bias'] = True
                # Replace Conv2D with 'same' padding by PaddedConv2D with correct padding value
                if isinstance(dst_layer, Conv2D) and config['padding'].lower() == 'same':
                    # Offset has a single value at this point
                    offset = rescaling_layer.offset[0] if isinstance(
                        rescaling_layer.offset, list) else rescaling_layer.offset
                    config['padding_value'] = float(-offset)
                    return PaddedConv2D.from_config(config)
        return layer.__class__.from_config(config)

    aligned_model = deep_clone_model(model, clone_function=replace_layer)
    rescaling_layer = aligned_model.get_layer(rescaling_layer.name)
    next_layer = aligned_model.get_layer(dst_layer.name)

    # Set weights in the layer of the new model, using the Rescaling parameters:
    base_weights = next_layer.get_weights()
    new_w = base_weights[0].copy()
    filters = new_w.shape[-1]

    scale = rescaling_layer.scale
    if isinstance(scale, list) and len(scale) > 1:
        # If scale is not a scalar, align it
        target_scale = np.mean(scale)
        rescaling_layer.scale = target_scale
        # To compensate, adjust the weights of the next layer
        for i in range(filters):
            # Rescale weights filter by filter to enable broadcast
            new_w[..., i] *= scale / target_scale
        if isinstance(next_layer, PaddedConv2D):
            # Also rescale the padding value
            next_layer._padding_value *= scale / target_scale
    new_weights = [new_w]

    if next_layer.use_bias:
        # Build zero initialized biases if the original layer didn't have any
        new_biases = base_weights[1].copy() if dst_layer.use_bias else np.zeros(filters)
        # new_biases = base_biases + sum(base_weights_per_filter * offset)
        for i in range(filters):
            # Rescale biases filter by filter to enable broadcast if offsets are per channel
            w_i = base_weights[0][..., i]
            new_biases[i] += np.sum(w_i * rescaling_layer.offset)
        new_weights += [new_biases]
        rescaling_layer.offset = 0

    next_layer.set_weights(new_weights)
    return aligned_model
