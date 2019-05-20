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


class PivotProperties(Model):
    """Each pivot must contain a 'type' and 'name'.

    :param type: Data type to show in view. Possible values include:
     'Dimension', 'TagKey'
    :type type: str or ~azure.mgmt.costmanagement.models.PivotTypeType
    :param name: Data field to show in view.
    :type name: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, type=None, name: str=None, **kwargs) -> None:
        super(PivotProperties, self).__init__(**kwargs)
        self.type = type
        self.name = name
