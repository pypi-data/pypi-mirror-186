#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Integrates Wiz.io into RegScale """

# standard python imports
import datetime
import json
from datetime import date
from json import JSONDecodeError
from os import sep
from typing import Tuple

import click
import requests
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

from app.api import Api
from app.logz import create_logger
from app.utils.app_utils import (
    check_file_path,
    check_license,
    create_progress_object,
    error_and_exit,
    save_data_to,
)
from app.utils.regscale_utils import verify_provided_module
from app.utils.threadhandler import create_threads, thread_assignment
from models.app_models.click import regscale_id, regscale_module
from models.integration_models.wiz import AssetType
from models.regscale_models.asset import Asset
from models.regscale_models.issue import Issue

# Private and global variables
logger = create_logger()
job_progress = create_progress_object()
new_assets = []
update_assets = []
close_issues = []
update_issues = []
new_issues = []
loop_count = []

AUTH0_URLS = [
    "https://auth.wiz.io/oauth/token",
    "https://auth0.gov.wiz.io/oauth/token",
    "https://auth0.test.wiz.io/oauth/token",
    "https://auth0.demo.wiz.io/oauth/token",
]
COGNITO_URLS = [
    "https://auth.app.wiz.io/oauth/token",
    "https://auth.gov.wiz.io/oauth/token",
    "https://auth.test.wiz.io/oauth/token",
    "https://auth.demo.wiz.io/oauth/token",
]

# Create group to handle Wiz.io integration
@click.group()
def wiz():
    """Integrates continuous monitoring data from Wiz.io."""


@wiz.command()
def authenticate():
    """Authenticate to Wiz."""
    app = check_license()
    api = Api(app)
    # Login with service account to retrieve a 24-hour access token that updates YAML file
    logger.info("Authenticating - Loading configuration from init.yaml file.")

    # load the config from YAML
    config = app.config

    # get secrets
    client_id = (
        config["wizClientId"]
        if "wizClientId" in config
        else error_and_exit("No Wiz Client ID provided in the init.yaml file.")
    )
    client_secret = (
        config["wizClientSecret"]
        if "wizClientSecret" in config
        else error_and_exit("No Wiz Client Secret provided in the init.yaml file.")
    )
    wiz_auth_url = (
        config["wizAuthUrl"]
        if "wizAuthUrl" in config
        else error_and_exit("No Wiz Authentication URL provided in the init.yaml file.")
    )

    # login and get token
    logger.info("Attempting to retrieve OAuth token from Wiz.io.")
    token, scope = get_token(
        api=api,
        client_id=client_id,
        client_secret=client_secret,
        token_url=wiz_auth_url,
    )

    # assign values
    config["wizAccessToken"] = f"Bearer {token}"
    config["wizScope"] = scope

    # save the changes back to init.yaml
    app.save_config(config)
    logger.info(
        "Access token written to init.yaml call to support future API calls. Token is good for 24 hours."
    )


def get_token(
    api: Api, client_id: str, client_secret: str, token_url: str
) -> Tuple[str, str]:
    """
    Function to authenticate with Wiz.io via API and returns a JWT and scope
    :param api: API object
    :param str client_id: Wiz client ID
    :param str client_secret: Wiz client secret
    :param str token_url: Wiz URL to get a token
    :raises: General exception if response failed or if toke or scope is missing from API response
    :return: Tuple[JWT, scope]
    :rtype: Tuple[str, str]
    """
    logger.info("Getting a token")
    response = api.post(
        url=token_url,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=generate_authentication_params(client_id, client_secret, token_url),
    )
    logger.debug(response.json())
    if response.status_code != requests.codes.ok:
        error_and_exit(
            f"Error authenticating to Wiz [{response.status_code}] - {response.text}."
        )
    response_json = response.json()
    token = response_json.get("access_token")
    scope = response_json.get("scope")
    if not token:
        error_and_exit(
            f'Could not retrieve token from Wiz: {response_json.get("message")}.'
        )
    if not scope:
        error_and_exit("Could not retrieve scope from Wiz.")
    logger.info("SUCCESS: Wiz.io access token successfully retrieved.")
    return token, scope


def generate_authentication_params(
    client_id: str, client_secret: str, token_url: str
) -> dict:
    """
    Function to create the Correct Parameter format based on URL
    :param str client_id: Wiz.io client ID
    :param str client_secret: Wiz.io client secret
    :param str token_url: URL to get a token from Wiz.io
    :raises: General exception if token_url is invalid
    :return: Dictionary of authentication parameters for API call to Wiz.io
    :rtype: dict
    """
    if token_url in AUTH0_URLS:
        return {
            "grant_type": "client_credentials",
            "audience": "beyond-api",
            "client_id": client_id,
            "client_secret": client_secret,
        }
    elif token_url in COGNITO_URLS:
        return {
            "grant_type": "client_credentials",
            "audience": "wiz-api",
            "client_id": client_id,
            "client_secret": client_secret,
        }
    else:
        error_and_exit("Invalid Token URL")


