# Copyright 2023 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.
"""
Deprecated functions.
"""

from boulderopaltoolkits.namespace import Namespace
from boulderopaltoolkits.toolkit_utils import expose

# pylint: disable=unused-argument, missing-function-docstring

# Namespace.PULSES deprecated 2022/12/01


@expose(Namespace.PULSES)
def cosine_pulse(*args, **kwargs):
    pass


@expose(Namespace.PULSES)
def gaussian_pulse(*args, **kwargs):
    pass


@expose(Namespace.PULSES)
def hann_series(*args, **kwargs):
    pass


@expose(Namespace.PULSES)
def linear_ramp(*args, **kwargs):
    pass


@expose(Namespace.PULSES)
def sech_pulse(*args, **kwargs):
    pass


@expose(Namespace.PULSES)
def sinusoid(*args, **kwargs):
    pass


@expose(Namespace.PULSES)
def square_pulse(*args, **kwargs):
    pass


@expose(Namespace.PULSES)
def tanh_ramp(*args, **kwargs):
    pass
