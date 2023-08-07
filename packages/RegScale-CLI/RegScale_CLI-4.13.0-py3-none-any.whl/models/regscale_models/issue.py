#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Dataclass for a RegScale Issue """

# standard python imports
from dataclasses import dataclass, asdict


@dataclass
class Issue:
    """Issue Model"""

    title: str = ""  # Required
    severityLevel: str = ""  # Required
    issueOwnerId: str = ""  # Required
    dueDate: str = ""  # Required
    id: int = None
    uuid: str = None
    dateCreated: str = None
    description: str = None
    issueOwner: str = None
    costEstimate: int = None
    levelOfEffort: int = None
    identification: str = None
    sourceReport: str = None
    status: str = None
    dateCompleted: str = None
    facility: str = None
    facilityId: int = None
    org: str = None
    orgId: int = None
    controlId: int = None
    assessmentId: int = None
    requirementId: int = None
    securityPlanId: int = None
    projectId: int = None
    supplyChainId: int = None
    policyId: int = None
    componentId: int = None
    incidentId: int = None
    jiraId: str = None
    serviceNowId: str = None
    wizId: str = None
    defenderId: str = None
    defenderCloudId: str = None
    prismaId: str = None
    tenableId: str = None
    qualysId: str = None
    pluginId: str = None
    cve: str = None
    assetIdentifier: str = None
    falsePositive: str = None
    operationalRequirement: str = None
    autoApproved: str = None
    kevList: str = None
    dateFirstDetected: str = None
    changes: str = None
    vendorDependency: str = None
    vendorName: str = None
    vendorLastUpdate: str = None
    vendorActions: str = None
    deviationRationale: str = None
    parentId: int = None
    parentModule: str = None
    createdBy: str = None
    createdById: str = None
    lastUpdatedBy: str = None
    lastUpdatedById: str = None
    dateLastUpdated: str = None
    isPublic: bool = True

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

    def dict(self) -> dict:
        """
        Create a dictionary from the Asset dataclass
        :return: Dictionary of Asset
        :rtype: dict
        """
        return {k: v for k, v in asdict(self).items()}