@wiz.command()
@regscale_id()
@regscale_module()
# flake8: noqa: C901
def inventory(regscale_id: int, regscale_module: str):
    """Process inventory list from Wiz."""
    app = check_license()
    api = Api(app)
    # load the config from YAML
    config = app.config

    # see if provided RegScale Module is an accepted option
    verify_provided_module(regscale_module)

    # get secrets
    url = config["wizUrl"]
    token = config["wizAccessToken"]

    # set health check URL
    url_assets = (
        config["domain"]
        + "/api/assets/getAllByParent/"
        + str(regscale_id)
        + "/"
        + str(regscale_module)
    )

    # get the full list of assets
    logger.info("Fetching full asset list from RegScale.")
    try:
        asset_response = api.get(url=url_assets)
        if asset_response.status_code != 204:
            asset_data = asset_response.json()
            logger.info("%s total asset(s) retrieved from RegScale.", len(asset_data))
        else:
            asset_data = None
    except JSONDecodeError as e:
        error_and_exit(f"Unable to retrieve asset list from RegScale.\n{e}")
    # check if artifacts directory exists
    check_file_path("artifacts")

    # output the results of the Wiz assets
    save_data_to(
        file_name=f"artifacts{sep}RegScaleAssets", file_type=".json", data=asset_data
    )
    # The GraphQL query that defines which data you wish to fetch.
    query = gql(
        """
  query GraphSearch(
      $query: GraphEntityQueryInput
      $controlId: ID
      $projectId: String!
      $first: Int
      $after: String
      $fetchTotalCount: Boolean!
      $quick: Boolean
      $fetchPublicExposurePaths: Boolean = false
      $fetchInternalExposurePaths: Boolean = false
      $fetchIssueAnalytics: Boolean = false
    ) {
      graphSearch(
        query: $query
        controlId: $controlId
        projectId: $projectId
        first: $first
        after: $after
        quick: $quick
      ) {
        totalCount @include(if: $fetchTotalCount)
        maxCountReached @include(if: $fetchTotalCount)
        pageInfo {
          endCursor
          hasNextPage
        }
        nodes {
          entities {
            id
            name
            type
            properties
            hasOriginalObject
            userMetadata {
              isInWatchlist
              isIgnored
              note
            }
            technologies {
              id
              icon
            }
            issueAnalytics: issues(filterBy: { status: [IN_PROGRESS, OPEN] })
              @include(if: $fetchIssueAnalytics) {
              lowSeverityCount
              mediumSeverityCount
              highSeverityCount
              criticalSeverityCount
            }
            publicExposures(first: 10) @include(if: $fetchPublicExposurePaths) {
              nodes {
                ...NetworkExposureFragment
              }
            }
            otherSubscriptionExposures(first: 10)
              @include(if: $fetchInternalExposurePaths) {
              nodes {
                ...NetworkExposureFragment
              }
            }
            otherVnetExposures(first: 10)
              @include(if: $fetchInternalExposurePaths) {
              nodes {
                ...NetworkExposureFragment
              }
            }
          }
          aggregateCount
        }
      }
    }

    fragment NetworkExposureFragment on NetworkExposure {
      id
      portRange
      sourceIpRange
      destinationIpRange
      path {
        id
        name
        type
        properties
        issueAnalytics: issues(filterBy: { status: [IN_PROGRESS, OPEN] })
          @include(if: $fetchIssueAnalytics) {
          lowSeverityCount
          mediumSeverityCount
          highSeverityCount
          criticalSeverityCount
        }
      }
    }
"""
    )

    # The variables sent along with the above query
    variables = {
        "fetchPublicExposurePaths": True,
        "fetchInternalExposurePaths": False,
        "fetchIssueAnalytics": False,
        "first": 50,
        "query": {
            "type": ["TECHNOLOGY"],
            "select": True,
            "relationships": [
                {
                    "type": [{"type": "HAS_TECH", "reverse": True}],
                    "with": {"type": ["ANY"], "select": True},
                }
            ],
        },
        "projectId": "*",
        "fetchTotalCount": False,
        "quick": False,
        "after": "100",
    }
    # initialize client for Wiz.io
    transport = AIOHTTPTransport(url=url, headers={"Authorization": token})
    client = Client(
        transport=transport, fetch_schema_from_transport=True, execute_timeout=55
    )
    # loop through until all records have been fetched
    records_fetched = 1
    assets = {}
    while records_fetched > 0:
        # fetch all assets from Wiz
        try:
            wiz_assets = client.execute(query, variable_values=variables)
            logger.info("Wiz Fetch #%s completed.", records_fetched)
        except Exception:
            # error - unable to retrieve Wiz assets
            error_and_exit(
                "Unable to fetch Wiz assets.  Ensure access token is valid and correct Wiz API endpoint was provided."
            )
        if records_fetched == 1:
            # initialize the object
            assets = wiz_assets
        else:
            # append any new records
            assets["graphSearch"]["nodes"].extend(wiz_assets["graphSearch"]["nodes"])
        # get page info
        page_info = wiz_assets["graphSearch"]["pageInfo"]

        # Check if there are additional results
        if page_info["hasNextPage"]:
            # Update variables to fetch the next batch of items
            variables["after"] = page_info["endCursor"]
            # update loop cursor
            records_fetched += 1
        else:
            # No additional results. End the loop/
            records_fetched = 0
    # output the results of the Wiz assets
    save_data_to(file_name=f"artifacts{sep}wizAssets", file_type=".json", data=assets)
    logger.info(
        "%s assets retrieved for processing from Wiz.io.",
        len(assets["graphSearch"]["nodes"]),
    )
    # get the Wiz nodes to process
    processing = assets["graphSearch"]["nodes"]

    with job_progress:
        # create task of analyzing results
        analyzing_results = job_progress.add_task(
            f"[#f8b737]Analyzing {len(processing)} Wiz asset(s)...",
            total=len(processing),
        )
        # create threads to analyze results
        create_threads(
            process=analyze_wiz_assets,
            args=(
                processing,
                asset_data,
                regscale_id,
                regscale_module,
                config,
                analyzing_results,
            ),
            thread_count=len(processing),
        )
        # output the results of the Wiz assets
        save_data_to(
            file_name=f"artifacts{sep}wizNewAssets", file_type=".json", data=new_assets
        )
        # output the results of the Wiz assets
        save_data_to(
            file_name=f"artifacts{sep}wizUpdateAssets",
            file_type=".json",
            data=update_assets,
        )
        # create threads to create new assets in RegScale if needed
        if len(new_assets) > 0:
            logger.info(
                "%s new asset(s) processed and ready for upload into RegScale.",
                len(new_assets),
            )
            # create task for creating RegScale assets
            creating_assets = job_progress.add_task(
                f"[#ef5d23]Creating {len(new_assets)} new asset(s) in RegScale...",
                total=len(new_assets),
            )
            # start threads to create assets in RegScale
            create_threads(
                process=create_assets,
                args=(
                    new_assets,
                    config["maxThreads"],
                    api,
                    f'{config["domain"]}/api/assets/',
                    creating_assets,
                ),
                thread_count=len(new_assets),
            )
        else:
            logger.info("All Wiz asset(s) already exist in RegScale.")
        # create threads to update assets in RegScale if needed
        if len(update_assets) > 0:
            logger.info(
                "%s existing asset(s) processed and ready to update in RegScale.",
                len(update_assets),
            )
            # create task for creating RegScale assets
            updating_assets = job_progress.add_task(
                f"[#21a5bb]Updating {len(update_assets)} asset(s) in RegScale...",
                total=len(update_assets),
            )

            # start threads to create assets in RegScale
            create_threads(
                process=update_existing_assets,
                args=(update_assets, api, config, updating_assets),
                thread_count=len(update_assets),
            )
        else:
            logger.info("No RegScale asset(s) needed to be updated.")


