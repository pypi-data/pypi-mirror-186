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

from dataclasses import dataclass
from typing import (
    Callable,
    Union,
)

from .router import BaseRouter


@dataclass
class CoreClientSettings:
    """Settings class for core clients.

    Parameters
    ----------
    router : Union[BaseRouter, Callable]
        The router to be used in the core client. Can be either
        an instance of `BaseRouter` or a callable which accepts
        no arguments and returns an instance of `BaseRouter`.
    """

    router: Union[BaseRouter, Callable]

    def update(self, **kwargs):
        """Updates settings fields."""

        for attr, value in kwargs.items():
            if not hasattr(self, attr):
                raise AttributeError(f"Invalid field: {attr}")

            setattr(self, attr, value)

    def get_router(self) -> BaseRouter:
        """Returns the configured router to be used by the client."""
        result = self.router

        if isinstance(result, BaseRouter):
            pass

        elif callable(result):
            result = result()

        else:
            raise ValueError(f"Invalid router: {result}")

        return result
