# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class CachingTypes(str, Enum):
    """Specifies the caching requirements. :code:`<br>`:code:`<br>` Possible values are:
    :code:`<br>`:code:`<br>` **None** :code:`<br>`:code:`<br>` **ReadOnly**
    :code:`<br>`:code:`<br>` **ReadWrite** :code:`<br>`:code:`<br>` Default: **None for Standard
    storage. ReadOnly for Premium storage**
    """

    none = "None"
    read_only = "ReadOnly"
    read_write = "ReadWrite"

class DiskCreateOptionTypes(str, Enum):
    """Specifies how the virtual machine should be created.:code:`<br>`:code:`<br>` Possible values
    are::code:`<br>`:code:`<br>` **Attach** \u2013 This value is used when you are using a
    specialized disk to create the virtual machine.:code:`<br>`:code:`<br>` **FromImage** \u2013
    This value is used when you are using an image to create the virtual machine. If you are using
    a platform image, you also use the imageReference element described above. If you are using a
    marketplace image, you  also use the plan element previously described.
    """

    from_image = "FromImage"
    empty = "Empty"
    attach = "Attach"

class OperatingSystemTypes(str, Enum):
    """The operating system of the osDiskImage.
    """

    windows = "Windows"
    linux = "Linux"

class ProtocolTypes(str, Enum):
    """Specifies the protocol of listener. :code:`<br>`:code:`<br>` Possible values are: :code:`<br>`\
    **http** :code:`<br>`:code:`<br>` **https**
    """

    http = "Http"
    https = "Https"

class SettingNames(str, Enum):
    """Specifies the name of the setting to which the content applies. Possible values are:
    FirstLogonCommands and AutoLogon.
    """

    auto_logon = "AutoLogon"
    first_logon_commands = "FirstLogonCommands"

class StatusLevelTypes(str, Enum):
    """The level code.
    """

    info = "Info"
    warning = "Warning"
    error = "Error"

class UpgradeMode(str, Enum):
    """Specifies the mode of an upgrade to virtual machines in the scale set.:code:`<br />`:code:`<br
    />` Possible values are::code:`<br />`:code:`<br />` **Manual** - You  control the application
    of updates to virtual machines in the scale set. You do this by using the manualUpgrade
    action.:code:`<br />`:code:`<br />` **Automatic** - All virtual machines in the scale set are
    automatically updated at the same time.
    """

    automatic = "Automatic"
    manual = "Manual"

class VirtualMachineScaleSetSkuScaleType(str, Enum):
    """The scale type applicable to the sku.
    """

    automatic = "Automatic"
    none = "None"

class VirtualMachineSizeTypes(str, Enum):
    """Specifies the size of the virtual machine. For more information about virtual machine sizes,
    see `Sizes for virtual machines <https://docs.microsoft.com/azure/virtual-machines/virtual-
    machines-windows-sizes?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
    :code:`<br>`:code:`<br>` The available VM sizes depend on region and availability set. For a
    list of available sizes use these APIs:  :code:`<br>`:code:`<br>` `List all available virtual
    machine sizes in an availability set
    <https://docs.microsoft.com/rest/api/compute/availabilitysets/listavailablesizes>`_
    :code:`<br>`:code:`<br>` `List all available virtual machine sizes in a region
    <https://docs.microsoft.com/rest/api/compute/virtualmachinesizes/list>`_
    :code:`<br>`:code:`<br>` `List all available virtual machine sizes for resizing
    <https://docs.microsoft.com/rest/api/compute/virtualmachines/listavailablesizes>`_
    """

    basic_a0 = "Basic_A0"
    basic_a1 = "Basic_A1"
    basic_a2 = "Basic_A2"
    basic_a3 = "Basic_A3"
    basic_a4 = "Basic_A4"
    standard_a0 = "Standard_A0"
    standard_a1 = "Standard_A1"
    standard_a2 = "Standard_A2"
    standard_a3 = "Standard_A3"
    standard_a4 = "Standard_A4"
    standard_a5 = "Standard_A5"
    standard_a6 = "Standard_A6"
    standard_a7 = "Standard_A7"
    standard_a8 = "Standard_A8"
    standard_a9 = "Standard_A9"
    standard_a10 = "Standard_A10"
    standard_a11 = "Standard_A11"
    standard_d1 = "Standard_D1"
    standard_d2 = "Standard_D2"
    standard_d3 = "Standard_D3"
    standard_d4 = "Standard_D4"
    standard_d11 = "Standard_D11"
    standard_d12 = "Standard_D12"
    standard_d13 = "Standard_D13"
    standard_d14 = "Standard_D14"
    standard_d1_v2 = "Standard_D1_v2"
    standard_d2_v2 = "Standard_D2_v2"
    standard_d3_v2 = "Standard_D3_v2"
    standard_d4_v2 = "Standard_D4_v2"
    standard_d5_v2 = "Standard_D5_v2"
    standard_d11_v2 = "Standard_D11_v2"
    standard_d12_v2 = "Standard_D12_v2"
    standard_d13_v2 = "Standard_D13_v2"
    standard_d14_v2 = "Standard_D14_v2"
    standard_d15_v2 = "Standard_D15_v2"
    standard_ds1 = "Standard_DS1"
    standard_ds2 = "Standard_DS2"
    standard_ds3 = "Standard_DS3"
    standard_ds4 = "Standard_DS4"
    standard_ds11 = "Standard_DS11"
    standard_ds12 = "Standard_DS12"
    standard_ds13 = "Standard_DS13"
    standard_ds14 = "Standard_DS14"
    standard_ds1_v2 = "Standard_DS1_v2"
    standard_ds2_v2 = "Standard_DS2_v2"
    standard_ds3_v2 = "Standard_DS3_v2"
    standard_ds4_v2 = "Standard_DS4_v2"
    standard_ds5_v2 = "Standard_DS5_v2"
    standard_ds11_v2 = "Standard_DS11_v2"
    standard_ds12_v2 = "Standard_DS12_v2"
    standard_ds13_v2 = "Standard_DS13_v2"
    standard_ds14_v2 = "Standard_DS14_v2"
    standard_ds15_v2 = "Standard_DS15_v2"
    standard_g1 = "Standard_G1"
    standard_g2 = "Standard_G2"
    standard_g3 = "Standard_G3"
    standard_g4 = "Standard_G4"
    standard_g5 = "Standard_G5"
    standard_gs1 = "Standard_GS1"
    standard_gs2 = "Standard_GS2"
    standard_gs3 = "Standard_GS3"
    standard_gs4 = "Standard_GS4"
    standard_gs5 = "Standard_GS5"