@wiz.command()
@regscale_id()
@regscale_module()
# flake8: noqa: C901
def issues(regscale_id: int, regscale_module: str):
    """Process issues from Wiz"""
    app = check_license()
    api = Api(app)

    # load the config from YAML
    config = app.config

    # see if provided RegScale Module is an accepted option
    verify_provided_module(regscale_module)

    # get secrets
    url = config["wizUrl"]
    token = config["wizAccessToken"]
    str_user = config["userId"]

    # set url
    url_issues = (
        config["domain"]
        + "/api/issues/getAllByParent/"
        + str(regscale_id)
        + "/"
        + str(regscale_module).lower()
    )
    # get the existing issues for the parent record that are already in RegScale
    logger.info("Fetching full issue list from RegScale.")
    issue_response = api.get(url=url_issues)
    # check for null/not found response
    if issue_response.status_code == 204:
        logger.warning("No existing issues for this RegScale record.")
        issues_data = []
    else:
        try:
            issues_data = issue_response.json()
        except JSONDecodeError:
            error_and_exit("Unable to fetch issues from RegScale.")
    # make directory if it doesn't exist
    check_file_path("artifacts")

    # write out issues data to file
    save_data_to(
        file_name=f"artifacts{sep}existingRecordIssues",
        file_type=".json",
        data=issues_data,
    )
    logger.info(
        "Writing out RegScale issue list for Record # %s to the artifacts folder (see existingRecordIssues.json).",
        regscale_id,
    )
    logger.info(
        "%s existing issue(s) retrieved for processing from RegScale.", len(issues_data)
    )

    # The GraphQL query that defines which data you wish to fetch.
    query = gql(
        """
    query IssuesTable($filterBy: IssueFilters, $first: Int, $after: String, $orderBy: IssueOrder) {
        issues(filterBy: $filterBy, first: $first, after: $after, orderBy: $orderBy) {
        nodes {
            ...IssueDetails
        }
        pageInfo {
            hasNextPage
            endCursor
        }
        totalCount
        informationalSeverityCount
        lowSeverityCount
        mediumSeverityCount
        highSeverityCount
        criticalSeverityCount
        uniqueEntityCount
        }
    }

        fragment IssueDetails on Issue {
        id
        control {
        id
        name
        query
        securitySubCategories {
          id
          externalId
          title
          description
          category {
            id
            externalId
            name
            framework {
              id
              name
            }
          }
        }
        }
        createdAt
        updatedAt
        projects {
        id
        name
        businessUnit
        riskProfile {
            businessImpact
        }
        }
        status
        severity
        entity {
        id
        name
        type
        }
        entitySnapshot {
        id
        type
        name
        }
        note
        serviceTicket {
        externalId
        name
        url
        }
    }
    """
    )

    # The variables sent along with the above query
    variables = {
        "first": 25,
        "filterBy": {"status": ["OPEN", "IN_PROGRESS"]},
        "orderBy": {"field": "SEVERITY", "direction": "DESC"},
    }

    # fetch the list of issues
    transport = AIOHTTPTransport(url=url, headers={"Authorization": token})
    client = Client(
        transport=transport, fetch_schema_from_transport=True, execute_timeout=55
    )
    # loop through until all records have been fetched
    fetched_count = 1
    issues = {}
    while fetched_count > 0:
        # Fetch the query!
        try:
            wiz_issues = client.execute(query, variable_values=variables)
        except Exception:
            # error - unable to retrieve Wiz issues
            error_and_exit(
                "Unable to fetch Wiz issues. Ensure access token is valid and correct Wiz API endpoint was provided."
            )
        if fetched_count == 1:
            # initialize the object
            issues = wiz_issues
        else:
            # append any new records
            issues["issues"]["nodes"].extend(wiz_issues["issues"]["nodes"])
        # get page info
        page_info = wiz_issues["issues"]["pageInfo"]

        # Check if there are additional results
        if page_info["hasNextPage"]:
            # Update variables to fetch the next batch of items
            variables["after"] = page_info["endCursor"]
            # update loop cursor
            fetched_count += 1
        else:
            # No additional results. End the loop/
            fetched_count = 0
    # output the results of the Wiz issues
    save_data_to(file_name=f"artifacts{sep}wizIssues", file_type=".json", data=issues)

    # save the issues into a variable
    wiz_issues = issues["issues"]["nodes"]
    logger.info(
        "%s issue(s) retrieved for processing from Wiz.io.",
        len(wiz_issues),
    )
    with job_progress:
        # create task of analyzing issues
        analyzing_issues = job_progress.add_task(
            f"[#f8b737]Analyzing {len(wiz_issues)} Wiz issue(s)...",
            total=len(wiz_issues),
        )
        # create threads to analyze issues
        create_threads(
            process=analyze_wiz_issues,
            args=(
                wiz_issues,
                issues_data,
                config,
                regscale_id,
                regscale_module,
                analyzing_issues,
            ),
            thread_count=len(wiz_issues),
        )
        # Warn that processing is beginning
        logger.warning("PRE-PROCESSING COMPLETE: Batch updates beginning.....")
        global loop_count
        # create threads to compare Wiz issues and RegScale issues
        if len(issues_data) > 0:
            logger.info(
                "Comparing Wiz issue(s) and %s issue(s) in RegScale.",
                len(new_issues),
            )
            # reset loop_count list
            loop_count = []
            # create task for comparing Wiz and RegScale issues
            comparing_issues = job_progress.add_task(
                f"[#ef5d23]Comparing Wiz issue(s) and {len(issues_data)} issue(s) in RegScale...",
                total=len(issues_data),
            )
            # start threads to create assets in RegScale
            create_threads(
                process=compare_wiz_and_regscale_issues,
                args=(
                    wiz_issues,
                    issues_data,
                    config["maxThreads"],
                    comparing_issues,
                ),
                thread_count=len(issues_data),
            )
        else:
            logger.info("No issues in RegScale to compare against Wiz issues.")
        # see if new issues need to be created in RegScale
        if len(new_issues) > 0:
            # reset loop_count list
            loop_count = []
            logger.info(
                "%s issue(s) ready to be created in RegScale.",
                len(new_issues),
            )
            # create process of updating RegScale issues
            creating_issues = job_progress.add_task(
                f"[#21a5bb]Creating {len(new_issues)} issue(s) in RegScale...",
                total=len(new_issues),
            )
            # create threads to update RegScale issues with new Wiz information
            create_threads(
                process=create_regscale_issues,
                args=(new_issues, config, api, creating_issues),
                thread_count=len(new_issues),
            )
            logger.warning(
                "%s/%s Wiz issue(s) were created in RegScale.",
                len(new_issues),
                len(loop_count),
            )
            # output the result to artifacts folder
            save_data_to(
                file_name=f"artifacts{sep}regScaleNewIssues",
                file_type=".json",
                data=new_issues,
            )
        else:
            logger.info("All Wiz issue(s) already exist in RegScale.")
        if len(update_issues) > 0:
            # reset loop_count list
            loop_count = []
            logger.info(
                "%s issue(s) ready for updating in RegScale.",
                len(update_issues),
            )
            # create process of updating RegScale issues
            updating_issues = job_progress.add_task(
                f"[#0866b4]Updating {len(update_issues)} issue(s) in RegScale...",
                total=len(update_issues),
            )
            # create threads to update RegScale issues with new Wiz information
            create_threads(
                process=update_regscale_issues,
                args=(update_issues, config, api, updating_issues),
                thread_count=len(update_issues),
            )
            logger.warning(
                "%s/%s Wiz issue(s) were updated in RegScale.",
                len(update_issues),
                len(loop_count),
            )
            # output the result to artifacts folder
            save_data_to(
                file_name=f"artifacts{sep}regScaleUpdateIssues",
                file_type=".json",
                data=update_issues,
            )
        else:
            logger.info("All Wiz issue(s) are current in RegScale.")
        # see if any issues need to be closed in RegScale
        if len(close_issues) > 0:
            # reset loop_count list
            loop_count = []
            logger.info(
                "%s issue(s) ready to be closed in RegScale.",
                len(close_issues),
            )
            # create process of updating RegScale issues
            closing_issues = job_progress.add_task(
                f"[green]Closing {len(close_issues)} issue(s) in RegScale...",
                total=len(close_issues),
            )
            # create threads to update RegScale issues with new Wiz information
            create_threads(
                process=update_regscale_issues,
                args=(update_issues, config, api, closing_issues),
                thread_count=len(close_issues),
            )
            logger.warning(
                "%s/%s Wiz issue(s) were closed in RegScale.",
                len(close_issues),
                len(loop_count),
            )
            # output the result to artifacts folder
            save_data_to(
                file_name=f"artifacts{sep}regScaleCloseIssues",
                file_type=".json",
                data=close_issues,
            )
        else:
            logger.info("No Wiz issue(s) need to be closed in RegScale.")


