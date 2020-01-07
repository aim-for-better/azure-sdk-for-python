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


class ReplaceAllFirewallRulesOperationResponse(Model):
    """An existing operation for replacing the firewall rules.

    :param operation_id: The operation ID
    :type operation_id: str
    """

    _attribute_map = {
        'operation_id': {'key': 'operationId', 'type': 'str'},
    }

    def __init__(self, *, operation_id: str=None, **kwargs) -> None:
        super(ReplaceAllFirewallRulesOperationResponse, self).__init__(**kwargs)
        self.operation_id = operation_id
