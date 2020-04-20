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

from enum import Enum


class Type(str, Enum):

    storage_account = "StorageAccount"
    event_hub = "EventHub"


class DataSourceKind(str, Enum):

    windows_event = "WindowsEvent"
    windows_performance_counter = "WindowsPerformanceCounter"
    iis_logs = "IISLogs"
    linux_syslog = "LinuxSyslog"
    linux_syslog_collection = "LinuxSyslogCollection"
    linux_performance_object = "LinuxPerformanceObject"
    linux_performance_collection = "LinuxPerformanceCollection"
    custom_log = "CustomLog"
    custom_log_collection = "CustomLogCollection"
    azure_audit_log = "AzureAuditLog"
    azure_activity_log = "AzureActivityLog"
    generic_data_source = "GenericDataSource"
    change_tracking_custom_path = "ChangeTrackingCustomPath"
    change_tracking_path = "ChangeTrackingPath"
    change_tracking_services = "ChangeTrackingServices"
    change_tracking_data_type_configuration = "ChangeTrackingDataTypeConfiguration"
    change_tracking_default_registry = "ChangeTrackingDefaultRegistry"
    change_tracking_registry = "ChangeTrackingRegistry"
    change_tracking_linux_path = "ChangeTrackingLinuxPath"
    linux_change_tracking_path = "LinuxChangeTrackingPath"
    change_tracking_content_location = "ChangeTrackingContentLocation"
    windows_telemetry = "WindowsTelemetry"
    office365 = "Office365"
    security_windows_baseline_configuration = "SecurityWindowsBaselineConfiguration"
    security_center_security_windows_baseline_configuration = "SecurityCenterSecurityWindowsBaselineConfiguration"
    security_event_collection_configuration = "SecurityEventCollectionConfiguration"
    security_insights_security_event_collection_configuration = "SecurityInsightsSecurityEventCollectionConfiguration"
    import_computer_group = "ImportComputerGroup"
    network_monitoring = "NetworkMonitoring"
    itsm = "Itsm"
    dns_analytics = "DnsAnalytics"
    application_insights = "ApplicationInsights"
    sql_data_classification = "SqlDataClassification"


class DataSourceType(str, Enum):

    custom_logs = "CustomLogs"
    azure_watson = "AzureWatson"


class WorkspaceSkuNameEnum(str, Enum):

    free = "Free"
    standard = "Standard"
    premium = "Premium"
    per_node = "PerNode"
    per_gb2018 = "PerGB2018"
    standalone = "Standalone"
    capacity_reservation = "CapacityReservation"


class EntityStatus(str, Enum):

    creating = "Creating"
    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"
    deleting = "Deleting"
    provisioning_account = "ProvisioningAccount"


class PublicNetworkAccessType(str, Enum):

    enabled = "Enabled"  #: Enables connectivity to Log Analytics through public DNS.
    disabled = "Disabled"  #: Disables public connectivity to Log Analytics through public DNS.


class ClusterSkuNameEnum(str, Enum):

    capacity_reservation = "CapacityReservation"


class IdentityType(str, Enum):

    system_assigned = "SystemAssigned"
    none = "None"


class StorageInsightState(str, Enum):

    ok = "OK"
    error = "ERROR"
