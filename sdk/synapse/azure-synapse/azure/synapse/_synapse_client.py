# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

from ._configuration import SynapseClientConfiguration
from .operations import MonitoringOperations
from .operations import SparkBatchOperations
from .operations import SparkSessionOperations
from .operations import WorkspaceAclOperations
from . import models


class SynapseClient(object):
    """

    :ivar monitoring: MonitoringOperations operations
    :vartype monitoring: azure.synapse.operations.MonitoringOperations
    :ivar spark_batch: SparkBatchOperations operations
    :vartype spark_batch: azure.synapse.operations.SparkBatchOperations
    :ivar spark_session: SparkSessionOperations operations
    :vartype spark_session: azure.synapse.operations.SparkSessionOperations
    :ivar workspace_acl: WorkspaceAclOperations operations
    :vartype workspace_acl: azure.synapse.operations.WorkspaceAclOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param synapse_dns_suffix: Gets the DNS suffix used as the base for all Synapse service requests.
    :type synapse_dns_suffix: str
    :param livy_api_version: Valid api-version for the request.
    :type livy_api_version: str
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        synapse_dns_suffix,  # type: str
        livy_api_version="2019-11-01-preview",  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        base_url = 'https://{workspaceName}.{SynapseDnsSuffix}'
        self._config = SynapseClientConfiguration(credential, synapse_dns_suffix, livy_api_version, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.monitoring = MonitoringOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.spark_batch = SparkBatchOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.spark_session = SparkSessionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_acl = WorkspaceAclOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> SynapseClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
