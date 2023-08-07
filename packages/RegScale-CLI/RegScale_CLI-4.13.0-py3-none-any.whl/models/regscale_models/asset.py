#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Dataclass for a RegScale Asset """

# standard python imports
from dataclasses import dataclass, asdict


@dataclass
class Asset:
    """Asset Model"""

    name: str  # Required
    parentId: int  # Required
    parentModule: str  # Required
    isPublic: bool = True
    osVersion: str = None
    otherTrackingNumber: str = None
    serialNumber: str = None
    ipAddress: str = None
    macAddress: str = None
    manufacturer: str = None
    model: str = None
    assetCategory: str = None
    assetOwnerId: str = None
    operatingSystem: str = None
    osVersion: str = None
    assetType: str = None
    cmmcAssetType: str = None
    cpu: int = None
    ram: int = None
    diskStorage: int = None
    description: str = None
    endOfLifeDate: str = ""
    purchaseDate: str = ""
    status: str = None
    wizId: str = None
    wizInfo: str = None
    facilityId: int = None
    orgId: int = None
    id: int = None
    createdById: str = None
    lastUpdatedById: str = None

    @staticmethod
    def from_dict(obj: dict) -> "Asset":
        """
        Create Asset object from dict
        :param obj: dictionary
        :return: Asset class
        :rtype: Asset
        """
        _osVersion = str(obj.get("operatingSystemVersion"))
        _isPublic = bool(obj.get("isPublic"))
        _name = str(obj.get("name"))
        _otherTrackingNumber = str(obj.get("otherTrackingNumber"))
        _serialNumber = str(obj.get("serialNumber"))
        _ipAddress = str(obj.get("ipAddress"))
        _macAddress = str(obj.get("macAddress")).upper()
        _manufacturer = str(obj.get("manufacturer"))
        _model = str(obj.get("model"))
        _assetCategory = str(obj.get("assetCategory"))
        _assetOwnerId = str(obj.get("assetOwnerId"))
        _operatingSystem = str(obj.get("operatingSystem"))
        _osVersion = str(obj.get("osVersion"))
        _assetType = str(obj.get("assetType"))
        _cmmcAssetType = str(obj.get("cmmcAssetType"))
        _cpu = int(obj.get("cpu"))
        _ram = int(obj.get("ram"))
        _diskStorage = int(obj.get("diskStorage"))
        _description = str(obj.get("description"))
        _endOfLifeDate = str(obj.get("endOfLifeDate"))
        _purchaseDate = str(obj.get("purchaseDate"))
        _status = str(obj.get("status"))
        _wizId = str(obj.get("wizId"))
        _wizInfo = str(obj.get("wizInfo"))
        if obj.get("facilityId"):
            _facilityId = int(obj.get("facilityId"))
        else:
            _facilityId = None
        if obj.get("orgId"):
            _orgId = int(obj.get("orgId"))
        else:
            _orgId = None
        _parentId = int(obj.get("parentId"))
        _parentModule = str(obj.get("parentModule"))
        if obj.get("id"):
            _id = obj.get("id")
        else:
            _id = None
        return Asset(
            isPublic=_isPublic,
            name=_name,
            otherTrackingNumber=_otherTrackingNumber,
            serialNumber=_serialNumber,
            ipAddress=_ipAddress,
            macAddress=_macAddress.upper(),
            manufacturer=_manufacturer,
            model=_model,
            assetOwnerId=_assetOwnerId,
            operatingSystem=_operatingSystem,
            osVersion=_osVersion,
            assetCategory=_assetCategory,
            assetType=_assetType,
            cmmcAssetType=_cmmcAssetType,
            cpu=_cpu,
            ram=_ram,
            diskStorage=_diskStorage,
            description=_description,
            endOfLifeDate=_endOfLifeDate,
            purchaseDate=_purchaseDate,
            status=_status,
            wizId=_wizId,
            wizInfo=_wizInfo,
            facilityId=_facilityId,
            orgId=_orgId,
            parentId=_parentId,
            parentModule=_parentModule,
            id=_id,
        )

    # 'uniqueness': 'ip, macaddress'
    # Enable object to be hashable
    def __hash__(self):
        """
        Enable object to be hashable
        :return: Hashed TenableAsset
        """
        return hash(str(self))

    def __getitem__(self, key: any) -> any:
        """
        Get attribute from Pipeline
        :param any key:
        :return: value of provided key
        :rtype: any
        """
        return getattr(self, key)

    def __setitem__(self, key: any, value: any) -> None:
        """
        Set attribute in Pipeline with provided key
        :param any key: Key to change to provided value
        :param any value: New value for provided Key
        :return: None
        """
        return setattr(self, key, value)

    def __eq__(self, other) -> "Asset":
        """
        Update items in TenableAsset class
        :param other:
        :return: Updated Asset
        :rtype: Asset
        """
        return (
            self.name == other.name
            and self.ipAddress == other.ipAddress
            and self.macAddress == other.macAddress
        )

    def dict(self) -> dict:
        """
        Create a dictionary from the Asset dataclass
        :return: Dictionary of Asset
        :rtype: dict
        """
        return {k: v for k, v in asdict(self).items()}
