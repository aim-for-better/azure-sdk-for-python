# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration_async import PolicyClientConfiguration
from .operations_async import PolicyAssignmentsOperations
from .operations_async import PolicyDefinitionsOperations
from .operations_async import PolicySetDefinitionsOperations
from .. import models


class PolicyClient(object):
    """To manage and control access to your resources, you can define customized policies and assign them at a scope.

    :ivar policy_assignments: PolicyAssignmentsOperations operations
    :vartype policy_assignments: azure.mgmt.resource.policy.v2018_05_01.aio.operations_async.PolicyAssignmentsOperations
    :ivar policy_definitions: PolicyDefinitionsOperations operations
    :vartype policy_definitions: azure.mgmt.resource.policy.v2018_05_01.aio.operations_async.PolicyDefinitionsOperations
    :ivar policy_set_definitions: PolicySetDefinitionsOperations operations
    :vartype policy_set_definitions: azure.mgmt.resource.policy.v2018_05_01.aio.operations_async.PolicySetDefinitionsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = PolicyClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.policy_assignments = PolicyAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.policy_definitions = PolicyDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.policy_set_definitions = PolicySetDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "PolicyClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
