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
Utility functions for trapped ion systems.
"""
from __future__ import annotations

from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import (
    Any,
    Optional,
)

import numpy as np
from qctrlcommons.exceptions import QctrlArgumentsValueError
from qctrlcommons.graph import Graph
from qctrlcommons.node.node_data import Pwc
from qctrlcommons.preconditions import (
    check_argument,
    check_duration,
    check_numeric_numpy_array,
)

from boulderopaltoolkits.namespace import Namespace
from boulderopaltoolkits.toolkit_utils import (
    expose,
    extract_graph_output,
)
from boulderopaltoolkits.utils.nodes import (
    complex_optimizable_pwc_signal,
    real_optimizable_pwc_signal,
)


@expose(Namespace.IONS)
def obtain_ion_chain_properties(
    qctrl: Any,
    atomic_mass: float,
    ion_count: int,
    center_of_mass_frequencies: list,
    wave_numbers: list,
    laser_detuning: Optional[float] = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Obtain the Lamb–Dicke parameters and mode frequencies (or relative detunings
    if a laser detuning is provided) for an ion chain.

    This is essentially a wrapper of the Boulder Opal function
    :func:`~qctrl.dynamic.namespaces.FunctionNamespace.calculate_ion_chain_properties`,
    but returns the result as NumPy arrays.

    Parameters
    ----------
    qctrl : qctrl.Qctrl
        Boulder Opal session object.
    atomic_mass : float
        The atomic mass of the ions of the chain in atomic units.
        This function assumes that all the ions in the chain are from the same atomic species.
    ion_count : int
        The number of ions in the chain, :math:`N`.
    center_of_mass_frequencies : list
        A list of three positive numbers representing the center-of-mass trapping frequency
        in the order of radial x-direction, radial y-direction, and axial z-direction,
        which correspond to the unit vectors :math:`(1, 0, 0)`, :math:`(0, 1, 0)`,
        and :math:`(0, 0, 1)` respectively.
    wave_numbers : list
        A list of three elements representing the the laser difference angular wave vector
        (in units of rad/m) in the order of radial x-direction, radial y-direction, and
        the axial z-direction, which correspond to the unit vectors :math:`(1, 0, 0)`,
        :math:`(0, 1, 0)`, and :math:`(0, 0, 1)` respectively.
    laser_detuning : float, optional
        The detuning of the control laser.
        If not provided, the returned relative detunings represent the mode frequencies.

    Returns
    -------
    np.ndarray
        A 3D array of shape ``(3, N, N)`` representing the Lamb–Dicke parameters of the ions.
        Its dimensions indicate, respectively, the direction (radial x-direction,
        radial y-direction, and axial z-direction), the collective mode, and the ion.
    np.ndarray
        A 2D array of shape ``(3, N)`` representing the mode frequencies
        (or relative detunings if a laser detuning is provided).
        Its dimensions indicate, respectively, the direction (radial x-direction,
        radial y-direction, and axial z-direction) and the collective mode.

    See Also
    --------
    :func:`~qctrl.dynamic.namespaces.FunctionNamespace.calculate_ion_chain_properties` :
        Function to calculate the properties of an ion chain.
    :func:`.ions.ms_optimize` :
        Find optimal pulses to perform Mølmer–Sørensen-type operations on trapped ions systems.
    :func:`.ions.ms_simulate` :
        Simulate a Mølmer–Sørensen-type operation on a trapped ions system.

    Examples
    --------
    Refer to the `How to optimize error-robust Mølmer–Sørensen gates for trapped ions
    <https://docs.q-ctrl.com/boulder-opal/user-guides/how-to-optimize-error-robust
    -molmer-sorensen-gates-for-trapped-ions>`_ user guide to find how to use this function.
    """

    check_argument(
        isinstance(ion_count, (int, np.integer)) and ion_count >= 1,
        "The ion count must be an integer and greater than 0.",
        {"ion_count": ion_count},
    )
    check_argument(
        _is_positive(atomic_mass),
        "The atomic mass must be positive.",
        {"atomic_mass": atomic_mass},
    )
    check_argument(
        len(center_of_mass_frequencies) == 3,
        "The center_of_mass_frequencies list must have three elements, representing the frequency "
        "in the order of radial x-direction, radial y-direction, and the axial z-direction.",
        {"center_of_mass_frequencies": center_of_mass_frequencies},
    )
    check_argument(
        _is_positive(np.asarray(center_of_mass_frequencies)),
        "All center of mass frequencies must be positive.",
        {"center_of_mass_frequencies": center_of_mass_frequencies},
    )
    check_argument(
        len(wave_numbers) == 3,
        "The wave_numbers list must have three elements, representing the wave vector "
        "in the order of radial x-direction, radial y-direction, and the axial z-direction.",
        {"wave_numbers": wave_numbers},
    )
    check_argument(
        not np.allclose(wave_numbers, 0),
        "At least one of the wave numbers must be non-zero.",
        {"wave_numbers": wave_numbers},
    )

    ion_chain_properties = qctrl.functions.calculate_ion_chain_properties(
        atomic_mass=float(atomic_mass),
        ion_count=int(ion_count),
        radial_x_center_of_mass_frequency=float(center_of_mass_frequencies[0]),
        radial_y_center_of_mass_frequency=float(center_of_mass_frequencies[1]),
        axial_center_of_mass_frequency=float(center_of_mass_frequencies[2]),
        radial_x_wave_number=float(wave_numbers[0]),
        radial_y_wave_number=float(wave_numbers[1]),
        axial_wave_number=float(wave_numbers[2]),
    )

    # The first axis of lamb_dicke_parameters and detuning are directions (x, y, z).
    lamb_dicke_parameters = []
    frequencies = []

    for properties_per_direction in [
        ion_chain_properties.radial_x_mode_properties,
        ion_chain_properties.radial_y_mode_properties,
        ion_chain_properties.axial_mode_properties,
    ]:

        lamb_dicke_parameters.append(
            [p.lamb_dicke_parameters for p in properties_per_direction]
        )
        frequencies.append([p.frequency for p in properties_per_direction])

    if laser_detuning is None:
        return np.asarray(lamb_dicke_parameters), np.asarray(frequencies)

    return np.asarray(lamb_dicke_parameters), np.asarray(frequencies) - laser_detuning


