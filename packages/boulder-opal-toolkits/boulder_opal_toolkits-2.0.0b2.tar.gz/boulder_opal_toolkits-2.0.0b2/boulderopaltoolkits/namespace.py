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
Namespaces for the toolkit functions, nodes, and classes.

These namespaces are categorized by physical system.
"""

from dataclasses import dataclass
from enum import Enum

TOOLKIT_MAIN_DOC = """
The Boulder Opal Toolkits provide convenience nodes, classes, and functions that can
simplify developing and deploying workflows in Boulder Opal.

The toolkits are built on top of the existing Boulder Opal functions_ and graph operations_, and
are designed for a particular physical system, or system-agnostic tasks. For example,
the superconducting toolkit contains functionalities to simulate and optimize superconducting
qubit systems, and the signal library provides various forms of commonly used control signals.

Each toolkit provides convenience functions, which can be accessed through its corresponding
namespace from the :py:obj:`~qctrl.Qctrl` object. For example, all functions in the utility toolkit
live in the namespace of `utils` of the :py:obj:`~qctrl.Qctrl` object. For ease of use,
some toolkits also define classes for creating abstractions for the physical system.
For example, the `Cavity` class in the superconducting toolkit. These classes also live
in the corresponding `superconducting` namespace of the :py:obj:`~qctrl.Qctrl` object.

Finally, toolkits may also host convenience graph nodes, which can be used together with other
nodes_ for defining a general computation graph for your task. These operations
live in the corresponding namespace of a :py:obj:`~qctrl.graphs.Graph` object.
For example, you can access the nodes for defining signals from the `signals` namespace of
a :py:obj:`~qctrl.graphs.Graph` object.

For more context on the role of toolkits and their usage in Boulder Opal, see the
`Boulder Opal Toolkits <https://docs.q-ctrl.com/boulder-opal/topics/boulder-opal-toolkits>`_ topic.


.. _functions: https://docs.q-ctrl.com/boulder-opal/references/qctrl/Functions.html
.. _operations: https://docs.q-ctrl.com/boulder-opal/references/qctrl/Graphs.html
.. _nodes: https://docs.q-ctrl.com/boulder-opal/references/qctrl/Graphs.html

Following is a list of toolkits in Boulder Opal:
"""

_CLOSED_LOOP_DOC = """
Toolkit for closed-loop optimizations.

For a quick introduction, see the `Find optimal pulses with automated optimization
<https://docs.q-ctrl.com/boulder-opal/tutorials/find-optimal-pulses-with-automated-optimization>`_
tutorial and the `How to automate closed-loop hardware optimization
<https://docs.q-ctrl.com/boulder-opal/user-guides/how-to-automate-closed-loop-hardware-optimization>`_
user guide.
"""

_IONS_DOC = """
Toolkit for trapped ion systems.
"""

_SIGNALS_DOC = """
Toolkit for signal library.

For a quick introduction, see the topic `Libraries of signals for Boulder Opal
<https://docs.q-ctrl.com/boulder-opal/topics/libraries-of-signals-for-boulder-opal>`_.
"""

_SUPERCONDUCTING_DOC = """
Toolkit for superconducting qubits.

For a quick introduction, see the `Simulate and optimize dynamics with the superconducting systems
toolkit <https://docs.q-ctrl.com/boulder-opal/tutorials/simulate-and-optimize-dynamics-
with-the-superconducting-systems-toolkit>`_ tutorial.
"""

_UTILS_DOC = """
Toolkit for system-agnostic functionality.
"""


@dataclass
class _NamespaceItem:
    """
    Store basic information about a namespace.
    """

    name: str
    doc: str
    title: str


class Namespace(Enum):
    """
    An enumeration of namespaces defined by physical systems.

    The `UTILS` namespace holds system-independent functionality.
    The `SIGNALS` namespace holds system-agnostic signals.
    """

    CLOSED_LOOP = _NamespaceItem(
        "closed_loop", _CLOSED_LOOP_DOC, "Closed-loop optimization"
    )
    IONS = _NamespaceItem("ions", _IONS_DOC, "Trapped ion systems")
    PULSES = _NamespaceItem("pulses", "", "")
    SIGNALS = _NamespaceItem("signals", _SIGNALS_DOC, "Signal library")
    SUPERCONDUCTING = _NamespaceItem(
        "superconducting", _SUPERCONDUCTING_DOC, "Superconducting systems"
    )
    UTILS = _NamespaceItem("utils", _UTILS_DOC, "General utilities")

    def get_name(self):
        """
        Get the name of the namespace.
        """
        return self.value.name

    def get_doc(self):
        """
        Get the doc of the namespace.
        """
        return self.value.doc

    def get_title(self):
        """
        Get the title of the doc page for toolkit.
        """
        if self.value.title is None:
            return f"{self.value.name.capitalize()} toolkit"

        return self.value.title
