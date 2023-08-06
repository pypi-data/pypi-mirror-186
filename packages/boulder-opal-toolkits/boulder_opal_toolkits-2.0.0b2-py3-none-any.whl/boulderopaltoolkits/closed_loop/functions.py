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
Utilities for the closed-loop optimizer.
"""

from __future__ import annotations

from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import (
    Any,
    Callable,
    Optional,
)

import numpy as np
from qctrlcommons.preconditions import (
    check_argument,
    check_argument_integer,
    check_argument_non_negative_scalar,
)

from boulderopaltoolkits.namespace import Namespace
from boulderopaltoolkits.toolkit_utils import expose


@expose(Namespace.CLOSED_LOOP)
class Optimizer(ABC):
    """
    Abstract class for optimizers used in closed-loop control.

    To create an optimizer, use one of the concrete classes in the closed-loop optimization
    toolkit. For example to create a cross entropy optimizer with an elite fraction of 0.1:
    `optimizer=qctrl.closed_loop.CrossEntropy(elite_fraction=0.1)`.

    See Also
    --------
    :class:`.closed_loop.Cmaes` :
        Class describing the covariance matrix adaptation evolution strategy (CMA-ES) optimizer.
    :class:`.closed_loop.CrossEntropy` :
        Class describing the cross entropy optimizer.
    :class:`.closed_loop.GaussianProcess` :
        Class describing the Gaussian-process-based optimizer.
    :class:`.closed_loop.NeuralNetwork` :
        Class describing the neural-network-based optimizer.
    :class:`.closed_loop.SimulatedAnnealing` :
        Class describing the simulated annealing optimizer.
    """

    method_name: str

    @abstractmethod
    def create_optimizer(self, qctrl, bounds):
        """
        Return the initialized optimizer.

        Parameters
        ----------
        qctrl : qctrl.Qctrl
            Boulder Opal session object.
        bounds : np.ndarray
            The per-parameter bounds on the test points.
            The bounds must be a NumPy array of shape ``(parameter count, 2)`` where the
            trailing axis are the bounds for each parameter (with the lower bound first, followed
            by the upper bound).
        """
        raise NotImplementedError


@expose(Namespace.CLOSED_LOOP)
@dataclass
class Cmaes(Optimizer):
    r"""
    The covariance matrix adaptation evolution strategy (CMA-ES) optimizer.

    Parameters
    ----------
    initial_mean : np.ndarray, optional
        The array of the initial means of the parameters for the multivariate normal
        distribution.
        Defaults to an array of ones.
    initial_step_size : float, optional
        The initial step size for the multivariate normal distribution from which new test
        points are sampled.
        Defaults to one.
    seed : int, optional
        Seed for the random number generator.
        Use this option to generate deterministic results from the optimizer.

    Notes
    -----
    The CMA-ES optimizer uses a multivariate normal distribution to generate new test points.
    The mean, step size, and covariance of this distribution are determined from their previous
    values and the current set of results.

    Note that this optimizer requires at least :math:`4 + \lfloor 3 \times \log N  \rfloor`
    test points each step, where :math:`N` is the number of optimizable parameters,
    :math:`\log` is the natural logarithm, and :math:`\lfloor x \rfloor` is the floor function.
    Otherwise, it will throw an error.

    For more detail on CMA-ES see `CMA-ES <https://en.wikipedia.org/wiki/CMA-ES>`_ on Wikipedia.
    """

    initial_mean: Optional[np.ndarray] = None
    initial_step_size: Optional[float] = None
    seed: Optional[int] = None
    method_name = "CMA-ES"

    def __post_init__(self):
        if self.initial_mean is not None:
            check_argument(
                isinstance(self.initial_mean, np.ndarray)
                and self.initial_mean.ndim == 1,
                "The initial mean must be a 1D np.ndarray.",
                {"initial_mean": self.initial_mean},
            )

        if self.seed is not None:
            check_argument_integer(self.seed, "seed")

    def create_optimizer(self, qctrl: Any, bounds: np.ndarray):
        _check_bounds(bounds)

        if self.initial_mean is not None:
            check_argument(
                len(self.initial_mean) == len(bounds),
                "The initial mean and the bounds must have the same length.",
                {"initial_mean": self.initial_mean, "bounds": bounds},
            )
            for mean_val, bound in zip(self.initial_mean, bounds):
                check_argument(
                    bound[0] <= mean_val <= bound[1],
                    "The initial mean must be within the bounds.",
                    {"initial_mean": self.initial_mean, "bounds": bounds},
                )

        def convert_to_list(array):
            if array is None:
                return None
            return array.tolist()

        initializer = qctrl.types.closed_loop_optimization_step.CmaesInitializer(
            bounds=_convert_bounds(qctrl, bounds),
            initial_mean=convert_to_list(self.initial_mean),
            initial_step_size=self.initial_step_size,
            seed=self.seed,
        )
        return qctrl.types.closed_loop_optimization_step.Optimizer(
            cmaes_initializer=initializer
        )


@expose(Namespace.CLOSED_LOOP)
@dataclass
class CrossEntropy(Optimizer):
    r"""
    The cross-entropy optimizer.

    Parameters
    ----------
    elite_fraction : float
        The top fraction of test points that the algorithm uses to generate the next distribution.
        Must be between 0 and 1.
    seed : int, optional
        Seed for the random number generator.
        Use this option to generate deterministic results from the optimizer.

    Notes
    -----
    The cross-entropy optimizer first fits a normal distribution to an `elite_fraction` of the given
    test points with the lowest cost function value. This normal distribution is then sampled to
    produce a new set of test points. Once all test points have converged, the optimization has
    converged and will no longer explore.

    Note that this optimizer requires at least
    :math:`\lceil 2 / \mathrm{elite}\_\mathrm{fraction} \rceil` results each step,
    to have at least 2 surviving elite points, and will throw an error if you don't provide enough
    `initial_test_parameters`.

    For best results, sample the initial test points from parameter space,
    varying each axis with each point. This optimizer will reject optimizations
    where all test points in the initial step are identical.

    For more detail on the cross-entropy optimizer see
    `cross-entropy method <https://en.wikipedia.org/wiki/Cross-entropy_method>`_ on Wikipedia.
    """

    elite_fraction: float
    seed: Optional[int] = None
    method_name = "cross entropy"

    def __post_init__(self):
        check_argument(
            0.0 < self.elite_fraction < 1.0,
            "The elite fraction must be between 0 and 1.",
            {"elite_fraction": self.elite_fraction},
        )

        if self.seed is not None:
            check_argument_integer(self.seed, "seed")

    def create_optimizer(self, qctrl: Any, bounds: np.ndarray):
        _check_bounds(bounds)

        initializer = qctrl.types.closed_loop_optimization_step.CrossEntropyInitializer(
            bounds=_convert_bounds(qctrl, bounds),
            elite_fraction=self.elite_fraction,
            seed=self.seed,
        )
        return qctrl.types.closed_loop_optimization_step.Optimizer(
            cross_entropy_initializer=initializer
        )


@expose(Namespace.CLOSED_LOOP)
@dataclass
class GaussianProcess(Optimizer):
    r"""
    The Gaussian process optimizer.

    Parameters
    ----------
    length_scale_bounds : np.ndarray, optional
        The per-parameter length scale bounds on the test points.
        The bounds must be a NumPy array of shape ``(parameter count, 2)`` where the trailing
        axis are the bounds for each parameter (with the lower bound first, followed by the upper
        bound).
        If not specified,  :py:obj:`~closed_loop.optimize` will pick a value derived from the
        `bounds` by picking orders of magnitudes below/above the sidelength for each box axis.
    seed : int, optional
        Seed for the random number generator.
        Use this option to generate deterministic results from the optimizer.

    Notes
    -----
    The Gaussian process is defined by the kernel

    .. math::
        k({\mathbf x}_j, {\mathbf x}_k)
            = \exp \left(-\frac{1}{2} ( {\mathbf x}_j - {\mathbf x}_k )^\top
                \Sigma^{-2} ( {\mathbf x}_j - {\mathbf x}_k )\right) ,

    where :math:`{\mathbf x}_j` is an :math:`n`-dimensional vector representing the
    :math:`j`-th test point, :math:`\Sigma= {\rm diag}(l_1, \cdots, l_n)`
    is an :math:`n \times n` diagonal matrix, and :math:`\{ l_j \}` are the length scales.
    The length scales are tuned while training the model, within the bounds set by the
    `length_scale_bounds` parameter. Roughly speaking, the amount a parameter needs to change
    to impact the optimization cost should lie within the length scale bounds.

    It's recommended to provide non-zero `cost_uncertainty` to :py:obj:`~closed_loop.optimize`
    when using this optimizer, otherwise you might encounter a numerical error when the optimizer
    tries to fit the kernel with your input data. If the error persists, try increasing the
    `cost_uncertainty` value or decreasing the minimum length scale bound. However, such numerical
    error is also an indication that your data might not be suitable to be modelled by a
    Gaussian process, and in that case, consider using a different closed-loop optimizer.

    For more detail on Gaussian processes see
    `Gaussian process <https://en.wikipedia.org/wiki/Gaussian_process>`_ on Wikipedia.
    """

    length_scale_bounds: Optional[np.ndarray] = None
    seed: Optional[int] = None
    method_name = "Gaussian process"

    def __post_init__(self):
        if self.length_scale_bounds is not None:
            _check_bounds(self.length_scale_bounds, "length scale bounds")

        if self.seed is not None:
            check_argument_integer(self.seed, "seed")

    def create_optimizer(self, qctrl: Any, bounds: np.ndarray):
        _check_bounds(bounds)

        if self.length_scale_bounds is not None:
            check_argument(
                len(self.length_scale_bounds) == len(bounds),
                "The length scale bounds and the bounds must have the same length.",
                {"length_scale_bounds": self.length_scale_bounds, "bounds": bounds},
            )

        initializer = (
            qctrl.types.closed_loop_optimization_step.GaussianProcessInitializer(
                bounds=_convert_bounds(qctrl, bounds),
                length_scale_bounds=_convert_bounds(qctrl, self.length_scale_bounds),
                seed=self.seed,
            )
        )
        return qctrl.types.closed_loop_optimization_step.Optimizer(
            gaussian_process_initializer=initializer
        )


@expose(Namespace.CLOSED_LOOP)
@dataclass
class NeuralNetwork(Optimizer):
    """
    The neural network optimizer.

    Parameters
    ----------
    seed : int, optional
        Seed for the random number generator.
        Use this option to generate deterministic results from the optimizer.

    Notes
    -----
    The neural network optimizer builds and trains a neural network to fit the cost landscape with
    the data it receives. Then a set of test points are returned, which minimize the neural
    network's fitted cost landscape. A gradient based optimizer is used to minimize this landscape,
    with the points starting from different random initial values.

    This method is recommended when you can provide a large amount of data about your system.

    The network architecture used by this optimizer is chosen for its good performance on a variety
    of quantum control tasks.

    For best results, you should pass an array of `initial_test_parameters` evenly sampled
    over the whole parameter space.
    """

    seed: Optional[int] = None
    method_name = "neural network"

    def __post_init__(self):
        if self.seed is not None:
            check_argument_integer(self.seed, "seed")

    def create_optimizer(self, qctrl: Any, bounds: np.ndarray):
        _check_bounds(bounds)

        initializer = (
            qctrl.types.closed_loop_optimization_step.NeuralNetworkInitializer(
                bounds=_convert_bounds(qctrl, bounds), seed=self.seed
            )
        )
        return qctrl.types.closed_loop_optimization_step.Optimizer(
            neural_network_initializer=initializer
        )


@expose(Namespace.CLOSED_LOOP)
@dataclass
class SimulatedAnnealing(Optimizer):
    r"""
    The simulated annealing optimizer.

    Parameters
    ----------
    temperatures : np.ndarray
        The array of initial per-parameter annealing temperatures :math:`T_0` used to generate
        new test points.
        Higher temperatures correspond to higher exploration.
        The per-parameter adjustments from the current test point are sampled from Cauchy
        distributions with scales given by temperatures.
        The temperatures are currently implemented to decay such that each temperature
        at the k-th step is set according to :math:`T_k=\frac{T_0}{1+k}`.
        All temperatures must be positive.
    temperature_cost : float
        The parameter for controlling the optimizer’s greediness.
        A high cost temperature allows the optimizer to explore test points which may not
        immediately improve the cost. A higher level of exploration can be helpful for
        more difficult optimization problems. The cost temperature is set to decay
        according to the same schedule as the temperatures.
        Must be positive.
    seed : int, optional
        Seed for the random number generator.
        Use this option to generate deterministic results from the optimizer.

    Notes
    -----
    This simulated annealing performs a temperature based random walk within the parameter `bounds`.
    The new test points are sampled from a distribution whose variance is given by the current
    `temperatures`. Higher `temperatures` translate to high levels of exploration, which can be
    useful for non-convex optimization. The `temperature_cost` parameter can be set independently of
    the `temperatures`, and controls the overall greediness of each update. A high
    `temperature_cost` allows the optimizer to accept updates which do not immediately improve the
    cost. Both `temperatures` and the `temperature_cost` automatically decay between iterations.

    For more information on this method see
    `simulated annealing <https://en.wikipedia.org/wiki/Simulated_annealing>`_ on Wikipedia.
    """

    temperatures: np.ndarray
    temperature_cost: float
    seed: Optional[int] = None
    method_name = "simulated annealing"

    def __post_init__(self):
        check_argument(
            all(self.temperatures > 0),
            "All parameter temperatures must be positive.",
            {"temperatures": self.temperatures},
        )

        check_argument(
            self.temperature_cost > 0,
            "The cost temperature must be positive.",
            {"temperature_cost": self.temperature_cost},
        )

        if self.seed is not None:
            check_argument_integer(self.seed, "seed")

    def create_optimizer(self, qctrl: Any, bounds: np.ndarray):
        _check_bounds(bounds)

        check_argument(
            len(self.temperatures) == len(bounds),
            "The temperatures and the bounds must have the same length.",
            {"temperatures": self.temperatures, "bounds": bounds},
        )

        initializer = (
            qctrl.types.closed_loop_optimization_step.SimulatedAnnealingInitializer(
                bounds=_convert_bounds(qctrl, bounds),
                temperatures=list(self.temperatures),
                temperature_cost=self.temperature_cost,
                seed=self.seed,
            )
        )
        return qctrl.types.closed_loop_optimization_step.Optimizer(
            simulated_annealing_initializer=initializer
        )


def _convert_bounds(qctrl, bounds):
    """
    Convert bounds to box constraints, if the bounds are passed as a NumPy array.
    If the bounds are not a NumPy array None is returned.
    """
    if isinstance(bounds, np.ndarray):
        return [
            qctrl.types.closed_loop_optimization_step.BoxConstraint(
                lower_bound=float(bound[0]), upper_bound=float(bound[1])
            )
            for bound in bounds
        ]
    return None


def _check_bounds(bounds: np.ndarray, name: str = "bounds"):
    """Check that the bounds are well-defined."""
    check_argument(
        isinstance(bounds, np.ndarray) and bounds.ndim == 2 and bounds.shape[1] == 2,
        f"The {name} must be a 2D np.ndarray with two components in the second axis.",
        {name: bounds},
    )
    check_argument(
        all(bounds[:, 1] > bounds[:, 0]),
        "The upper bound (second component) must be greater than the lower bound "
        f"(first component) for each element in the {name} array.",
        {name: bounds},
    )


@expose(Namespace.CLOSED_LOOP)
def optimize(
    qctrl: Any,
    cost_function: Callable,
    initial_test_parameters: np.ndarray,
    optimizer: Optimizer,
    bounds: np.ndarray,
    cost_uncertainty: Optional[float] = None,
    target_cost: Optional[float] = None,
    max_iteration_count: int = 100,
    callback: Optional[Callable] = None,
    verbose: bool = True,
) -> dict:
    """
    Run a closed-loop optimization to find a minimum of the given cost function.

    This is an iterative process, where the optimizer generates and tests a set of points.
    After several iterations the distribution of generated test points should converge
    to low values of the cost function. You can use this approach when your system is too
    complicated to model, or the computation of gradient is expensive or impossible.

    Parameters
    ----------
    qctrl : qctrl.Qctrl
        Boulder Opal session object.
    cost_function : Callable
        A function that takes the parameters as an argument and returns an array of costs values.
        The function should take a NumPy array of input parameters with shape
        ``(test point count, parameter count)`` and return the costs in a 1D array of length test
        point count.
    initial_test_parameters : np.ndarray
        The initial values of the parameters to use in the optimization.
        A 2D NumPy array of shape ``(test point count, parameter count)``.
    optimizer : ~closed_loop.Optimizer
        The optimizer to be used in the minimization of the cost function.
    bounds : np.ndarray
        The per-parameter bounds on the test points.
        The bounds must be a NumPy array of shape ``(parameter count, 2)`` where the trailing
        axis are the bounds for each parameter (with the lower bound first, followed by the upper
        bound).
    cost_uncertainty : float, optional
        The standard deviation in the value of the cost.
        Must be non-negative.
        Defaults to 0.
    target_cost : float, optional
        The target cost.
        If passed, the optimization will halt if the best cost is below the given value.
    max_iteration_count : int, optional
        The maximum number of iterations.
        Defaults to 100.
    callback : Callable, optional
        A function that takes in the current set of parameters, a 2D NumPy array of shape
        ``(test point count, parameter count)``, and returns a bool.
        The function is evaluated once during each iteration with the
        current parameters. If it returns True, the optimization is halted.
    verbose : bool, optional
        Whether to print out information about the optimization cycle.
        Defaults to True.

    Returns
    -------
    dict
        A dictionary containing the results of the optimization, namely, the best parameters
        `best_parameters`, their associated cost `best_cost`, and
        the history of best cost values `best_cost_history`.

    Notes
    -----
    If the optimization loop is halted via a `KeyboardInterrupt` then the function returns
    the best results obtained in the optimization thus far.
    """

    def verbose_print(message):
        if verbose:
            print(message)

    check_argument(
        isinstance(initial_test_parameters, np.ndarray)
        and np.ndim(initial_test_parameters) == 2,
        "The initial test parameters must be a 2D np.ndarray.",
        {"initial_test_parameters": initial_test_parameters},
    )

    check_argument(
        np.all(
            (initial_test_parameters >= bounds[:, 0])
            & (initial_test_parameters <= bounds[:, 1])
        ),
        "The initial test parameters must be within the bounds.",
        {"initial_test_parameters": initial_test_parameters, "bounds": bounds},
    )

    if cost_uncertainty is not None:
        check_argument_non_negative_scalar(cost_uncertainty, "cost uncertainty")

    verbose_print(
        f"""Running closed loop optimization
