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
Validator for core__calculateClosedLoopOptimizationStep mutation.
"""

import numpy as np

from qctrlcommons.exceptions import QctrlFieldError
from qctrlcommons.validation.base import BaseMutationInputValidator
from qctrlcommons.validation.messages import Messages


def _check_results_in_bounds(results, bounds):
    """
    Checks that the initial results are within the bounds.
    """
    results_array = np.array([result["parameters"] for result in results])
    bounds_array = np.array(
        [[bound["lowerBound"], bound["upperBound"]] for bound in bounds]
    )
    if not (
        (bounds_array[:, 0] <= results_array) & (results_array <= bounds_array[:, 1])
    ).all():
        raise QctrlFieldError(
            message="The initial results must be within the bounds.",
            fields=["bounds", "results"],
        )


def _check_cross_entropy_initializer(input_):
    """
    Checks input parameters for the cross entropy optimizer.
    """
    initializer = input_["optimizer"]["crossEntropyInitializer"]
    elite_fraction = initializer["eliteFraction"]

    _check_seed(initializer.get("seed", initializer.get("rngSeed")))

    if elite_fraction <= 0 or elite_fraction >= 1:
        raise QctrlFieldError(
            message="The elite_fraction has to be strictly between 0 and 1.",
            fields=["eliteFraction"],
        )

    results = input_.get("results")
    min_result_count = int(np.ceil(2 / elite_fraction))
    if results is None or len(results) < min_result_count:
        raise QctrlFieldError(
            message=Messages(
                field_name="results", minimum=min_result_count, items="items"
            ).min_items,
            fields=["results"],
        )

    bounds = initializer.get("bounds")
    if bounds is not None:
        parameter_count = len(results[0]["parameters"])
        _check_parameter_bounds(bounds, parameter_count)
        _check_results_in_bounds(results, bounds)


def _check_box_constraint(constraint, field):
    """
    Checks box constraint.
    """
    if constraint["upperBound"] <= constraint["lowerBound"]:
        raise QctrlFieldError(
            message="Ensure the upper bound is greater than the lower bound.",
            fields=[field],
        )


def _check_non_empty_initial_result(input_):
    """
    Checks whether initial results is empty.
    """
    if len(input_.get("results", [])) == 0:
        raise QctrlFieldError(
            message="Non empty `results` is required when initializing the optimizer.",
            fields=["optimizer", "results"],
        )


def _check_parameter_bounds(bounds, parameter_count):
    """
    Checks that
    1. bound must be set for each parameter,
    2. each bound must be valid.
    """
    if len(bounds) != parameter_count:
        raise QctrlFieldError(
            message="Bounds must be set for all parameters.",
            fields=["bounds", "results"],
        )
    for bound in bounds:
        _check_box_constraint(bound, "bounds")


def _check_gaussian_process_initializer(input_):
    """
    Checks input parameters for the Gaussian process based optimizer.
    """

    _check_non_empty_initial_result(input_)

    initializer = input_["optimizer"]["gaussianProcessInitializer"]
    bounds = initializer["bounds"]
    parameter_count = len(input_["results"][0]["parameters"])
    _check_parameter_bounds(bounds, parameter_count)
    _check_seed(initializer.get("seed", initializer.get("rngSeed")))

    length_scale_bounds = initializer.get("lengthScaleBounds")
    if length_scale_bounds is not None:
        if len(length_scale_bounds) != parameter_count:
            raise QctrlFieldError(
                message="Length scale bounds must be set for all parameters.",
                fields=["lengthScaleBounds", "results"],
            )
        for length_scale_bound in length_scale_bounds:
            _check_box_constraint(length_scale_bound, "lengthScaleBounds")
            if length_scale_bound["lowerBound"] <= 0:
                raise QctrlFieldError(
                    message=Messages(field_name="lowerBound", minimum=0).greater_than,
                    fields=["lowerBound"],
                )
    results = input_.get("results")
    _check_results_in_bounds(results, bounds)


def _check_simulated_annealing_initializer(input_):
    """
    Checks input parameters for the simulated annealing optimizer.
    """

    _check_non_empty_initial_result(input_)

    initializer = input_["optimizer"]["simulatedAnnealingInitializer"]
    bounds = initializer["bounds"]
    parameter_count = len(input_["results"][0]["parameters"])
    _check_parameter_bounds(bounds, parameter_count)
    _check_seed(initializer.get("seed", initializer.get("rngSeed")))

    temperatures = initializer["temperatures"]
    if len(temperatures) != parameter_count:
        raise QctrlFieldError(
            message="A temperature must be provided for each parameter.",
            fields=["temperatures", "results"],
        )
    if any(t <= 0 for t in temperatures):
        raise QctrlFieldError(
            message="All temperatures must be positive.", fields=["temperatures"]
        )

    temperature_cost = initializer["temperatureCost"]
    if temperature_cost <= 0:
        raise QctrlFieldError(
            message="The cost temperature must be positive.", fields=["temperatureCost"]
        )

    results = input_.get("results")
    _check_results_in_bounds(results, bounds)


def _check_neural_network_initializer(input_):
    """
    Checks input parameters for the neural-network-based optimizer.
    """
    _check_non_empty_initial_result(input_)

    initializer = input_["optimizer"]["neuralNetworkInitializer"]
    bounds = initializer["bounds"]
    parameter_count = len(input_["results"][0]["parameters"])

    _check_parameter_bounds(bounds, parameter_count)
    _check_seed(initializer.get("seed", initializer.get("rngSeed")))

    results = input_.get("results")
    _check_results_in_bounds(results, bounds)


def _check_cmaes_initializer(input_):
    """
    Checks input parameters for the CMA-ES optimizer.
    """
    initializer = input_["optimizer"]["cmaesInitializer"]
    bounds = initializer["bounds"]
    parameter_count = len(input_["results"][0]["parameters"])

    _check_parameter_bounds(bounds, parameter_count)
    _check_seed(initializer.get("seed", initializer.get("rngSeed")))

    initial_mean = initializer.get("initialMean")

    if initial_mean is not None:
        if len(initial_mean) != parameter_count:
            raise QctrlFieldError(
                message="The length of initial mean must be the same as the number of parameters.",
                fields=["initialMean"],
            )

        for mean_val, bound in zip(initial_mean, bounds):
            if mean_val < bound["lowerBound"] or mean_val > bound["upperBound"]:
                raise QctrlFieldError(
                    message="The initial mean must be within the bounds.",
                    fields=["initialMean", "bounds"],
                )

    results = input_.get("results")
    min_result_count = 4 + int(np.floor(3 * np.log(parameter_count)))
    if results is None or len(results) < min_result_count:
        raise QctrlFieldError(
            message="The number of results must be greater than or equal "
            "to 4 + np.floor(3 * np.log(N)), where N is the number of optimizable parameters.",
            fields=["results"],
        )

    _check_results_in_bounds(results, bounds)


AVAILABLE_OPTIMIZERS = {
    "crossEntropyInitializer": _check_cross_entropy_initializer,
    "gaussianProcessInitializer": _check_gaussian_process_initializer,
    "neuralNetworkInitializer": _check_neural_network_initializer,
    "simulatedAnnealingInitializer": _check_simulated_annealing_initializer,
    "cmaesInitializer": _check_cmaes_initializer,
}


def _check_seed(seed):
    if seed is not None and seed < 0:
        raise QctrlFieldError(
            message="Ensure seed value is greater than or equal to 0.", fields=["seed"]
        )


class CalculateClosedLoopOptimizationStepValidator(BaseMutationInputValidator):
    """
    Validator for core__calculateClosedLoopOptimizationStep mutation.
    """

    def check_optimizer(self, input_):  # pylint:disable=no-self-use
        """
        Check optimizer.
        1. only one optimizer initializer is allowed.
        2. exactly one of initializers or state can be set.
        3. check inputs for optimizer initializer.

        Raises
        ------
        QctrlFieldError
            If one of conditions above fails.
        """

        optimizer = input_.get("optimizer")

        if len(optimizer) != 1:
            raise QctrlFieldError(
                message="Exactly one field in `optimizer` must be set."
                " One of the optimizer initializers must be set in the first step and"
                " `state` must be updated for following optimization steps.",
                fields=["optimizer"],
            )

        # optimizer initializer validation is optional. That is, we might not
        # add validators for optimizers with some simple parameters.
        initializer_key = next(iter(optimizer))
        if initializer_key in AVAILABLE_OPTIMIZERS:
            AVAILABLE_OPTIMIZERS[initializer_key](input_)

    def check_results(self, input_):  # pylint:disable=no-self-use
        """
        Check cost function results:
        1. all result must have the same number of parameters.
        2. cost uncertainty must not be negative, if set.

        Raises
        ------
        QctrlFieldError
            If one of conditions above fails.
        """

        parameter_counts = []
        for result in input_.get("results"):
            parameter_counts.append(len(result["parameters"]))
            cost_uncertainty = result.get("costUncertainty")
            if cost_uncertainty is not None and cost_uncertainty < 0:
                raise QctrlFieldError(
                    message=Messages(field_name="costUncertainty", minimum=0).minimum,
                    fields=["costUncertainty"],
                )
        if len(set(parameter_counts)) > 1:
            raise QctrlFieldError(
                message="Cost function results must have the same number of parameters.",
                fields=["results"],
            )

    def check_requested_test_point_count(self, input_):  # pylint:disable=no-self-use
        """
        Check test_point_count.

        Raises
        ------
        QctrlFieldError
            If test_point_count is negative.
        """
        test_point_count = input_.get("testPointCount")
        if test_point_count is not None and test_point_count < 0:
            raise QctrlFieldError(
                message=Messages(field_name="testPointCount", minimum=0).minimum,
                fields=["testPointCount"],
            )
