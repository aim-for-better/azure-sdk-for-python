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


class EntityReference(Model):
    """The entity reference.

    :param type: The type of this referenced entity. Possible values include:
     'IntegrationRuntimeReference', 'LinkedServiceReference'
    :type type: str or
     ~azure.mgmt.datafactory.models.IntegrationRuntimeEntityReferenceType
    :param reference_name: The name of this referenced entity.
    :type reference_name: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EntityReference, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.reference_name = kwargs.get('reference_name', None)
