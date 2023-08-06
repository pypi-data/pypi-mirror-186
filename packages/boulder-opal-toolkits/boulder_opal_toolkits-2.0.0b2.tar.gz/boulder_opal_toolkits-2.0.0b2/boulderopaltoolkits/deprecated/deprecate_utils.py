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
Utilities for deprecating toolkit functionality.
"""

from functools import wraps

from qctrlcommons.exceptions import QctrlException


def deprecate_member(member, deprecated, replacement):
    """
    Replace a member (function or node) in a deprecated namespace
    with a function that raises an exception.
    If a replacement namespace is provided, a suggestion is also given.
    """
    message = f"The {deprecated.value.name} namespace has been deprecated."
    if replacement is not None:
        message += f" Please use the {replacement.value.name} namespace instead."

    @wraps(member)
    def wrapper(*args, **kwargs):  # pylint: disable=unused-argument
        wrapper.__doc__ = message
        raise QctrlException(message)

    return wrapper