@wiz.command()
def threats():
    """Process threats from Wiz."""
    check_license()
    logger.info("Threats - COMING SOON")


@wiz.command()
def vulnerabilities():
    """Process vulnerabilities from Wiz."""
    check_license()
    logger.info("Vulnerabilities - COMING SOON")


def map_category(asset_string: str) -> str:
    """
    Maps Wiz.io asset and returns asset category as a string
    :param str asset_string: Asset string from Wiz
    :raises: General exception
    :return: String of asset category
    :rtype: str
    """
    try:
        return getattr(AssetType, asset_string).value
    except Exception as ex:
        logger.warning("Unable to find %s in AssetType enum.\n", ex)
    # Default to Software, if there is an exception
    return "Software"


def analyze_wiz_assets(args: Tuple, thread: int) -> None:
    """
    Function to allow threads to analyze the results from Wiz.io
    :param Tuple args: Tuple of args to use during the process
    :param int thread: Thread number of current thread
    :return: None
    """
    # get variables from args Tuple
    assets, asset_data, regscale_id, regscale_module, config, task = args

    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(assets))
    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the node for the thread for later use in the function
        node = assets[threads[i]]

        # ignore built-in service principals
        if node["entities"][0]["name"] not in config["wizExcludes"]:
            # add node to loop_count for a counter
            loop_count.append(node)
            logger.info(
                "%s) %s: %s",
                len(loop_count),
                node["entities"][1]["type"],
                node["entities"][1]["name"],
            )
            # get the Wiz ID
            wiz_id = node["entities"][1]["id"]

            # see if it already exists
            found_flag = False
            update_asset = None
            for asset in asset_data:
                if asset.get("wizId") == wiz_id:
                    found_flag = True
                    update_asset = asset
                    break
            # get the Wiz metadata
            metadata = json.dumps(node["entities"])

            # see if a new record or already exists
            if found_flag:
                # verify the asset needs to be updated
                verify_asset_update_needed(
                    node=node,
                    update_asset=update_asset,
                    metadata=metadata,
                    user_id=config["userId"],
                )
            else:
                # create a new asset
                new_asset = Asset(
                    name=node["entities"][1]["name"],
                    assetOwnerId=config["userId"],
                    assetType=node["entities"][1]["type"],
                    status="Active (On Network)",
                    wizId=wiz_id,
                    wizInfo=metadata,
                    parentId=regscale_id,
                    parentModule=regscale_module,
                    createdById=config["userId"],
                    lastUpdatedById=config["userId"],
                )
                new_asset["assetCategory"] = map_category(node["entities"][1]["type"])
                new_assets.append(new_asset.dict())
        # update progress bar
        job_progress.update(task, advance=1)