def _is_positive(x: float | np.ndarray | int):
    """
    Check the value must be greater than zero, taking into account rounding errors.
    """
    return not np.any(np.isclose(x, 0)) and np.all(x > 0)


def _complex_symmetrized_drive(graph, segment_count, duration, maximum, name):
    """
    Create a symmetrized drive signal (Milne et al., Phys. Rev. Applied, 2020).
    """

    free_segment_count = (segment_count + 1) // 2

    moduli = graph.optimization_variable(
        count=free_segment_count, lower_bound=0, upper_bound=maximum
    )
    phases = graph.optimization_variable(
        count=free_segment_count,
        lower_bound=0,
        upper_bound=2 * np.pi,
        is_lower_unbounded=True,
        is_upper_unbounded=True,
    )

    if segment_count % 2 == 0:
        moduli_reversed = graph.reverse(moduli, [0])
        phases_reversed = graph.reverse(phases, [0])

    else:
        moduli_reversed = graph.reverse(moduli[:-1], [0])
        phases_reversed = graph.reverse(phases[:-1], [0])

    moduli_comb = graph.concatenate([moduli, moduli_reversed], 0)
    phases_comb = graph.concatenate([phases, 2 * phases[-1] - phases_reversed], 0)

    return graph.complex_pwc_signal(
        moduli=moduli_comb, phases=phases_comb, duration=duration, name=name
    )


def _real_symmetrized_drive(graph, segment_count, duration, minimum, maximum, name):
    """
    Create a symmetrized drive signal (Milne et al., Phys. Rev. Applied, 2020).
    """

    free_segment_count = (segment_count + 1) // 2

    values = graph.optimization_variable(
        count=free_segment_count, lower_bound=minimum, upper_bound=maximum
    )
    if segment_count % 2 == 0:
        values_reversed = graph.reverse(values, [0])

    else:
        values_reversed = graph.reverse(values[:-1], [0])

    return graph.pwc_signal(
        values=graph.concatenate([values, values_reversed], 0),
        duration=duration,
        name=name,
    )


def _validate_addressing(addressing):
    """
    Validate an addressing input and return it as a tuple.
    """
    message = "The ions addressed must be an integer or a tuple of integers."
    try:
        check_argument(
            all(isinstance(ion, (int, np.integer)) for ion in addressing),
            message,
            {"addressing": addressing},
        )

    except TypeError as error:

        if isinstance(addressing, (int, np.integer)):
            return (addressing,)

        raise QctrlArgumentsValueError(message, {"addressing": addressing}) from error

    addressing = tuple(int(k) for k in addressing)
    check_argument(
        len(addressing) == len(set(addressing)),
        "The ions addressed must be unique.",
        {"addressing": addressing},
    )
    return addressing


@expose(Namespace.IONS)
@dataclass
class Drive:
    """
    A piecewise-constant complex-valued drive.

    Parameters
    ----------
    values : np.ndarray
        The values of the drive at each segment, in units of rad/s.
    addressing : int or tuple[int, ...]
        The indices of the ions addressed by the drive.

    See Also
    --------
    :class:`.ions.OptimizableDrive` :
        Abstract class describing a piecewise-constant optimizable drive.
    :func:`.ions.ms_simulate` :
        Simulate a Mølmer–Sørensen-type operation on a trapped ions system.
    """

    values: np.ndarray
    addressing: int | tuple[int, ...]

    def __post_init__(self):
        check_numeric_numpy_array(self.values, "values")
        self.addressing = _validate_addressing(self.addressing)

    def get_pwc(self, graph: Graph, duration: float) -> Pwc:
        """
        Return a Pwc representation of the drive.
        """
        return graph.pwc_signal(values=self.values, duration=duration)


