#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Dataclass for a RegScale Assessment """
from dataclasses import dataclass, asdict


@dataclass
class Assessment:
    """Assessment Model"""

    leadAssessorId: str  # Required field
    title: str  # Required field
    assessmentType: str  # Required field
    plannedStart: str  # Required field
    plannedFinish: str  # Required field
    status: str = "Scheduled"  # Required field
    assessmentResult: str = ""
    actualFinish: str = ""
    assessmentReport: str = None
    masterId: int = None
    complianceScore: float = None
    targets: str = None
    automationInfo: str = None
    automationId: str = None
    metadata: str = None
    assessmentPlan: str = None
    oscalsspId: int = None
    oscalComponentId: int = None
    controlId: int = None
    requirementId: int = None
    securityPlanId: int = None
    projectId: int = None
    supplyChainId: int = None
    policyId: int = None
    componentId: int = None
    incidentId: int = None
    parentId: int = None
    parentModule: str = None
    createdById: str = None
    dateCreated: str = None
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
        Create a dictionary from the Assessment dataclass
        :return: Dictionary of Assessment
        :rtype: dict
        """
        return {k: v for k, v in asdict(self).items()}