def create_assets(args: Tuple, thread: int) -> None:
    """
    Function to create assets in RegScale using threads
    :param Tuple args: Tuple of args to use during the process
    :param int thread: Thread number of current thread
    :raises: JSONDecodeError if API response cannot be converted to a json object
    :return: None
    """
    # set up variables from args Tuple
    new_regscale_assets, max_threads, api, url_create_asset, task = args

    # update api pool limits to max_thread count from init.yaml
    api.pool_connections = max_threads
    api.pool_maxsize = max_threads

    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(new_assets))

    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the new_asset for the thread for later use in the function
        new_asset = new_regscale_assets[threads[i]]
        try:
            asset_upload = api.post(url=url_create_asset, json=new_asset)
            asset_upload_response = asset_upload.json()
            # output the result
            logger.info(
                "Success: New asset created in RegScale # %s for Wiz Asset: %s.",
                asset_upload_response["id"],
                asset_upload_response["name"],
            )
        except JSONDecodeError:
            error_and_exit(
                f"Unable to create asset: {new_asset['otherTrackingNumber']}"
            )
        # update progress bar
        job_progress.update(task, advance=1)


def update_existing_assets(args: Tuple, thread: int) -> None:
    """
    function to update existing assets in RegScale while using threads
    :param Tuple args: Tuple of args to use during the process
    :param int thread: Thread number of current thread
    :raises: JSONDecodeError if API response cannot be converted to a json object
    :return: None
    """
    # set up local variables from args passed
    update_regscale_assets, api, config, task = args

    # update api pool limits to maxThread count from init.yaml
    api.pool_connections = config["maxThreads"]
    api.pool_maxsize = config["maxThreads"]

    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(update_assets))
    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the recommendation for the thread for later use in the function
        asset = update_regscale_assets[threads[i]]

        # set url for update
        url_update_asset = f'{config["domain"]}/api/assets/{asset["id"]}'
        try:
            asset_upload = api.put(url_update_asset, json=asset)
            asset_upload_response = asset_upload.json()
            # output the result
            logger.info(
                "Success: Asset updated in RegScale # %s for Wiz Asset: %s.",
                asset_upload_response["id"],
                asset_upload_response["name"],
            )
        except JSONDecodeError:
            logger.debug(asset["assetCategory"])
            error_and_exit(f"Unable to update asset: {asset['wizId']}.")
        # update progress bar
        job_progress.update(task, advance=1)


