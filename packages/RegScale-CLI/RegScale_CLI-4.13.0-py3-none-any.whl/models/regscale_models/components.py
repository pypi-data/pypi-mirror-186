#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Dataclass for a RegScale Component """

# standard python imports
from dataclasses import dataclass


@dataclass
class Component:
    """Component Model"""

    title: str
    description: str
    componentType: str
    componentOwnerId: str
    purpose: str = None
    securityPlansId: int = None
    cmmcAssetType: str = None
    createdBy: str = None
    createdById: str = None
    dateCreated: str = None
    lastUpdatedBy: str = None
    lastUpdatedById: str = None
    dateLastUpdated: str = None
    status: str = "Active"
    uuid: str = None
    componentOwner: str = None
    cmmcExclusion: str = False
    id: int = None
    isPublic: str = True

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
