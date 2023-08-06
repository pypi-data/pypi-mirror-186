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

import sys

import click
from qctrlclient import (
    CliAuth,
    GraphQLClient,
    get_default_api_url,
    get_default_cli_auth,
)
from qctrlclient.client import QctrlException
from qctrlclient.globals import global_value

from fireopal.constants import INVALID_SUBSCRIPTION_ERROR
from fireopal.core import (
    ApiRouter,
    CoreClientSettings,
    LocalRouter,
    RemoteRegistry,
)


def _get_fire_opal_api_router(client: GraphQLClient) -> ApiRouter:
    """Returns an `ApiRouter` with the required configuration
    for Fire Opal.
    """
    return ApiRouter(client, RemoteRegistry.FIRE_OPAL)


def get_default_router() -> ApiRouter:
    """Returns the default router that the Fire Opal
    client uses.
    """
    client = GraphQLClient(get_default_api_url(), auth=get_default_cli_auth())

    try:
        client.check_user_role("fire-opal-cli-access")
    except QctrlException:
        click.echo(INVALID_SUBSCRIPTION_ERROR, err=True)
        sys.exit(1)

    return _get_fire_opal_api_router(client)


@global_value("FIRE_OPAL_CONFIG")
def get_config() -> CoreClientSettings:
    """Returns the global Fire Opal settings."""
    return CoreClientSettings(router=get_default_router)


def configure(**kwargs):
    """Updates the global Fire Opal settings. See `CoreClientSettings`
    for details on which fields can be updated.
    """
    config = get_config()
    config.update(**kwargs)


def configure_api(api_url: str, oidc_url: str):
    """Convenience function to configure Fire Opal for API
    routing.

    Parameters
    ----------
    api_url : str
        URL of the GraphQL schema
    oidc_url : str
        Base URL of the OIDC provider e.g. Keycloak
    """
    client = GraphQLClient(api_url, CliAuth(oidc_url))

    configure(router=_get_fire_opal_api_router(client))


def configure_local(resolver: "BaseResolver"):
    """Convenience function to configure Fire Opal for local
    routing.

    Parameters
    ----------
    resolver : BaseResolver
        A local implementation of a workflow resolver which uses
        a registry that implements all of the available Fire Opal
        workflows
    """
    configure(router=LocalRouter(resolver))
