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

from .proxy_resource_py3 import ProxyResource


class View(ProxyResource):
    """States and configurations of Cost Analysis.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param e_tag: eTag of the resource. To handle concurrent update scenario,
     this field will be used to determine whether the user is updating the
     latest version or not.
    :type e_tag: str
    :param version: View API version used to create the view.
    :type version: str
    :param query_version: Query API version to use.
    :type query_version: str
    :param display_name: User input name of the view. Required.
    :type display_name: str
    :param scope: Cost Management scope to save the view on. This includes
     'subscriptions/{subscriptionId}' for subscription scope,
     'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for
     resourceGroup scope,
     'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for
     Billing Account scope,
     'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
     for Department scope,
     'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
     for EnrollmentAccount scope,
     'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
     for BillingProfile scope,
     'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}'
     for InvoiceSection scope,
     'providers/Microsoft.Management/managementGroups/{managementGroupId}' for
     Management Group scope,
     '/providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}'
     for ExternalBillingAccount scope, and
     '/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}'
     for ExternalSubscription scope.
    :type scope: str
    :ivar created_on: Date the user created this view.
    :vartype created_on: datetime
    :ivar modified_on: Date when the user last modified this view.
    :vartype modified_on: datetime
    :ivar view_type: Required. The type of the report. Usage represents actual
     usage, forecast represents forecasted data and UsageAndForecast represents
     both usage and forecasted data. Actual usage and forecasted data can be
     differentiated based on dates. Default value: "Usage" .
    :vartype view_type: str
    :param timeframe: Required. The time frame for pulling data for the
     report. If custom, then a specific time period must be provided. Possible
     values include: 'WeekToDate', 'MonthToDate', 'YearToDate', 'Custom'
    :type timeframe: str or ~azure.mgmt.costmanagement.models.TimeframeType
    :param time_period: Has time period for pulling data for the report.
    :type time_period:
     ~azure.mgmt.costmanagement.models.ReportConfigTimePeriod
    :param dataset: Has definition for data in this report config.
    :type dataset: ~azure.mgmt.costmanagement.models.ReportConfigDataset
    :param chart: Chart type of the main view in Cost Analysis. Required.
     Possible values include: 'Area', 'Line', 'StackedColumn', 'GroupedColumn',
     'Table'
    :type chart: str or ~azure.mgmt.costmanagement.models.ChartType
    :param accumulated: Show costs accumulated over time. Possible values
     include: 'true', 'false'
    :type accumulated: str or ~azure.mgmt.costmanagement.models.enum
    :param metric: Metric to use when displaying costs. Possible values
     include: 'ActualCost', 'AmortizedCost', 'AHUB'
    :type metric: str or ~azure.mgmt.costmanagement.models.MetricType
    :param kpis: List of KPIs to show in Cost Analysis UI.
    :type kpis: list[~azure.mgmt.costmanagement.models.KpiProperties]
    :param pivots: Configuration of 3 sub-views in the Cost Analysis UI.
    :type pivots: list[~azure.mgmt.costmanagement.models.PivotProperties]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'created_on': {'readonly': True},
        'modified_on': {'readonly': True},
        'view_type': {'required': True, 'constant': True},
        'timeframe': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'query_version': {'key': 'properties.queryVersion', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'created_on': {'key': 'properties.createdOn', 'type': 'iso-8601'},
        'modified_on': {'key': 'properties.modifiedOn', 'type': 'iso-8601'},
        'view_type': {'key': 'properties.query.type', 'type': 'str'},
        'timeframe': {'key': 'properties.query.timeframe', 'type': 'str'},
        'time_period': {'key': 'properties.query.timePeriod', 'type': 'ReportConfigTimePeriod'},
        'dataset': {'key': 'properties.query.dataset', 'type': 'ReportConfigDataset'},
        'chart': {'key': 'properties.chart', 'type': 'str'},
        'accumulated': {'key': 'properties.accumulated', 'type': 'str'},
        'metric': {'key': 'properties.metric', 'type': 'str'},
        'kpis': {'key': 'properties.kpis', 'type': '[KpiProperties]'},
        'pivots': {'key': 'properties.pivots', 'type': '[PivotProperties]'},
    }

    view_type = "Usage"

    def __init__(self, *, timeframe, e_tag: str=None, version: str=None, query_version: str=None, display_name: str=None, scope: str=None, time_period=None, dataset=None, chart=None, accumulated=None, metric=None, kpis=None, pivots=None, **kwargs) -> None:
        super(View, self).__init__(e_tag=e_tag, **kwargs)
        self.version = version
        self.query_version = query_version
        self.display_name = display_name
        self.scope = scope
        self.created_on = None
        self.modified_on = None
        self.timeframe = timeframe
        self.time_period = time_period
        self.dataset = dataset
        self.chart = chart
        self.accumulated = accumulated
        self.metric = metric
        self.kpis = kpis
        self.pivots = pivots
