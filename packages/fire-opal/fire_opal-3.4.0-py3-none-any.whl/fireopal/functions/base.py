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

from functools import partial

from fireopal.config import get_config
from fireopal.core import (
    core_workflow,
    run_core_workflow,
)

fire_opal_workflow = partial(core_workflow, get_config)
run_fire_opal_workflow = partial(run_core_workflow, get_config)