def verify_asset_update_needed(
    node: dict, update_asset: dict, metadata: str, user_id: str
) -> None:
    """
    Function to verify asset needs to be updated in RegScale
    :param dict node: original dict for comparison
    :param dict update_asset: dict to compare against node
    :param  str metadata: string of the metadata
    :param  str user_id: RegScale user ID string
    :return: None
    """
    update_needed = False
    if update_asset["name"] != node["entities"][1]["name"]:
        update_asset["name"] = node["entities"][1]["name"]
        update_needed = True
    if update_asset["assetType"] != node["entities"][1]["type"]:
        update_asset["assetType"] = node["entities"][1]["type"]
        update_needed = True
    if update_asset["lastUpdatedById"] != user_id:
        update_asset["wizInfo"] = metadata
        update_needed = True
    if update_asset["assetCategory"] != map_category(node["entities"][1]["type"]):
        update_asset["assetCategory"] = map_category(node["entities"][1]["type"])
        update_needed = True
    if update_needed:
        update_assets.append(update_asset)


def analyze_wiz_issues(args: Tuple, thread: int) -> None:
    """
    function to analyze issues from wiz using threads
    :param Tuple args: Tuple of args to use during the process
    :param int thread: Thread number of current thread
    :return: None
    """
    # set up local variables from the passed args
    wiz_issues, issues_data, config, regscale_id, regscale_module, task = args

    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(wiz_issues))
    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the issue for the thread for later use in the function
        issue = wiz_issues[threads[i]]
        # default to Not Found
        found_flag = False

        # see if this issue already exists in RegScale
        for exists in issues_data:
            if exists.get("wizId") == issue["id"]:
                found_flag = True
                # capture the existing record
                issue_found = exists
                break

        # pre-process metadata
        title = f'{issue["entity"]["name"]} - {issue["control"]["name"]}'
        description = (
            "<strong>Wiz Control ID: </strong>"
            + issue["control"]["id"]
            + f'<br/><strong>Asset Type: </strong>{issue["entity"]["type"]}'
            + f'<br/><strong>Severity: </strong>{issue["severity"]}'
            + f'<br/><strong>Date First Seen: </strong>{issue["createdAt"]}'
            + f'<br/><strong>Date Last Seen: </strong>{issue["updatedAt"]}'
        )

        # process subcategories for security frameworks
        categories = issue["control"]["securitySubCategories"]
        table = "<table><tr><td>Control ID</td><td>Category/Family</td><td>Framework</td><td>Description</td></tr>"
        for cat in categories:
            table += (
                f'<tr><td>{cat["externalId"]}</td><td>{cat["category"]["name"]}</td>'
                + f'<td>{cat["category"]["framework"]["name"]}</td><td>{cat["description"]}</td></tr></table>'
            )
        # get today's date as a baseline
        today_date = date.today().strftime("%m/%d/%y")

        # handle status and due date
        if issue["severity"] == "LOW":
            days = config["issues"]["wiz"]["low"]
            severity = "III - Low - Other Weakness"
            due_date = datetime.datetime.strptime(
                today_date, "%m/%d/%y"
            ) + datetime.timedelta(days=days)
        elif issue["severity"] == "MEDIUM":
            days = config["issues"]["wiz"]["medium"]
            severity = "II - Moderate - Reportable Condition"
            due_date = datetime.datetime.strptime(
                today_date, "%m/%d/%y"
            ) + datetime.timedelta(days=days)
        elif issue["severity"] == "HIGH":
            days = config["issues"]["wiz"]["high"]
            severity = "II - Moderate - Reportable Condition"
            due_date = datetime.datetime.strptime(
                today_date, "%m/%d/%y"
            ) + datetime.timedelta(days=days)
        elif issue["severity"] == "CRITICAL":
            days = config["issues"]["wiz"]["critical"]
            severity = "I - High - Significant Deficiency"
            due_date = datetime.datetime.strptime(
                today_date, "%m/%d/%y"
            ) + datetime.timedelta(days=days)
        else:
            error_and_exit("Unknown Wiz severity level: %s.", issue["severity"])

        # handle parent assignments for deep linking
        security_plan_id = regscale_id if regscale_module == "securityplans" else 0
        project_id = regscale_id if regscale_module == "projects" else 0
        supply_chain_id = regscale_id if regscale_module == "supplychain" else 0
        component_id = regscale_id if regscale_module == "components" else 0

        # process based on whether found or not
        if found_flag:
            # update existing record
            logger.info(
                "RegScale Issue #%s already exists for %s. Queuing for update.",
                issue_found["id"],
                issue_found["wizId"],
            )
            # update the description
            issue_found["description"] = description + "<br/><br/>" + table
            # add to the update list
            update_issues.append(issue_found)
        else:
            # process new record
            new_issue = Issue(
                uuid=issue["entity"]["id"],
                title=title,
                dateCreated=issue["createdAt"],
                description=description + "<br/><br/>" + table,
                severityLevel=severity,
                issueOwnerId=config["userId"],
                dueDate=str(due_date),
                identification="Security Control Assessment",
                status=config["issues"]["wiz"]["status"],
                securityPlanId=security_plan_id,
                projectId=project_id,
                supplyChainId=supply_chain_id,
                componentId=component_id,
                wizId=issue["id"],
                parentId=regscale_id,
                parentModule=regscale_module,
                createdById=config["userId"],
                lastUpdatedById=config["userId"],
                dateLastUpdated=issue["updatedAt"],
            )
            # add the issue dictionary to the processing list
            new_issues.append(new_issue.dict())
        # update progress bar
        job_progress.update(task, advance=1)