@expose(Namespace.IONS)
class OptimizableDrive(ABC):
    """
    Abstract class for optimizable drives. You need to call the concrete classes below
    to create optimizable drives.

    See Also
    --------
    :class:`.ions.ComplexOptimizableDrive` :
        Class describing a piecewise-constant complex-valued optimizable drive.
    :class:`.ions.RealOptimizableDrive` :
        Class describing a piecewise-constant real-valued optimizable drive.
    :func:`.ions.ms_optimize` :
       Find optimal pulses to perform Mølmer–Sørensen-type operations on trapped ions systems.
    """

    name: str
    addressing: int | tuple[int, ...]

    @abstractmethod
    def get_pwc(self, graph: Graph, duration: float, robust: bool) -> Pwc:
        """
        Return a Pwc representation of the optimizable drive.
        """
        raise NotImplementedError


@expose(Namespace.IONS)
@dataclass
class ComplexOptimizableDrive(OptimizableDrive):
    """
    A piecewise-constant complex-valued optimizable drive.
    The main function will try to find the optimal values for it.

    Parameters
    ----------
    count : int
        The number of segments in the piecewise-constant drive.
    maximum_rabi_rate : float
        The maximum value that the modulus of the drive can take at each segment,
        in units of rad/s.
    addressing : int or tuple[int, ...]
        The indices of the ions addressed by the drive.
    name : str, optional
        The identifier of the drive.
        Defaults to "drive".

    See Also
    --------
    :class:`.ions.Drive` :
        Class describing non-optimizable drives.
    :class:`.ions.RealOptimizableDrive` :
        Class describing optimizable real-valued drives.
    :func:`.ions.ms_optimize` :
        Find optimal pulses to perform Mølmer–Sørensen-type operations on trapped ions systems.
    """

    count: int
    maximum_rabi_rate: float
    addressing: int | tuple[int, ...]
    name: str = "drive"

    def __post_init__(self):
        check_argument(
            self.count > 0, "There must be at least one segment.", {"count": self.count}
        )
        self.addressing = _validate_addressing(self.addressing)

    def get_pwc(self, graph: Graph, duration: float, robust: bool) -> Pwc:

        if robust:
            return _complex_symmetrized_drive(
                graph=graph,
                segment_count=self.count,
                duration=duration,
                maximum=self.maximum_rabi_rate,
                name=self.name,
            )

        return complex_optimizable_pwc_signal(
            graph=graph,
            segment_count=self.count,
            duration=duration,
            maximum=self.maximum_rabi_rate,
            name=self.name,
        )


@expose(Namespace.IONS)
@dataclass
class RealOptimizableDrive(OptimizableDrive):
    """
    A piecewise-constant real-valued optimizable drive.
    The main function will try to find the optimal values for it.

    Parameters
    ----------
    count : int
        The number of segments in the piecewise-constant drive.
    minimum_rabi_rate : float
        The minimum value that the drive can take at each segment, in units of rad/s.
    maximum_rabi_rate : float
        The maximum value that the drive can take at each segment, in units of rad/s.
    addressing : int or tuple[int, ...]
        The indices of the ions addressed by the drive.
    name : str, optional
        The identifier of the drive.
        Defaults to "drive".

    See Also
    --------
    :class:`.ions.ComplexOptimizableDrive` :
        Class describing optimizable complex-valued drives.
    :class:`.ions.Drive` :
        Class describing non-optimizable drives.
    :func:`.ions.ms_optimize` :
        Find optimal pulses to perform Mølmer–Sørensen-type operations on trapped ions systems.
    """

    count: int
    minimum_rabi_rate: float
    maximum_rabi_rate: float
    addressing: int | tuple[int, ...]
    name: str = "drive"

    def __post_init__(self):
        check_argument(
            self.count > 0, "There must be at least one segment.", {"count": self.count}
        )
        check_argument(
            self.minimum_rabi_rate < self.maximum_rabi_rate,
            "The maximum Rabi rate must be larger than the minimum.",
            {
                "minimum_rabi_rate": self.minimum_rabi_rate,
                "maximum_rabi_rate": self.maximum_rabi_rate,
            },
        )
        self.addressing = _validate_addressing(self.addressing)

    def get_pwc(self, graph: Graph, duration: float, robust: bool) -> Pwc:

        if robust:
            return _real_symmetrized_drive(
                graph=graph,
                segment_count=self.count,
                duration=duration,
                minimum=self.minimum_rabi_rate,
                maximum=self.maximum_rabi_rate,
                name=self.name,
            )

        return real_optimizable_pwc_signal(
            graph=graph,
            segment_count=self.count,
            duration=duration,
            maximum=self.maximum_rabi_rate,
            minimum=self.minimum_rabi_rate,
            name=self.name,
        )


