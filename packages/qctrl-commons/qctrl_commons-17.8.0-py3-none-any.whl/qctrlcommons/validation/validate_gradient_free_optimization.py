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
Validator for core__calculateGradientFreeOptimization mutation.
"""

from qctrlcommons.validation.base import BaseMutationInputValidator
from qctrlcommons.validation.utils import (
    validate_cost_in_optimization_graph,
    validate_initial_value_for_optimization_variables,
    validate_optimization_variables,
    validate_output_node_in_optimization_graph,
)


class CalculateGradientFreeOptimizationValidator(BaseMutationInputValidator):
    """
    Validator for core__calculateGradientFreeOptimization mutation.
    """

    properties = {
        "optimizationCount": {"type": "number", "exclusiveMinimum": 0},
        "seed": {"type": "number", "minimum": 0},
        "iterationCount": {"type": "number", "exclusiveMinimum": 0},
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

    def check_initial_values(self, input_: dict):
        """
        Check non-default initial values.
        """
        validate_initial_value_for_optimization_variables(input_)
