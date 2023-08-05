# Copyright 2022 Sony Semiconductor Israel, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from typing import Dict
from model_compression_toolkit.core import common
from model_compression_toolkit.core.common.framework_info import FrameworkInfo
from model_compression_toolkit import quantizers_infrastructure as qi
from model_compression_toolkit.qat.pytorch.quantizer.ste_rounding.symmetric_ste import STEWeightQuantizer, STEActivationQuantizer
from model_compression_toolkit.qat.pytorch.quantizer.ste_rounding.uniform_ste import STEUniformWeightQuantizer, STEUniformActivationQuantizer


METHOD2WEIGHTQUANTIZER = {qi.QuantizationMethod.SYMMETRIC: STEWeightQuantizer,
                          qi.QuantizationMethod.POWER_OF_TWO: STEWeightQuantizer,
                          qi.QuantizationMethod.UNIFORM: STEUniformWeightQuantizer}


METHOD2ACTQUANTIZER = {qi.QuantizationMethod.SYMMETRIC: STEActivationQuantizer,
                       qi.QuantizationMethod.POWER_OF_TWO: STEActivationQuantizer,
                       qi.QuantizationMethod.UNIFORM: STEUniformActivationQuantizer}


def quantization_dispatcher_builder(n: common.BaseNode,
                                    fw_info: FrameworkInfo,
                                    method2weightquantizer: Dict[
                                        qi.QuantizationMethod, qi.BasePytorchTrainableQuantizer] = None,
                                    method2actquantizer: Dict[
                                        qi.QuantizationMethod, qi.BasePytorchTrainableQuantizer] = None
                                    ) -> qi.PytorchNodeQuantizationDispatcher:

    """
    Build a NodeQuantizationDispatcher for a node according to its quantization configuration and
    a global NoOpQuantizeConfig object.

    Args:
        n: Node to build its QuantizeConfig.
        fw_info: Framework information (e.g., mapping from layers to their attributes to quantize).
        method2weightquantizer: A mapping between quantization method to weight quantizer.
        method2actquantizer: A mapping between quantization method to activation quantizer.

    Returns:
        A QuantizeConfig object with the appropriate quantizers (according to the node's
        quantization configuration).
    """
    if method2weightquantizer is None:
        method2weightquantizer = METHOD2WEIGHTQUANTIZER
    if method2actquantizer is None:
        method2actquantizer = METHOD2ACTQUANTIZER

    nqd = qi.PytorchNodeQuantizationDispatcher()
    if n.is_weights_quantization_enabled():
        attributes = fw_info.get_kernel_op_attributes(n.type)
        for attr in attributes:
            quantizer_class = method2weightquantizer.get(n.final_weights_quantization_cfg.weights_quantization_method)
            if quantizer_class is None:
                common.Logger.error(
                    f'Unknown Quantiztion method for weights: {n.final_weights_quantization_cfg.weights_quantization_method}')
            nqd.add_weight_quantizer(attr, quantizer_class(n.final_weights_quantization_cfg))

    if n.is_activation_quantization_enabled():
        quantizer_class = method2actquantizer.get(
            n.final_activation_quantization_cfg.activation_quantization_method)
        if quantizer_class is None:
            common.Logger.error(
                f'Unknown Quantization method for activations: {n.final_activation_quantization_cfg.activation_quantization_method}')
        nqd.activation_quantizers = [quantizer_class(n.final_activation_quantization_cfg)]

    return nqd
