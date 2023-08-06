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

from typing import (
    Any,
    Dict,
    List,
    Optional,
)

from fireopal.core import print_warnings

from .base import fire_opal_workflow


@fire_opal_workflow("validate_input_circuits_workflow", formatter=print_warnings)
def validate(
    circuits: List[str],
    credentials: Dict[str, Any],
    backend: Optional[str] = None,
    backend_name: Optional[str] = None,
):
    """
    Validate the compatibility of a batch of circuits for Fire Opal.

    Parameters
    ----------
    circuits : List[str]
        A list of quantum circuit in the form QASM string. You can use Qiskit to
        generate these strings.
    credentials : Dict[str, Any]
        The credentials for running circuits on an IBM backend. This dictionary should
        contain key-value entries with keys `token`, `project`, `hub`, and `group`.
    backend : str, optional
        The backend device that should be used to run circuits. To be deprecated no sooner
        than 28 February 2023. If provided, takes precedence over `backend_name`.
    backend_name : str, optional
        The backend device that will be used to run circuits after validation.
    """
    return {
        "circuits": circuits,
        "credentials": credentials,
        "backend": backend,
        "backend_name": backend_name,
    }
