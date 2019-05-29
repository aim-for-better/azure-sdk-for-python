# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CopySink(Model):
    """A copy activity sink.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: CosmosDbMongoDbApiSink, SalesforceSink,
    AzureDataExplorerSink, DynamicsSink, OdbcSink, AzureSearchIndexSink,
    AzureBlobFSSink, AzureDataLakeStoreSink, OracleSink, SqlDWSink,
    AzureSqlSink, SqlServerSink, SqlSink, DocumentDbCollectionSink,
    FileSystemSink, BlobSink, ParquetSink, AzureTableSink, AzureQueueSink,
    SapCloudForCustomerSink, DelimitedTextSink

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param write_batch_size: Write batch size. Type: integer (or Expression
     with resultType integer), minimum: 0.
    :type write_batch_size: object
    :param write_batch_timeout: Write batch timeout. Type: string (or
     Expression with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type write_batch_timeout: object
    :param sink_retry_count: Sink retry count. Type: integer (or Expression
     with resultType integer).
    :type sink_retry_count: object
    :param sink_retry_wait: Sink retry wait. Type: string (or Expression with
     resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type sink_retry_wait: object
    :param max_concurrent_connections: The maximum concurrent connection count
     for the sink data store. Type: integer (or Expression with resultType
     integer).
    :type max_concurrent_connections: object
    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'write_batch_size': {'key': 'writeBatchSize', 'type': 'object'},
        'write_batch_timeout': {'key': 'writeBatchTimeout', 'type': 'object'},
        'sink_retry_count': {'key': 'sinkRetryCount', 'type': 'object'},
        'sink_retry_wait': {'key': 'sinkRetryWait', 'type': 'object'},
        'max_concurrent_connections': {'key': 'maxConcurrentConnections', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'CosmosDbMongoDbApiSink': 'CosmosDbMongoDbApiSink', 'SalesforceSink': 'SalesforceSink', 'AzureDataExplorerSink': 'AzureDataExplorerSink', 'DynamicsSink': 'DynamicsSink', 'OdbcSink': 'OdbcSink', 'AzureSearchIndexSink': 'AzureSearchIndexSink', 'AzureBlobFSSink': 'AzureBlobFSSink', 'AzureDataLakeStoreSink': 'AzureDataLakeStoreSink', 'OracleSink': 'OracleSink', 'SqlDWSink': 'SqlDWSink', 'AzureSqlSink': 'AzureSqlSink', 'SqlServerSink': 'SqlServerSink', 'SqlSink': 'SqlSink', 'DocumentDbCollectionSink': 'DocumentDbCollectionSink', 'FileSystemSink': 'FileSystemSink', 'BlobSink': 'BlobSink', 'ParquetSink': 'ParquetSink', 'AzureTableSink': 'AzureTableSink', 'AzureQueueSink': 'AzureQueueSink', 'SapCloudForCustomerSink': 'SapCloudForCustomerSink', 'DelimitedTextSink': 'DelimitedTextSink'}
    }

    def __init__(self, **kwargs):
        super(CopySink, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.write_batch_size = kwargs.get('write_batch_size', None)
        self.write_batch_timeout = kwargs.get('write_batch_timeout', None)
        self.sink_retry_count = kwargs.get('sink_retry_count', None)
        self.sink_retry_wait = kwargs.get('sink_retry_wait', None)
        self.max_concurrent_connections = kwargs.get('max_concurrent_connections', None)
        self.type = None
