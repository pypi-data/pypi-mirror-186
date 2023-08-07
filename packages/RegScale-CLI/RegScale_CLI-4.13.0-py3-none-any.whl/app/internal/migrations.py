#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Performs data processing for bulk processing"""

# standard python imports
from os import sep
from typing import Tuple

import click

from app.api import Api
from app.application import Application
from app.logz import create_logger
from app.utils.app_utils import (
    check_file_path,
    create_progress_object,
    error_and_exit,
    save_data_to,
)
from app.utils.regscale_utils import get_all_from_module
from app.utils.threadhandler import create_threads, thread_assignment

logger = create_logger()
job_progress = create_progress_object()
process_counter = []


@click.group()
def migrations():
    """Performs data processing for legacy data to migrate data formats or perform bulk processing."""


@migrations.command(name="issue_linker")
def issue_linker():
    """Provides linkage to the lineage of the issue (deep links to parent records in the tree)."""
    module = "issues"

    api, regscale_issues = initialize_and_fetch_data(module)

    with job_progress:
        # create task to process issues
        processing_issues = job_progress.add_task(
            f"[#f8b737]Analyzing {len(regscale_issues)} RegScale issue(s)...",
            total=len(regscale_issues),
        )

        # create threads to process the issues
        create_threads(
            process=process_data,
            args=(api, regscale_issues, module, processing_issues),
            thread_count=len(regscale_issues),
        )

        # notify user of outcome
        logger.info(
            "%s/%s %s processed from RegScale.",
            len(process_counter),
            len(regscale_issues),
            module.title(),
        )


@migrations.command(name="assessment_linker")
def assessment_linker():
    """Provides linkage to the lineage of the assessment (deep links to parent records in the tree)."""
    module = "assessments"

    api, regscale_assessments = initialize_and_fetch_data(module)

    with job_progress:
        # create task to process issues
        processing_issues = job_progress.add_task(
            f"[#f8b737]Analyzing {len(regscale_assessments)} RegScale issue(s)...",
            total=len(regscale_assessments),
        )

        # create threads to process the issues
        create_threads(
            process=process_data,
            args=(api, regscale_assessments, module, processing_issues),
            thread_count=len(regscale_assessments),
        )

        # notify user of outcome
        logger.info(
            "%s/%s %s processed from RegScale.",
            len(process_counter),
            len(regscale_assessments),
            module.title(),
        )


@migrations.command(name="risk_linker")
def risk_linker():
    """Provides linkage to the lineage of the risk (deep links to parent records in the tree)."""
    module = "risks"

    api, regscale_risks = initialize_and_fetch_data(module)

    with job_progress:
        # create task to process issues
        processing_issues = job_progress.add_task(
            f"[#f8b737]Analyzing {len(regscale_risks)} RegScale issue(s)...",
            total=len(regscale_risks),
        )

        # create threads to process the issues
        create_threads(
            process=process_data,
            args=(api, regscale_risks, module, processing_issues),
            thread_count=len(regscale_risks),
        )

        # notify user of outcome
        logger.info(
            "%s/%s %s processed from RegScale.",
            len(process_counter),
            len(regscale_risks),
            module.title(),
        )


def initialize_and_fetch_data(module: str) -> Tuple[Api, list[dict]]:
    """
    Function to start application, api, and fetches all records for the provided module
    from RegScale via API and saves the output to a .json file
    :param str module: python module
    :raises: General Error if token or domain are missing or blank in init.yaml
    :return: Tuple[Api object, list of data of provided module from RegScale API]
    :rtype: Tuple[Api, list[dict]]
    """
    # load the config from YAML
    app = Application()
    api = Api(app)
    config = app.load_config()

    # make sure config is set before processing
    if config["domain"] is None:
        error_and_exit("No domain set in the initialization file.")
    elif config["domain"] == "":
        error_and_exit("The domain is blank in the initialization file.")
    elif config["token"] is None:
        error_and_exit("The token has not been set in the initialization file.")
    elif config["token"] == "":
        error_and_exit("The token is blank in the initialization file.")
    else:
        # get the data of provided module from RegScale via API
        regscale_data = get_all_from_module(api=api, module=module)

        # verify artifacts folder exists
        check_file_path("artifacts")

        # write out risks data to file
        save_data_to(
            file_name=f"artifacts{sep}RegScale{module.title()}",
            file_type=".json",
            data=regscale_data,
        )
        logger.info(
            "Writing out RegScale risk list to the artifacts folder (see RegScale%sList.json).",
            module.title(),
        )
        logger.info(
            "%s %s retrieved for processing from RegScale.", len(regscale_data), module
        )
        return api, regscale_data


def process_data(args: Tuple, thread: int) -> None:
    """
    Function to utilize threading and process the data from RegScale
    :param Tuple args: Tuple of args to use during the process
    :param int thread: Thread number of current thread
    :raises: General error if unable to retrieve data from RegScale API
    :return: None
    """
    # set up local variables from args passed
    api, regscale_data, module, task = args

    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(regscale_data))
    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the recommendation for the thread for later use in the function
        item = regscale_data[threads[i]]

        url_processor = (
            f'{api.config["domain"]}/api/{module}/processLineage{item["id"]}'
        )
        try:
            process_result = api.get(url_processor)
            logger.info(
                "Processing %s #: %s Result: %s",
                module[:-1].title(),
                item["id"],
                process_result.text,
            )
            process_counter.append(item)
        except Exception:
            logger.error("Unable to process Issue # %s.", item["id"])
        job_progress.update(task, advance=1)