def _validate_system_parameters(
    lamb_dicke_parameters: np.ndarray,
    relative_detunings: np.ndarray,
    target_phases: Optional[np.ndarray],
) -> int:
    """
    Validate the arrays describing an ion system
    and return the number of ions.
    """

    ion_count = lamb_dicke_parameters.shape[-1]

    check_argument(
        lamb_dicke_parameters.shape == (3, ion_count, ion_count)
        and relative_detunings.shape == (3, ion_count),
        "The shape of the Lamb–Dicke parameters array must be (3, N, N), "
        "and the shape of the relative detunings array must be (3, N), "
        "where N is the number of ions.",
        {
            "lamb_dicke_parameters": lamb_dicke_parameters,
            "relative_detunings": relative_detunings,
        },
        extras={
            "lamb_dicke_parameters.shape": lamb_dicke_parameters.shape,
            "relative_detunings.shape": relative_detunings.shape,
        },
    )

    if target_phases is not None:
        check_argument(
            target_phases.shape == (ion_count, ion_count),
            "The shape of the target phases array must be (N, N), "
            "where N is the number of ions.",
            {"target_phases": target_phases},
            extras={"ion count": ion_count, "target_phases.shape": target_phases.shape},
        )

    return ion_count


def _check_drives_addressing(drives, ion_count):
    """
    Check the input drives are a list and that the ions they address are valid.
    """

    check_argument(
        isinstance(drives, list),
        "You must provide a list of drives.",
        {"drives": drives},
    )

    all_addressing = []
    for idx, drive in enumerate(drives):
        check_argument(
            all(0 <= ion < ion_count for ion in drive.addressing),
            "The addressed ions must be between 0 (inclusive) "
            "and the number of ions (exclusive).",
            {"drives": drives},
            extras={
                f"drives[{idx}].addressing": drive.addressing,
                "ion count": ion_count,
            },
        )
        all_addressing += drive.addressing

    check_argument(
        len(all_addressing) == len(set(all_addressing)),
        "Each ion can only be addressed by a single drive.",
        {"drives": drives},
    )


def _get_ion_drives(pwc_addressings, ion_count, graph, duration):
    """
    From a list of (Pwc, list(int)) tuples (drives and ions addressed by them),
    return a list of length ion_count the drive addressing each ion
    or a PWC with value 0 if the ion is not addressed by any drive.
    """
    ion_drives = []
    for idx in range(ion_count):
        for pwc, addressing in pwc_addressings:
            # Add the first drive that addresses the ion as we assume
            # each ion can only be addressed by a single drive.
            if idx in addressing:
                ion_drives.append(pwc)
                break
        else:
            ion_drives.append(graph.constant_pwc(constant=0.0, duration=duration))

    return ion_drives


_MS_NODE_NAMES = ["phases", "displacements", "infidelities"]


