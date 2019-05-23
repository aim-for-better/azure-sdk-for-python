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


class InstallOCIDriverTaskInput(Model):
    """Input for the service task to install an OCI driver.

    :param driver_package_name: Name of the uploaded driver package to
     install.
    :type driver_package_name: str
    """

    _attribute_map = {
        'driver_package_name': {'key': 'driverPackageName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(InstallOCIDriverTaskInput, self).__init__(**kwargs)
        self.driver_package_name = kwargs.get('driver_package_name', None)
