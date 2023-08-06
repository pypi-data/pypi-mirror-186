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
Node for the filter function.
"""
from typing import (
    Optional,
    Union,
)

import forge
import numpy as np

from qctrlcommons.node import node_data
from qctrlcommons.node.base import Node
from qctrlcommons.node.documentation import Category
from qctrlcommons.node.node_data import Pwc
from qctrlcommons.node.utils import validate_filter_function_input


class FilterFunctionOperation(Node):
    r"""
    Evaluate the filter function for a control Hamiltonian and a noise operator
    at the given frequency elements.

    Parameters
    ----------
    control_hamiltonian : Pwc
        The control Hamiltonian :math:`H_\mathrm{c}(t)`.
    noise_operator : Pwc
        The noise operator :math:`N(t)`.
    frequencies : list or tuple or np.ndarray
        The elements in the frequency domain at which to return the values of the filter function.
    sample_count : int, optional
        The number of points in time, :math:`M`, to sample the control-frame noise operator.
        These samples are used to calculate the approximate Fourier integral efficiently.
        If None the piecewise Fourier integral is calculated exactly.
        Defaults to 100.
    projection_operator : np.ndarray, optional
        The projection operator :math:`P`. Defaults to None, in which case the identity operator
        is used.
    name : str, optional
        The name of the node.

    Returns
    -------
    ~graphs.FilterFunction
        The filter function.

    See Also
    --------
    frequency_domain_noise_operator :
        Control-frame noise operator in the frequency domain.

    Notes
    -----
    The filter function is defined as [1]_:

    .. math::
        F(f) = \frac{1}{\mathrm{Tr}(P)} \mathrm{Tr} \left(
        P \mathcal{F} \left\{ \tilde N^\prime(t) \right\}(f)
        \mathcal{F} \left\{ \tilde N^\prime(t) \right\}(f)^\dagger P \right),

    with the control-frame noise operator in the frequency domain

    .. math::
        \mathcal{F} \left\{ \tilde N^\prime(t) \right\}(f) = \int_0^\tau
        e^{-i 2\pi f t} \tilde N^\prime(t) \mathrm{d}t,

    where

    .. math::
        \tilde N^\prime(t) = \tilde N(t) - \frac{\mathrm{Tr}\left( P \tilde N(t)
        P \right)}{\mathrm{Tr}(P)} \mathbb{I}

    is the traceless control-frame noise operator in the time domain,

    .. math::
        \tilde N(t) = U_c^\dagger(t) N(t) U_c(t)

    is the control-frame noise operator in the time domain, and :math:`U_c(t)` is
    the time evolution induced by the control Hamiltonian.

    References
    ----------
    .. [1] `H. Ball, M. J. Biercuk, A. R. R. Carvalho, J. Chen, M. Hush,
            L. A. De Castro, L. Li, P. J. Liebermann, H. J. Slatyer, and C. Edmunds,
            Quantum Sci. Technol. 6, 044011 (2021).
            <https://doi.org/10.1088/2058-9565/abdca6>`_
    """

    name = "filter_function"
    args = [
        forge.arg("control_hamiltonian", type=Pwc),
        forge.arg("noise_operator", type=Pwc),
        forge.arg("frequencies", type=Union[list, tuple, np.ndarray]),
        forge.arg("sample_count", type=Optional[int], default=100),
        forge.arg("projection_operator", type=Optional[np.ndarray], default=None),
    ]
    rtype = node_data.FilterFunction
    categories = [Category.TIME_EVOLUTION]

    @classmethod
    def create_node_data(cls, _operation, **kwargs):
        control_hamiltonian = kwargs.get("control_hamiltonian")
        noise_operator = kwargs.get("noise_operator")
        frequencies = kwargs.get("frequencies")
        frequencies = np.asarray(frequencies)
        sample_count = kwargs.get("sample_count")
        projection_operator = kwargs.get("projection_operator")
        _ = validate_filter_function_input(
            control_hamiltonian,
            noise_operator,
            frequencies,
            sample_count,
            projection_operator,
        )

        return node_data.FilterFunction(
            _operation, frequencies=frequencies, exact=sample_count is None
        )


class FrequencyDomainNoiseOperator(Node):
    r"""
    Create a control-frame noise operator in the frequency domain for a control Hamiltonian
    and a noise operator at the given frequencies.

    Parameters
    ----------
    control_hamiltonian : Pwc
        The control Hamiltonian :math:`H_\mathrm{c}(t)`.
    noise_operator : Pwc
        The noise operator :math:`N(t)`.
    frequencies : list or tuple or np.ndarray
        The elements in the frequency domain at which to return the values of the filter function.
    sample_count : int, optional
        The number of points in time, :math:`M`, to sample the control-frame noise operator.
        These samples are used to calculate the approximate Fourier integral efficiently.
        If None the piecewise Fourier integral is calculated exactly.
        Defaults to 100.
    projection_operator : np.ndarray, optional
        The projection operator :math:`P`. Defaults to None, in which case the identity operator
        is used.
    name : str, optional
        The name of the node.

    Returns
    -------
    Tensor
        The noise operator in the frequency domain.

    See Also
    --------
    filter_function :
        The filter function.

    Notes
    -----
    The control-frame noise operator in the frequency domain
    is defined as the Fourier transform of the operator in the time domain [1]_:

    .. math::
        \mathcal{F} \left\{ \tilde N^\prime(t) \right\}(f) = \int_0^\tau
        e^{-i 2\pi f t} \tilde N^\prime(t) \mathrm{d}t,

    where

    .. math::
        \tilde N^\prime(t) = \tilde N(t) - \frac{\mathrm{Tr}\left( P \tilde N(t)
        P \right)}{\mathrm{Tr}(P)} \mathbb{I}

    is the traceless control-frame noise operator in the time domain,

    .. math::
        \tilde N(t) = U_c^\dagger(t) N(t) U_c(t)

    is the control-frame noise operator in the time domain, and :math:`U_c(t)` is
    the time evolution induced by the control Hamiltonian. If `sample_count` is
    set, the Fourier integral is approximated as

    .. math::
        \mathcal{F} \left\{ \tilde N^\prime(t) \right\}(f) \approx \sum_{n=0}^{M-1}
        \frac{\tau}{M} e^{-i 2\pi f n \tau/M}
        \langle \tilde N^\prime (n\tau/M) \rangle,

    where :math:`\tau` is the duration of the control Hamiltonian.

    References
    ----------
    .. [1] `H. Ball, M. J. Biercuk, A. R. R. Carvalho, J. Chen, M. Hush,
            L. A. De Castro, L. Li, P. J. Liebermann, H. J. Slatyer, and C. Edmunds,
            Quantum Sci. Technol. 6, 044011 (2021).
            <https://doi.org/10.1088/2058-9565/abdca6>`_
    """

    name = "frequency_domain_noise_operator"
    args = [
        forge.arg("control_hamiltonian", type=Pwc),
        forge.arg("noise_operator", type=Pwc),
        forge.arg("frequencies", type=Union[list, tuple, np.ndarray]),
        forge.arg("sample_count", type=Optional[int], default=100),
        forge.arg("projection_operator", type=Optional[np.ndarray], default=None),
    ]
    rtype = node_data.Tensor
    categories = [Category.TIME_EVOLUTION]

    @classmethod
    def create_node_data(cls, _operation, **kwargs):
        control_hamiltonian = kwargs.get("control_hamiltonian")
        noise_operator = kwargs.get("noise_operator")
        frequencies = kwargs.get("frequencies")
        frequencies = np.asarray(frequencies)
        sample_count = kwargs.get("sample_count")
        projection_operator = kwargs.get("projection_operator")
        dimension = validate_filter_function_input(
            control_hamiltonian,
            noise_operator,
            frequencies,
            sample_count,
            projection_operator,
        )
        count = len(frequencies)

        return node_data.Tensor(_operation, shape=(count, dimension, dimension))
