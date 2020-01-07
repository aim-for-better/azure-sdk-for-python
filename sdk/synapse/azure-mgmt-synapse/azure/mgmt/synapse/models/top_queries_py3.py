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


class TopQueries(Model):
    """A database query.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar aggregation_function: The function that is used to aggregate each
     query's metrics. Possible values include: 'min', 'max', 'avg', 'sum'
    :vartype aggregation_function: str or
     ~azure.mgmt.synapse.models.QueryAggregationFunction
    :ivar execution_type: The execution type that is used to filter the query
     instances that are returned. Possible values include: 'any', 'regular',
     'irregular', 'aborted', 'exception'
    :vartype execution_type: str or
     ~azure.mgmt.synapse.models.QueryExecutionType
    :ivar interval_type: The duration of the interval (ISO8601 duration
     format).
    :vartype interval_type: str
    :ivar number_of_top_queries: The number of requested queries.
    :vartype number_of_top_queries: float
    :ivar observation_start_time: The start time for queries that are returned
     (ISO8601 format)
    :vartype observation_start_time: datetime
    :ivar observation_end_time: The end time for queries that are returned
     (ISO8601 format)
    :vartype observation_end_time: datetime
    :ivar observed_metric: The type of metric to use for ordering the top
     metrics. Possible values include: 'cpu', 'io', 'logio', 'duration',
     'executionCount'
    :vartype observed_metric: str or
     ~azure.mgmt.synapse.models.QueryObservedMetricType
    :ivar queries: The list of queries.
    :vartype queries: list[~azure.mgmt.synapse.models.QueryStatistic]
    """

    _validation = {
        'aggregation_function': {'readonly': True},
        'execution_type': {'readonly': True},
        'interval_type': {'readonly': True},
        'number_of_top_queries': {'readonly': True},
        'observation_start_time': {'readonly': True},
        'observation_end_time': {'readonly': True},
        'observed_metric': {'readonly': True},
        'queries': {'readonly': True},
    }

    _attribute_map = {
        'aggregation_function': {'key': 'aggregationFunction', 'type': 'QueryAggregationFunction'},
        'execution_type': {'key': 'executionType', 'type': 'QueryExecutionType'},
        'interval_type': {'key': 'intervalType', 'type': 'str'},
        'number_of_top_queries': {'key': 'numberOfTopQueries', 'type': 'float'},
        'observation_start_time': {'key': 'observationStartTime', 'type': 'iso-8601'},
        'observation_end_time': {'key': 'observationEndTime', 'type': 'iso-8601'},
        'observed_metric': {'key': 'observedMetric', 'type': 'QueryObservedMetricType'},
        'queries': {'key': 'queries', 'type': '[QueryStatistic]'},
    }

    def __init__(self, **kwargs) -> None:
        super(TopQueries, self).__init__(**kwargs)
        self.aggregation_function = None
        self.execution_type = None
        self.interval_type = None
        self.number_of_top_queries = None
        self.observation_start_time = None
        self.observation_end_time = None
        self.observed_metric = None
        self.queries = None