def compare_wiz_and_regscale_issues(args: Tuple, thread: int) -> None:
    """
    Function to compare Wiz issues and RegScale Issues
    :param Tuple args: Tuple of args to use during the process
    :param int thread: Thread number of current thread
    :return: None
    """
    # set up local variables from the passed args
    wiz_issues, issues_data, max_threads, task = args

    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(issues_data))
    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the issue for the thread for later use in the function
        issue = issues_data[threads[i]]
        # see if any issues are open in RegScale that have been closed in Wiz (in RegScale but not in Wiz)
        # only process open issues
        if issue["status"] == "Open":
            # default to close unless found
            close_flag = True
            # loop through each Wiz issue and look for a match
            for wiz_issue in wiz_issues:
                if issue["wizId"] == wiz_issue["id"]:
                    # still open in Wiz
                    close_flag = False
                    break
            # if not found, close it
            if close_flag:
                # set closed status
                issue["Status"] = "Closed"
                issue["DateCompleted"] = datetime.date.today().strftime("%m/%d/%Y")
                # append to close_issues list
                close_issues.append(issue)
        # update progress bar
        job_progress.update(task, advance=1)


def create_regscale_issues(args: Tuple, thread: int) -> None:
    """
    Function to create new issues in RegScale using Wiz issues using threads
    :param Tuple args: Tuple of args to use during the process
    :param int thread: Thread number of current thread
    :raises: JSONDecodeError if API response cannot be converted to a json object
    :return: None
    """
    # set up local variables from the passed args
    regscale_issues, config, api, task = args

    # load each new Wiz issue into RegScale
    url_create_issue = config["domain"] + "/api/issues"

    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(regscale_issues))

    # update api pool limits to max_thread count from init.yaml
    api.pool_connections = config["maxThreads"]
    api.pool_maxsize = config["maxThreads"]

    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the issue for the thread for later use in the function
        issue = regscale_issues[threads[i]]
        try:
            issue_upload = api.post(url=url_create_issue, json=issue)
            issue_upload_response = issue_upload.json()
            # output the result
            logger.info(
                "Success: New RegScale Issue # %s loaded for Wiz ID #%s.",
                issue_upload_response["id"],
                issue_upload_response["wizId"],
            )
            loop_count.append(issue)
        except JSONDecodeError:
            error_and_exit(f"Unable to create {issue}.")
        # update progress bar
        job_progress.update(task, advance=1)


