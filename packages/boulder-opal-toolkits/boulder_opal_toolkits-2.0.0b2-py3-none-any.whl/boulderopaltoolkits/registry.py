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
Registry for toolkits.
"""
from __future__ import annotations

import inspect
from dataclasses import dataclass
from functools import partial

import boulderopaltoolkits.closed_loop.functions
import boulderopaltoolkits.closed_loop.nodes
import boulderopaltoolkits.deprecated.functions
import boulderopaltoolkits.deprecated.nodes
import boulderopaltoolkits.ions.functions
import boulderopaltoolkits.signals.functions
import boulderopaltoolkits.signals.pwc_nodes
import boulderopaltoolkits.signals.stf_nodes
import boulderopaltoolkits.superconducting.functions
import boulderopaltoolkits.superconducting.nodes
import boulderopaltoolkits.utils.functions
import boulderopaltoolkits.utils.nodes
from boulderopaltoolkits.deprecated.deprecate_utils import deprecate_member
from boulderopaltoolkits.namespace import Namespace
from boulderopaltoolkits.toolkit_utils import TOOLKIT_ATTR

DEPRECATED_NAMESPACES = {Namespace.PULSES: Namespace.SIGNALS}


def _register(modules):
    """
    Collect exposed toolkits from modules.
    """
    registered = []
    for module in modules:
        for _, member in inspect.getmembers(
            module, predicate=partial(_filter, module_name=module.__name__)
        ):
            if hasattr(member, TOOLKIT_ATTR):
                namespace = getattr(member, TOOLKIT_ATTR)[0]
                if namespace in DEPRECATED_NAMESPACES:
                    member = deprecate_member(
                        member, namespace, DEPRECATED_NAMESPACES[namespace]
                    )
                registered.append(member)
    return registered


def _filter(member, module_name):
    """
    - Exposed member must either be a class or a function.
    - Exposed member must be defined in the module, not imported.
    - Exposed member must not be private.
    """
    return (
        (inspect.isfunction(member) or inspect.isclass(member))
        and member.__module__ == module_name
        and not member.__name__.startswith("_")
    )


NODES = _register(
    [
        boulderopaltoolkits.closed_loop.nodes,
        boulderopaltoolkits.deprecated.nodes,
        boulderopaltoolkits.signals.pwc_nodes,
        boulderopaltoolkits.signals.stf_nodes,
        boulderopaltoolkits.superconducting.nodes,
        boulderopaltoolkits.utils.nodes,
    ]
)
FUNCTIONS = _register(
    [
        boulderopaltoolkits.closed_loop.functions,
        boulderopaltoolkits.ions.functions,
        boulderopaltoolkits.deprecated.functions,
        boulderopaltoolkits.signals.functions,
        boulderopaltoolkits.superconducting.functions,
        boulderopaltoolkits.utils.functions,
    ]
)


def _get_empty_namespaces(exposed_items):
    """
    Collect a list with the names of the namespaces that are not in
    any of the exposed_items' TOOLKIT_ATTRs.
    """
    all_namespaces = set(Namespace)
    exposed_namespaces = set()
    for item in exposed_items:
        exposed_namespaces.update(set(getattr(item, TOOLKIT_ATTR)))

    left_namespaces = all_namespaces.difference(exposed_namespaces)
    return [item.get_name() for item in left_namespaces]


@dataclass
class _DocConfig:
    """
    Class to store information for building docs for the toolkits.

    Parameters
    ----------
    namespaces_without_functions: list[str]
        A list of names for namespaces that don't have functions.
    namespaces_without_nodes : list[str]
        A list of names for namespaces that don't have nodes.
    excluded_class_methods : list[str]
        A list of names for class methods that shouldn't be documented.
    deprecated_namespaces : list[Namespace]
        A list of deprecated namespaces.
    """

    namespaces_without_functions: list[str]
    namespaces_without_nodes: list[str]
    excluded_class_methods: list[str]
    deprecated_namespaces: list[Namespace]


TOOLKIT_DOC_CONFIG = _DocConfig(
    namespaces_without_functions=_get_empty_namespaces(FUNCTIONS),
    namespaces_without_nodes=_get_empty_namespaces(NODES),
    excluded_class_methods=["get_pwc", "create_optimizer"],
    deprecated_namespaces=list(DEPRECATED_NAMESPACES.keys()),
)
