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
Validator for core__calculateStochasticOptimization mutation.
"""

from qctrlcommons.exceptions import QctrlFieldError
from qctrlcommons.validation.base import BaseMutationInputValidator
from qctrlcommons.validation.utils import (
    validate_cost_in_optimization_graph,
    validate_optimization_variables,
    validate_output_node_in_optimization_graph,
)


def _check_adam_optimizer(input_):
    """
    Checks the configuration for the Adam optimizer.
    """

    learning_rate = input_["optimizer"]["adam"]["learningRate"]
    if learning_rate <= 0:
        raise QctrlFieldError(
            message="'learning_rate' of the Adam optimizer must be positive.",
            fields=["adam"],
        )


AVAILABLE_OPTIMIZERS = {"adam": _check_adam_optimizer}


class CalculateStochasticOptimizationValidator(BaseMutationInputValidator):
    """
    Validator for core__calculateStochasticOptimization mutation.
    """

    properties = {
        "iterationCount": {"type": "number", "exclusiveMinimum": 0},
        "seed": {"type": "number", "minimum": 0},
    }

    # pylint:disable=no-self-use
    def check_cost_in_graph(self, input_: dict):
        """
        Expect the cost node to be in the graph.
        """
        validate_cost_in_optimization_graph(input_)

    def check_output_node_names(self, input_: dict):
        """
        Validate output nodes.
        """
        validate_output_node_in_optimization_graph(input_)

    def check_optimizable_variables(self, input_: dict):
        """
        Check that optimizable variables are present in the input graph.
        """
        validate_optimization_variables(input_)

    def check_optimizer(self, input_):
        """
        Check optimizer.

        1. if not set, skip
        2. if set, must be one of those supported
        3. check configuration

        Raises
        ------
        QctrlFieldError
            If one of conditions above fails.
        """

        optimizer = input_.get("optimizer")

        # skip checking if default optimizer is used.
        if optimizer is None:
            return

        if len(optimizer) != 1:
            raise QctrlFieldError(
                message="When set, exactly one field in `optimizer` can be non-null.",
                fields=["optimizer"],
            )

        optimizer_name = next(iter(optimizer))

        # skip check for state
        if optimizer_name == "state":
            return

        if optimizer_name not in AVAILABLE_OPTIMIZERS:
            raise QctrlFieldError(
                message="One of the following optimizers must be set: "
                f"{list(AVAILABLE_OPTIMIZERS.keys())}",
                fields=["optimizer"],
            )

        AVAILABLE_OPTIMIZERS[optimizer_name](input_)