def update_regscale_issues(args: Tuple, thread: int) -> None:
    """
    Function to upload RegScale issues with the new Wiz information using threads
    :param Tuple args: Tuple of args to use during the process
    :param int thread: Thread number of current thread
    :raises: JSONDecodeError if API response cannot be converted to a json object
    :return: None
    """
    # set up local variables from the passed args
    regscale_issues, config, api, task = args

    # update each existing Wiz issue in RegScale
    url_update_issue = f"{config['domain']}/api/issues/"

    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(regscale_issues))
    # update api pool limits to max_thread count from init.yaml
    api.pool_connections = config["maxThreads"]
    api.pool_maxsize = config["maxThreads"]

    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the issue for the thread for later use in the function
        issue = regscale_issues[threads[i]]
        try:
            issue_upload = api.put(url=f"{url_update_issue}{issue['id']}", json=issue)
            issue_upload_response = issue_upload.json()
            # output the result
            logger.info(
                "Success: Issue update for RegScale # %s loaded for Wiz ID #%s.",
                issue_upload_response["id"],
                issue_upload_response["wizId"],
            )
            loop_count.append(issue)
        except JSONDecodeError:
            error_and_exit(f"Unable to update {issue['id']}.")
        # update progress bar
        job_progress.update(task, advance=1)


def close_regscale_issues(args: Tuple, thread: int) -> None:
    """
    Function to close issues in RegScale for closed Wiz issues using threads
    :param Tuple args: Tuple of args to use during the process
    :param int thread: Thread number of current thread
    :raises: JSONDecodeError if API response cannot be converted to a json object
    :return: None
    """
    # set up local variables from the passed args
    regscale_issues, config, api, task = args

    # set url to close RegScale issues
    url_close_issue = config["domain"] + "/api/issues/"

    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(regscale_issues))
    # update api pool limits to max_thread count from init.yaml
    api.pool_connections = config["maxThreads"]
    api.pool_maxsize = config["maxThreads"]

    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the issue for the thread for later use in the function
        issue = regscale_issues[threads[i]]
        try:
            issue_upload = api.put(
                url=f"{url_close_issue}{issue['id']}",
                json=issue,
            )
            issue_upload_response = issue_upload.json()
            # output the result
            logger.info(
                "Success: Closed RegScale Issue # %s; Wiz ID #%s.",
                issue_upload_response["id"],
                issue_upload_response["wizId"],
            )
            loop_count.append(issue)
        except JSONDecodeError:
            error_and_exit(f"Unable to close Issue # {issue['id']}.")
        # update progress bar
        job_progress.update(task, advance=1)