----------------------------------------
  Optimizer            : {optimizer.method_name}
  Number of test points: {initial_test_parameters.shape[0]}
  Number of parameters : {initial_test_parameters.shape[1]}
----------------------------------------
"""
    )

    closed_loop_optimizer = optimizer.create_optimizer(qctrl, bounds)

    test_parameters = initial_test_parameters

    # Obtain initial costs.
    verbose_print("Calling cost function…")
    costs = cost_function(test_parameters)

    check_argument(
        len(np.asarray(costs).shape) == 1
        and len(costs) == len(initial_test_parameters),
        "The cost function must return a 1D array of the length test point count.",
        {"initial_test_parameters": initial_test_parameters},
        extras={"cost_function(test_parameters)": costs},
    )

    best_cost_overall, best_parameters_overall = min(
        zip(costs, test_parameters), key=lambda params: params[0]
    )
    verbose_print(f"  Initial best cost: {best_cost_overall:.3f}")

    # Store the cost history.
    best_cost_history = [best_cost_overall]

    # Run the optimization loop until a halting condition is met.
    try:
        for iteration_count in range(max_iteration_count):
            # Organize the costs into the proper input format.
            results = [
                qctrl.types.closed_loop_optimization_step.CostFunctionResult(
                    parameters=parameters, cost=cost, cost_uncertainty=cost_uncertainty
                )
                for parameters, cost in zip(test_parameters, costs)
            ]

            # Call the automated closed-loop optimizer and obtain the next set of test points.
            verbose_print("\nRunning optimizer…")
            optimization_result = (
                qctrl.functions.calculate_closed_loop_optimization_step(
                    optimizer=closed_loop_optimizer,
                    results=results,
                    test_point_count=test_parameters.shape[0],
                )
            )

            # Retrieve the optimizer state and create a new optimizer object.
            closed_loop_optimizer = qctrl.types.closed_loop_optimization_step.Optimizer(
                state=optimization_result.state
            )

            # Organize the data returned by the automated closed-loop optimizer.
            test_parameters = np.array(
                [
                    test_point.parameters
                    for test_point in optimization_result.test_points
                ]
            )

            # Obtain costs.
            verbose_print("Calling cost function…")
            costs = cost_function(test_parameters)

            # Record the best results after this round.
            best_cost, best_parameters = min(
                zip(costs, test_parameters), key=lambda params: params[0]
            )

            # Compare last best results with best result overall.
            if best_cost < best_cost_overall:
                best_cost_overall = best_cost
                best_parameters_overall = best_parameters

            # Print the current best cost.
            verbose_print(
                f"  Best cost after {iteration_count+1} iterations: {best_cost_overall:.3f}"
            )

            # Store the current best cost.
            best_cost_history.append(best_cost_overall)

            if callback is not None:
                if callback(test_parameters):
                    verbose_print(
                        "\nCallback condition satisfied. Stopping the optimization."
                    )
                    break

            # Check if desired threshold has been achieved.
            if target_cost is not None:
                if best_cost_overall < target_cost:
                    verbose_print("\nTarget cost reached. Stopping the optimization.")
                    break
        else:
            verbose_print(
                "\nMaximum iteration count reached. Stopping the optimization."
            )

    except KeyboardInterrupt:
        # Exit the loop and return the current best results if a KeyboardInterrupt is caught.
        print("\nCalculation interrupted. Stopping the optimization.")

    return {
        "best_cost": best_cost_overall,
        "best_parameters": best_parameters_overall,
        "best_cost_history": best_cost_history,
    }