@expose(Namespace.IONS)
def ms_simulate(
    qctrl: Any,
    drives: list[Drive],
    lamb_dicke_parameters: np.ndarray,
    relative_detunings: np.ndarray,
    duration: float,
    target_phases: Optional[np.ndarray] = None,
    sample_count: int = 128,
):
    r"""
    Simulate a Mølmer–Sørensen-type operation on a system composed of ions.

    Parameters
    ----------
    qctrl : qctrl.Qctrl
        Boulder Opal session object.
    drives : list[~ions.Drive]
        A list of drives addressing the ions.
        Each ion can only be addressed by a single drive,
        but there may be ions not addressed by any drive.
    lamb_dicke_parameters : np.ndarray
        A 3D array of shape ``(3, N, N)``, where :math:`N` is the number of
        ions in the system, specifying the laser-ion coupling strength,
        :math:`\{\eta_{jkl}\}`. The three dimensions indicate, respectively,
        the axis, the collective mode number, and the ion.
    relative_detunings : np.ndarray
        A 2D array of shape ``(3, N)`` specifying the difference, in Hz, between
        each motional mode frequency and the laser detuning
        (with respect to the qubit transition frequency :math:`\omega_0`),
        :math:`\{\delta_{jk} = \nu_{jk} - \delta\}`. The two dimensions indicate,
        respectively, the axis and the collective mode number.
    duration : float
        The duration, in seconds, of the dynamics to be simulated, :math:`T`.
        It must be greater than zero.
    target_phases : np.ndarray, optional
        A 2D array of shape ``(N, N)`` with the target relative phases between
        ion pairs, :math:`\{\Psi_{kl}\}`, as a strictly lower triangular matrix.
        Its :math:`(k, l)`-th element indicates the total relative phase target
        for ions :math:`k` and :math:`l`, with :math:`k > l`.
        If not provided, the function does not return the operational infidelities.
    sample_count : int, optional
        The number of times :math:`T` between 0 and `duration` (included)
        at which the evolution is sampled.
        Defaults to 128.

    Returns
    -------
    dict
        A dictionary containing information about the evolution of the system.
        The dictionary keys are:

            ``sample_times``
                The times at which the evolution is sampled, as an array of shape ``(T,)``.
            ``phases``
                Acquired phases :math:`\{\Phi_{jk}(t_i) = \phi_{jk}(t_i) + \phi_{kj}(t_i)\}`
                for each sample time and for all ion pairs, as a strictly lower triangular
                matrix of shape ``(T, N, N)``.
                :math:`\Phi_{jk}` records the relative phase between ions :math:`j`
                and :math:`k`; matrix elements where :math:`j \leq k` are zero.
            ``displacements``
                Displacements :math:`\{\eta_{pj}\alpha_{pj}(t_i)\}` for all mode-ion
                combinations, as an array of shape ``(T, 3, N, N)``.
                The four dimensions indicate the sample time, the axis,
                the collective mode number, and the ion.
            ``infidelities``
                A 1D array of length ``T`` representing the operational infidelities of
                the Mølmer–Sørensen gate at each sample time, :math:`\mathcal{I}(t_i)`.
                Only returned if target relative phases are provided.

    See Also
    --------
    :class:`.ions.Drive` :
        Class describing non-optimizable drives.
    :func:`.ions.ms_optimize` :
        Find optimal pulses to perform Mølmer–Sørensen-type operations on trapped ions systems.
    :func:`.ions.obtain_ion_chain_properties` :
        Calculate the properties of an ion chain.

    Notes
    -----
    The internal and motional Hamiltonian of :math:`N` ions is

    .. math::
        H_0 = \sum_{p = 1}^{3N} \hbar\nu_p \left(a_p^\dagger a_p + \frac{1}{2}\right)
            + \sum_{j = 1}^N \frac{\hbar \omega_0}{2} \sigma_{z,j} ,

    where the axis dimension and collective mode dimension are combined into a single index
    :math:`p` for simplicity, :math:`a_p` is the annihilation operator for the mode :math:`p`,
    and :math:`\sigma_{z,j}` is the Pauli :math:`Z` operator for the ion :math:`j`.
    The interaction Hamiltonian for Mølmer–Sørensen-type
    operations in the rotating frame with respect to :math:`H_0` is:

    .. math::
        H_I(t) = i\hbar\sum_{j = 1}^N \sigma_{x, j} \sum_{p = 1}^{3N} (-\beta_{pj}^*(t)a_p +
                \beta_{pj}(t) a_p^\dagger) ,

    where :math:`\sigma_{x, j}` is the Pauli :math:`X` operator for the ion :math:`j` and
    :math:`\beta_{pj}(t) = \eta_{pj} \frac{\gamma_j(t)}{2} e^{i\delta_p t}`,
    indicating the coupling of the ion :math:`j` to the motional mode :math:`p`,
    where :math:`\{\gamma_j\}` is the total drive acting on ion :math:`j`.

    The corresponding unitary operation is given by [1]_

    .. math::
        U(t) = \exp\left[ \sum_{j=1}^N \sigma_{x, j} B_j(t)
                + i\sum_{j=1}^N\sum_{k=1}^{j - 1} (\phi_{jk}(t) + \phi_{kj}(t))
                \sigma_{x, j} \sigma_{x, k} \right] ,

    where

    .. math::
        B_j(t) &\equiv \sum_{p = 1}^{3N}  \left(\eta_{pj}\alpha_{pj}(t)a_p^\dagger
            - \eta_{pj}^{\ast}\alpha_{pj}^\ast(t)a_p \right) ,

        \phi_{jk}(t) &\equiv \mathrm{Im} \left[ \sum_{p=1}^{3N} \int_{0}^{t} d \tau_1
            \int_{0}^{\tau_1} d \tau_2 \beta_{pj}(\tau_1)\beta_{pk}^{\ast}(\tau_2) \right] ,

    and

    .. math::
        \alpha_{pj}(t) = \int_0^t d\tau \frac{\gamma_j(\tau)}{2} e^{i \delta_p \tau} .

    The operational infidelity of the Mølmer–Sørensen gate is defined as [1]_:

    .. math::
        \mathcal{I} = 1 - \left| \left( \prod_{\substack{k=1 \\ l<k}}^N \cos (
            \phi_{kl} - \psi_{kl}) \right)
            \left( 1 - \sum_{j=1}^3 \sum_{k,l=1}^N \left[ |\eta_{jkl}|^2
            |\alpha_{jkl}|^2 \left(\bar{n}_{jk}+\frac{1}{2} \right) \right] \right) \right|^2 .

    References
    ----------
    .. [1] `C. D. B. Bentley, H. Ball, M. J. Biercuk, A. R. R. Carvalho,
            M. R. Hush, and H. J. Slatyer, Advanced Quantum Technologies 3, 2000044 (2020).
            <https://doi.org/10.1002/qute.202000044>`_
    """

    ion_count = _validate_system_parameters(
        lamb_dicke_parameters, relative_detunings, target_phases
    )

    check_duration(duration, "duration")

    check_argument(
        all(isinstance(drive, Drive) for drive in drives),
        "All drives must be non-optimizable.",
        {"drives": drives},
    )

    sample_times = np.linspace(0.0, duration, sample_count)

    graph = qctrl.create_graph()

    _check_drives_addressing(drives, ion_count)

    drive_pwcs = [
        (drive.get_pwc(graph, duration), drive.addressing) for drive in drives
    ]
    ion_drives = _get_ion_drives(drive_pwcs, ion_count, graph, duration)

    phases = graph.ms_phases(
        drives=ion_drives,
        lamb_dicke_parameters=lamb_dicke_parameters,
        relative_detunings=relative_detunings,
        sample_times=sample_times,
        name=_MS_NODE_NAMES[0],
    )

    displacements = graph.ms_displacements(
        drives=ion_drives,
        lamb_dicke_parameters=lamb_dicke_parameters,
        relative_detunings=relative_detunings,
        sample_times=sample_times,
        name=_MS_NODE_NAMES[1],
    )

    if target_phases is not None:
        graph.ms_infidelity(
            phases=phases,
            displacements=displacements,
            target_phases=target_phases,
            name=_MS_NODE_NAMES[2],
        )
        output_node_names = _MS_NODE_NAMES
    else:
        output_node_names = _MS_NODE_NAMES[:2]

    simulation_result = qctrl.functions.calculate_graph(
        graph=graph, output_node_names=output_node_names
    )

    # Retrieve results and build output dictionary.
    result_dict: dict[str, Any] = {"sample_times": sample_times}

    for key, value in simulation_result.output.items():
        result_dict[key] = extract_graph_output(value)

    return result_dict


