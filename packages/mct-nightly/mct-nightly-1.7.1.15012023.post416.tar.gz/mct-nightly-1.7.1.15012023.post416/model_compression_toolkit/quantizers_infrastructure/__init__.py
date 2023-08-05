# Copyright 2023 Sony Semiconductor Israel, Inc. All rights reserved.
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

from model_compression_toolkit.core.common.target_platform import QuantizationMethod
from model_compression_toolkit.quantizers_infrastructure.common.base_inferable_quantizer import QuantizationTarget, BaseInferableQuantizer
from model_compression_toolkit.quantizers_infrastructure.keras.base_keras_quantizer import BaseKerasTrainableQuantizer
from model_compression_toolkit.quantizers_infrastructure.keras.keras_node_quantization_dispatcher import \
    KerasNodeQuantizationDispatcher
from model_compression_toolkit.quantizers_infrastructure.keras.load_model import keras_load_quantized_model
from model_compression_toolkit.quantizers_infrastructure.keras.quantize_wrapper import KerasQuantizationWrapper
from model_compression_toolkit.quantizers_infrastructure.pytorch.base_pytorch_quantizer import \
    BasePytorchTrainableQuantizer
from model_compression_toolkit.quantizers_infrastructure.pytorch.pytorch_node_quantization_dispatcher import \
    PytorchNodeQuantizationDispatcher
from model_compression_toolkit.quantizers_infrastructure.pytorch.quantize_wrapper import PytorchQuantizationWrapper
from model_compression_toolkit.quantizers_infrastructure.keras import inferable_quantizers as keras_inferable_quantizers
from model_compression_toolkit.quantizers_infrastructure.keras.inferable_quantizers.base_keras_inferable_quantizer import BaseKerasInferableQuantizer