@expose(Namespace.IONS)
def ms_optimize(
    qctrl: Any,
    drives: list[OptimizableDrive],
    lamb_dicke_parameters: np.ndarray,
    relative_detunings: np.ndarray,
    duration: float,
    target_phases: np.ndarray,
    sample_count: int = 128,
    robust: bool = False,
    optimization_count: int = 5,
    max_iteration_count: Optional[int] = None,
    cost_history: Optional[str] = None,
):
    r"""
    Find optimal pulses to perform a target Mølmer–Sørensen-type operation
    on a system composed of ions.

    Parameters
    ----------
    qctrl : qctrl.Qctrl
        Boulder Opal session object.
    drives : list[OptimizableDrive]
        A list of optimizable drives addressing the ions.
        Each ion can only be addressed by a single drive,
        but there may be ions not addressed by any drive.
    lamb_dicke_parameters : np.ndarray
        A 3D array of shape ``(3, N, N)``, where :math:`N` is the number of
        ions in the system, specifying the laser-ion coupling strength,
        :math:`\{\eta_{jkl}\}`. The three dimensions indicate, respectively,
        the axis, the collective mode number, and the ion.
    relative_detunings : np.ndarray
        A 2D array of shape ``(3, N)`` specifying the difference, in Hz, between
        each motional mode frequency and the laser detuning
        (with respect to the qubit transition frequency :math:`\omega_0`),
        :math:`\{\delta_{jk} = \nu_{jk} - \delta\}`. The two dimensions indicate,
        respectively, the axis and the collective mode number.
    duration : float
        The duration, in seconds, of the dynamics to be optimized, :math:`T`.
        It must be greater than zero.
    target_phases : np.ndarray
        A 2D array of shape ``(N, N)`` with the target relative phases between
        ion pairs, :math:`\{\Psi_{kl}\}`, as a strictly lower triangular matrix.
        Its :math:`(k, l)`-th element indicates the total relative phase target
        for ions :math:`k` and :math:`l`, with :math:`k > l`.
    sample_count : int, optional
        The number of times :math:`T` between 0 and `duration` (included)
        at which the evolution is sampled.
        Defaults to 128.
    robust : bool, optional
        Whether to obtain optimized drives robust against dephasing noise.
    optimization_count : int, optional
        The number of independent randomly seeded optimizations to perform. The result
        from the best optimization (the one with the lowest cost) is returned.
        Defaults to 5.
    max_iteration_count : int, optional
        The maximum number of optimizer iterations to perform.
        You can set this as an early stop condition for the optimizer.
        If provided, it must be greater than zero.
        Defaults to None, which means that the optimizer runs until it converges.
    cost_history : str, optional
        String determining the output of the optimization cost history.
        If "BEST", a single cost history for the best performing optimization is returned.
        If "ALL", a list with the cost histories for all optimizations is returned.
        Defaults to None, in which case no cost history is returned.

    Returns
    -------
    dict
        A dictionary containing information about the evolution of the system.
        The dictionary keys are:

            ``optimized_values``
                Dictionary containing the optimized drives values, whose keys
                are the names of the drives provided to the function, and whose
                values are an np.ndarray with the values of the piecewise-constant signal.
            ``cost``
                The final optimized cost. If `robust` is set to False, this corresponds to
                the infidelity at the end of the gate. If `robust` is set to True, it is
                the final infidelity plus the dephasing-robust cost term.
            ``sample_times``
                The times at which the evolution is sampled, as an array of shape ``(T,)``.
            ``phases``
                Acquired phases :math:`\{\Phi_{jk}(t_i) = \phi_{jk}(t_i) + \phi_{kj}(t_i)\}`
                for each sample time and for all ion pairs, as a strictly lower triangular
                matrix of shape ``(T, N, N)``.
                :math:`\Phi_{jk}` records the relative phase between ions :math:`j`
                and :math:`k`; matrix elements where :math:`j \leq k` are zero.
            ``displacements``
                Displacements :math:`\{\eta_{pj}\alpha_{pj}(t_i)\}` for all mode-ion
                combinations, as an array of shape ``(T, 3, N, N)``.
                The four dimensions indicate the sample time, the axis,
                the collective mode number, and the ion.
            ``infidelities``
                A 1D array of length ``T`` representing the operational infidelities of
                the Mølmer–Sørensen gate at each sample time, :math:`\mathcal{I}(t_i)`.
            ``cost_history``
                If `cost_history` is set to "BEST", the cost history for the best performing
                optimization. If `cost_history` is set to "ALL", a list of all the cost histories
                for each optimization.

    See Also
    --------
    :class:`.ions.ComplexOptimizableDrive` :
        Class describing a piecewise-constant complex-valued optimizable drive.
    :class:`.ions.RealOptimizableDrive` :
        Class describing a piecewise-constant real-valued optimizable drive.
    :func:`.ions.ms_simulate` :
        Simulate a Mølmer–Sørensen-type operation on a trapped ions system.
    :func:`.ions.obtain_ion_chain_properties` :
        Calculate the properties of an ion chain.

    Notes
    -----
    The internal and motional Hamiltonian of :math:`N` ions is

    .. math::
        H_0 = \sum_{p = 1}^{3N} \hbar\nu_p \left(a_p^\dagger a_p + \frac{1}{2}\right)
            + \sum_{j = 1}^N \frac{\hbar \omega_0}{2} \sigma_{z,j} ,

    where the axis dimension and collective mode dimension are combined into a single index
    :math:`p` for simplicity, :math:`a_p` is the annihilation operator for the mode :math:`p`,
    and :math:`\sigma_{z,j}` is the Pauli :math:`Z` operator for the ion :math:`j`.
    The interaction Hamiltonian for Mølmer–Sørensen-type
    operations in the rotating frame with respect to :math:`H_0` is:

    .. math::
        H_I(t) = i\hbar\sum_{j = 1}^N \sigma_{x, j} \sum_{p = 1}^{3N} (-\beta_{pj}^*(t)a_p +
                \beta_{pj}(t) a_p^\dagger) ,

    where :math:`\sigma_{x, j}` is the Pauli :math:`X` operator for the ion :math:`j` and
    :math:`\beta_{pj}(t) = \eta_{pj} \frac{\gamma_j(t)}{2} e^{i\delta_p t}`,
    indicating the coupling of the ion :math:`j` to the motional mode :math:`p`,
    where :math:`\{\gamma_j\}` is the total drive acting on ion :math:`j`.

    The corresponding unitary operation is given by [1]_

    .. math::
        U(t) = \exp\left[ \sum_{j=1}^N \sigma_{x, j} B_j(t)
                + i\sum_{j=1}^N\sum_{k=1}^{j - 1} (\phi_{jk}(t) + \phi_{kj}(t))
                \sigma_{x, j} \sigma_{x, k} \right] ,

    where

    .. math::
        B_j(t) &\equiv \sum_{p = 1}^{3N}  \left(\eta_{pj}\alpha_{pj}(t)a_p^\dagger
            - \eta_{pj}^{\ast}\alpha_{pj}^\ast(t)a_p \right) ,

        \phi_{jk}(t) &\equiv \mathrm{Im} \left[ \sum_{p=1}^{3N} \int_{0}^{t} d \tau_1
            \int_{0}^{\tau_1} d \tau_2 \beta_{pj}(\tau_1)\beta_{pk}^{\ast}(\tau_2) \right] ,

    and

    .. math::
        \alpha_{pj}(t) = \int_0^t d\tau \frac{\gamma_j(\tau)}{2} e^{i \delta_p \tau} .

    The operational infidelity of the Mølmer–Sørensen gate is defined as [1]_:

    .. math::
        \mathcal{I} = 1 - \left| \left( \prod_{\substack{k=1 \\ l<k}}^N \cos (
            \phi_{kl} - \psi_{kl}) \right)
            \left( 1 - \sum_{j=1}^3 \sum_{k,l=1}^N \left[ |\eta_{jkl}|^2
            |\alpha_{jkl}|^2 \left(\bar{n}_{jk}+\frac{1}{2} \right) \right] \right) \right|^2 .

    You can use the `robust` flag to construct a Mølmer–Sørensen gate that is
    robust against dephasing noise. This imposes a symmetry [1]_ in the optimizable
    ion drives and aims to minimize the time-averaged positions of the phase-space
    trajectories,

    .. math::
        \langle \alpha_{pj} \rangle
            = \frac{1}{t_\text{gate}} \int_0^{t_\text{gate}}
                \alpha_{pj}(t) \mathrm{d} t ,

    where the axis dimension and the collective mode dimension are combined
    into a single index :math:`p` for simplicity.

    This is achieved by adding an additional term to the cost function,
    consisting of the sum of the square moduli of the time-averaged positions
    multiplied by the corresponding Lamb–Dicke parameters. That is to say,

    .. math::
        C_\text{robust} =
            \mathcal{I} + \sum_{p,j}
                \left| \eta_{pj} \langle \alpha_{pj} \rangle \right|^2 .

    References
    ----------
    .. [1] `C. D. B. Bentley, H. Ball, M. J. Biercuk, A. R. R. Carvalho,
            M. R. Hush, and H. J. Slatyer, Advanced Quantum Technologies 3, 2000044 (2020).
            <https://doi.org/10.1002/qute.202000044>`_
    """

    if max_iteration_count is not None:
        check_argument(
            max_iteration_count > 0,
            "The maximum number of iterations must be positive.",
            {"max_iteration_count": max_iteration_count},
        )

    ion_count = _validate_system_parameters(
        lamb_dicke_parameters, relative_detunings, target_phases
    )

    check_duration(duration, "duration")

    _check_drives_addressing(drives, ion_count)

    check_argument(
        all(isinstance(drive, OptimizableDrive) for drive in drives),
        "All drives must be optimizable.",
        {"drives": drives},
    )

    sample_times = np.linspace(0.0, duration, sample_count)

    graph = qctrl.create_graph()

    drive_names = [drive.name for drive in drives]

    check_argument(
        len(drive_names) == len(set(drive_names)),
        "The drive names must be unique.",
        {"drives": drives},
        extras={"[drive.name for drive in drives]": drive_names},
    )

    if cost_history:
        check_argument(
            cost_history in ["ALL", "BEST"],
            "If passed, the cost history must be 'ALL' or 'BEST'.",
            {"cost_history": cost_history},
        )
        cost_history_scope = "ITERATION_VALUES"
    else:
        cost_history_scope = None

    drive_pwcs = [
        (drive.get_pwc(graph, duration, robust), drive.addressing) for drive in drives
    ]
    ion_drives = _get_ion_drives(drive_pwcs, ion_count, graph, duration)

    phases = graph.ms_phases(
        drives=ion_drives,
        lamb_dicke_parameters=lamb_dicke_parameters,
        relative_detunings=relative_detunings,
        sample_times=sample_times,
        name=_MS_NODE_NAMES[0],
    )

    displacements = graph.ms_displacements(
        drives=ion_drives,
        lamb_dicke_parameters=lamb_dicke_parameters,
        relative_detunings=relative_detunings,
        sample_times=sample_times,
        name=_MS_NODE_NAMES[1],
    )

    infidelities = graph.ms_infidelity(
        phases=phases,
        displacements=displacements,
        target_phases=target_phases,
        name=_MS_NODE_NAMES[2],
    )

    cost = infidelities[-1]
    if robust:
        cost += graph.ms_dephasing_robust_cost(
            drives=ion_drives,
            lamb_dicke_parameters=lamb_dicke_parameters,
            relative_detunings=relative_detunings,
        )

    optimization_result = qctrl.functions.calculate_optimization(
        graph=graph,
        optimization_count=optimization_count,
        cost_node_name=cost.name,
        output_node_names=drive_names + _MS_NODE_NAMES,
        max_iteration_count=max_iteration_count,
        cost_history_scope=cost_history_scope,
    )

    # Retrieve results and build output dictionary.
    result_dict: dict[str, Any] = {
        "optimized_values": {},
        "cost": optimization_result.cost,
        "sample_times": sample_times,
    }

    for key in drive_names:
        result_dict["optimized_values"][key] = extract_graph_output(
            optimization_result.output[key]
        )

    for key in _MS_NODE_NAMES:
        result_dict[key] = extract_graph_output(optimization_result.output[key])

    if cost_history == "ALL":
        result_dict["cost_history"] = optimization_result.cost_history.iteration_values
    elif cost_history == "BEST":
        result_dict["cost_history"] = min(
            optimization_result.cost_history.iteration_values, key=lambda hist: hist[-1]
        )

    return result_dict
