#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Integrates OSCAL into RegScale"""

# standard python imports
import dataclasses
import json
import tempfile
import uuid
from os import remove, sep
from pathlib import Path
from subprocess import CalledProcessError, run
from typing import Tuple

import click
import pandas as pd
import requests
import xmltodict
import yaml

from app.api import Api
from app.application import Application
from app.logz import create_logger
from app.utils.app_utils import (
    check_file_path,
    create_progress_object,
    error_and_exit,
    save_data_to,
)
from app.utils.threadhandler import create_threads, thread_assignment
from models.regscale_models.components import Component
from models.regscale_models.control_implementation import ControlImplementation

# create global variables
job_progress = create_progress_object()
logger = create_logger()
app = Application()
config = app.config
oscal_cli_path = Path(config["oscalCliPath"])
api = Api(app)
controls, new_regscale_controls, errors, new_params, new_tests, new_objectives = (
    [],
    [],
    [],
    [],
    [],
    [],
)
loop_counter = {
    "controls": [],
    "child_controls": [],
    "tests": [],
    "objectives": [],
    "updates": [],
}


@click.group()
def oscal():
    """Performs bulk processing of OSCAL files."""


# OSCAL Version Support
@oscal.command()
def version():
    """Info on current OSCAL version supported by RegScale."""
    logger.info("RegScale currently supports OSCAL Version 1.0.")
    check_oscal()


def convert_oscal_comp_to_regscale(j_data: dict) -> None:
    """
    Convert OSCAL component dict into a Regscale Component
    :param dict j_data: OSCAL component
    :raises: KeyError if compenents key isn't found in j_data
    :raises: requests.exceptions.RequestException if unable to get data from OSCAL API
    :raises: KeyError if OSCAL data is missing title
    :return: None
    """
    component_id = None
    regscale_components = []
    components = []
    existing_components = api.get(
        url=config["domain"] + "/api/components/getList"
    ).json()
    controls_to_be_added = []
    j_data["component-definition"]["metadata"]
    try:
        components = j_data["component-definition"]["components"]
    except KeyError as kex:
        error_and_exit(f"Key Error! {kex}")

    for comp in components:
        control_implementations = comp["control-implementations"]
        base_catalog = ""
        try:
            base_catalog = api.get(
                url=comp["control-implementations"][0]["source"], headers={}
            ).json()["catalog"]["metadata"]["title"]
        except requests.exceptions.RequestException as rex:
            logger.error(rex)
        except KeyError as kex:
            logger.error(kex)
        component = Component(
            title=comp["title"],
            componentOwnerId=app.config["userId"],
            componentType=comp["type"].lower(),
            description=comp["description"],
            purpose=comp["purpose"],
        )
        regscale_components.append(dataclasses.asdict(component))
        for control_implements in control_implementations:
            for control_data in control_implements["implemented-requirements"]:
                d = {
                    "title": control_data["control-id"],
                    "description": control_data["description"],
                }
                controls_to_be_added.append(d)
    for reg in regscale_components:

        check_component = [x for x in existing_components if x["title"] == reg["title"]]
        if not check_component:
            r = api.post(url=f'{config["domain"]}/api/components/', json=reg)
            if not r.raise_for_status():
                component_id = r.json()["id"]
                logger.info("Successfully posted %s to RegScale.", reg["title"])
        else:
            for cmp in check_component:
                r = api.put(
                    url=f'{config["domain"]}/api/components/{cmp["id"]}', json=reg
                )
                if not r.raise_for_status():
                    component_id = cmp["id"]
                    # component_id = r.json()['id']
                    logger.info(
                        "Successfully updated component %s in RegScale.", cmp["title"]
                    )
    # Load controls to RegScale and associate with new component
    load_controls(
        controls_to_be_added=controls_to_be_added,
        component_id=component_id,
        base_catalog=base_catalog,
    )


@oscal.command(name="component")
@click.argument("file_name", type=click.Path(exists=True))
def upload_component(file_name: str) -> None:
    """Upload OSCAL Component to RegScale."""
    # Load Controls and assign to component
    process_component(file_name=file_name)


def load_controls(
    controls_to_be_added: dict, component_id: int, base_catalog: str
) -> None:
    """
    Load control implementations to RegScale
    :param dict controls_to_be_added: Controls to load from RegScale
    :param int component_id: Compenent ID from RegScale
    :param str base_catalog: base catalog to filter components
    :raises: requests.RequestException if unable to get data from RegSCale API
    :return: None
    """
    control_implementations_to_insert = []
    control_implementations_to_update = []
    try:
        imp_r = api.get(
            url=f'{config["domain"]}/api/controlImplementation/getAllByParent/{component_id}/components'
        )
        if not imp_r.raise_for_status():
            all_implementations = imp_r.json()
    except requests.RequestException as rex:
        logger.debug("No control implementations found for %s.", component_id)
        all_implementations = []
    cats = api.get(url=f'{config["domain"]}/api/catalogues/getList').json()
    cat = [cat for cat in cats if cat["title"] == base_catalog]

    if len(cat) > 0:
        cat_id = cat[0]["id"]
        try:
            controls = api.get(
                f'{config["domain"]}/api/SecurityControls/getList/{cat_id}'
            ).json()
        except requests.RequestException as rex:
            error_and_exit(rex)
        for imp_control in controls_to_be_added:
            try:
                reg_control = [
                    cntrl
                    for cntrl in controls
                    if cntrl["controlId"].lower() == imp_control["title"].lower()
                ]
                if len(reg_control) > 0:
                    control_implementation = ControlImplementation(
                        parentId=component_id,
                        parentModule="components",
                        controlOwnerId=config["userId"],
                        status="Fully Implemented",
                        controlID=reg_control[0]["id"],
                        implementation=imp_control["description"],
                    )
                    dat = dataclasses.asdict(control_implementation)
                    if control_implementation.implementation not in [
                        imp["implementation"]
                        for imp in all_implementations
                        if imp["implementation"]
                        == control_implementation.implementation
                    ]:
                        control_implementations_to_insert.append(dat)
                    else:
                        dat["id"] = [
                            imp["id"]
                            for imp in all_implementations
                            if imp["implementation"] == dat["implementation"]
                        ][0]
                        control_implementations_to_update.append(dat)
            except requests.RequestException as rex:
                logger.error(rex)
            except IndexError as iex:
                logger.error("Index Error: %s\n%s", dat, iex)
    logger.debug(control_implementations_to_insert)
    # Insert or update new control implementations
    if control_implementations_to_insert:
        api.update_server(
            method="post",
            url=f'{config["domain"]}/api/controlImplementation',
            message=f"Inserting {len(control_implementations_to_insert)} implementations...",
            json_list=control_implementations_to_insert,
        )
    if control_implementations_to_update:

        api.update_server(
            method="put",
            url=f'{config["domain"]}/api/controlImplementation',
            message=f"Updating {len(control_implementations_to_update)} implementations...",
            json_list=control_implementations_to_update,
        )


def process_component(file_name: str) -> None:
    """
    OSCAL Component to RegScale
    :param str file_name: File Name
    :raises: FileNotFoundError if provided file cannot be found
    :return: None
    """
    output_name = tempfile.gettempdir() + sep + "component.json"
    logger.debug(file_name)
    file_convert_json(file_name, output_name)
    try:
        json_d = open(output_name, "r").read()
    except FileNotFoundError:
        error_and_exit(f"File not found!\n{file_name}")
    convert_oscal_comp_to_regscale(j_data=json.loads(json_d))
    remove(output_name)


def file_convert_json(input: str, output: str) -> None:
    """
    Convert file from YML/XML to JSON
    :param str input: Path to the original file to convert
    :param str output: Desired path of the converted file
    :return: None
    """
    # Create object
    with open(input, "r") as file_in, open(output, "w") as file_out:
        if Path(input).suffix == ".xml":
            obj = xmltodict.parse((file_in.read()))
        if Path(input).suffix in [".yaml", ".yml"]:
            obj = yaml.safe_load(file_in.read())
        json.dump(obj, file_out)


# Convert OSCAL formatted catalog json file to OSCAL xml
@oscal.command(name="convert")
@click.argument("input", type=click.Path(exists=True, file_okay=True, dir_okay=False))
@click.argument("output", type=click.Path())
@click.argument("command_type", type=click.STRING)
@click.argument(
    "file_type", type=click.Choice(["xml", "json", "yaml"], case_sensitive=False)
)
def convert(input: Path, output: Path, command_type: str, file_type: str):
    """Convert any file type using oscal-cli tool

    Provide INPUT filename or path

    Provide OUTPUT filename or path

    Provide Command Type (catalog, profile, component-definition, ssp, mapping-collection, ap, ar, poam, metaschema)

    Provide OUTPUT Type: (xml, json, yaml)

    ex. regscale oscal convert /data/basic-ssp.json /tmp/output.xml ssp xml
    """
    oscal_convert(input, output, command_type, file_type)


def oscal_convert(input: Path, output: Path, command_type: str, file_type: str) -> None:
    """
    Call oscal-cli to perform conversion
    :param Path input: Path the original file
    :param Path output: Path to save the converted file
    :param str command_type: Classification of file
    :param str file_type: Desired file type
    :return: None
    """
    assert command_type.lower() in [
        "catalog",
        "profile",
        "component-definition",
        "ssp",
        "mapping-collection",
        "ap",
        "ar",
        "poam",
        "metaschema",
    ], "Please Enter a valid command type: (catalog, profile, component-definition, ssp, mapping-collection, ap, ar, poam, metaschema)"
    assert file_type.lower() in [
        "xml",
        "json",
        "yaml",
    ], "Please Enter a valid file type: (xml, json, or yaml)"
    logger.debug(Path(input))
    assert Path(input).exists()
    check_oscal()
    if "not found" not in app.get_java():
        if oscal_cli_path.exists():
            command = [
                oscal_cli_path,
                command_type,
                "convert",
                "--overwrite",
                "--to",
                file_type,
                input.absolute(),
                output.absolute(),
            ]
            logger.info(
                "Executing OSCAL Conversion... %s",
                [" ".join([str(item) for item in command])],
            )
            try:
                run(command, shell=False, check=True)
                logger.info("Finished! Output file saved: %s", output)
            except CalledProcessError as ex:
                if "status 3" not in str(ex):
                    logger.error("CalledProcessError: %s.", ex)

    else:
        logger.warning(
            "Java distribution not found, Java is required to execute OSCAL conversion tools."
        )


# OSCAL Profile Loader Support
@oscal.command()
@click.option(
    "--title",
    type=click.STRING,
    help="RegScale will name the profile with the title provided.",
    prompt="Enter the title for the OSCAL profile",
    required=True,
)
@click.option(
    "--categorization",
    type=click.Choice(["Low", "Moderate", "High"], case_sensitive=False),
    help="Choose from Low, Moderate, or High.",
    prompt="Enter the FIPS categorization level",
    required=True,
)
@click.option(
    "--catalog",
    type=click.INT,
    help="Primary key (unique ID) of the RegScale catalog.",
    prompt="Enter the RegScale Catalog ID to use",
    required=True,
)
@click.option(
    "--file_name",
    type=click.Path(exists=True, dir_okay=False, file_okay=True),
    help="RegScale will process and load the profile along with all specified controls.",
    prompt="Enter the file name of the OSCAL profile to process",
    required=True,
)
def profile(title: str, categorization: str, catalog: int, file_name: Path):
    """OSCAL Profile Loader."""
    upload_profile(
        title=title, categorization=categorization, catalog=catalog, file_name=file_name
    )


# flake8: noqa: C901
def upload_profile(
    title: str, categorization: str, catalog: int, file_name: Path
) -> None:
    """
    OSCAL Profile Uploader
    :param str title: Title
    :param str categorization: Category information
    :param str catalog: Catalog Title
    :param Path file_name: Desired file name
    :return: None
    """
    # validation
    if catalog <= 0:
        error_and_exit("No catalog provided or catalog invalid.")
    elif (
        categorization.title() != "Low"
        and categorization.title() != "Moderate"
        and categorization.title() != "High"
    ):
        error_and_exit("Categorization not provided or invalid.")
    else:
        # load the catalog
        try:
            oscal = open(file_name, "r", encoding="utf-8-sig")
            oscal_data = json.load(oscal)
        except Exception as ex:
            logger.debug(file_name)
            error_and_exit(
                f"Unable to open the specified OSCAL file for processing.\n{ex}"
            )
        # load the config from YAML
        try:
            config = app.load_config()
        except FileNotFoundError:
            error_and_exit("Unable to open the init.yaml file.")

        # set headers
        str_user = config["userId"]
        headers = {"Accept": "application/json", "Authorization": config["token"]}

        # create a new profile
        profile = {
            "id": 0,
            "uuid": "",
            "name": title,
            "confidentiality": "",
            "integrity": "",
            "availability": "",
            "category": categorization,
            "profileOwnerId": str_user,
            "createdById": str_user,
            "dateCreated": None,
            "lastUpdatedById": str_user,
            "dateLastUpdated": None,
            "isPublic": True,
        }

        # create the profile
        url_prof = f'{config["domain"]}/api/profiles/'
        logger.info("RegScale creating a new profile...")
        try:
            prof_response = api.post(url=url_prof, headers=headers, json=profile)
            prof_json_response = prof_response.json()
            logger.info("\nProfile ID: " + str(prof_json_response["id"]))
            # get the profile ID
            int_profile = prof_json_response["id"]
        except requests.exceptions.RequestException as ex:
            error_and_exit(f"Unable to create profile in RegScale.\n{ex}")

        # get the list of existing controls for the catalog
        url_sc = f'{config["domain"]}/api/SecurityControls/getList/{catalog}'
        try:
            sc_response = api.get(url_sc, headers=headers)
            sc_data = sc_response.json()
        except requests.exceptions.RequestException as ex:
            error_and_exit(
                f"Unable to retrieve security controls for this catalog in RegScale.\nError: {ex}\n{sc_response.text}",
            )

        # loop through each item in the OSCAL control set
        mappings = []
        for m in oscal_data["profile"]["imports"][0]["include-controls"][0]["with-ids"]:
            b_match = False
            for sc in sc_data:
                if m == sc["controlId"]:
                    b_match = True
                    map = {
                        "id": 0,
                        "profileID": int_profile,
                        "controlID": int(sc["id"]),
                    }
                    mappings.append(map)
                    break
            if b_match is False:
                logger.error("Unable to locate control: %s.", m)

        # upload the controls to the profile as mappings
        url_maps = config["domain"] + "/api/profileMapping/batchCreate"
        try:
            api.post(url_maps, headers=headers, json=mappings)
            logger.info(
                "%s total mappings created in RegScale for this profile.",
                str(len(mappings)),
            )
        except requests.exceptions.RequestException as ex:
            error_and_exit(
                f"Unable to create mappings for this profile in RegScale.\n{ex}"
            )


# Process catalog from OSCAL
@oscal.command()
@click.option(
    "--file_name",
    type=click.Path(exists=True, dir_okay=False, file_okay=True),
    help="RegScale will process and load the catalog along with all controls, statements, and parameters.",
    prompt="Enter the file name of the NIST Catalog to process",
    required=True,
)
def catalog(file_name: Path):
    """Process and load catalog to RegScale."""
    upload_catalog(file_name)


# flake8: noqa: C901
def upload_catalog(file_name: Path) -> None:
    """
    Process and load catalog to RegScale
    :param Path file_name: Path to the catalog to upload
    :raises: requests.exceptions.RequestException if any issues encountered during API calls
    :raises: General Error if unable to load init.yaml
    :return: None
    """
    # Create directory if not exists
    check_file_path("processing")

    # load the catalog
    try:
        with open(file_name, "r", encoding="utf-8-sig") as input:
            oscal_data = json.load(input)
    except requests.exceptions.RequestException as ex:
        error_and_exit(f"Unable to open the specified OSCAL file for processing.\n{ex}")
    # load the config from YAML
    try:
        config = app.load_config()
    except Exception:
        error_and_exit("Unable to open the init file.")
    # debug flag to pause upload when testing and debugging (always true for production CLI use)
    upload_flag = params_flag = tests_flag = objects_flag = deep_links_flag = True

    # set headers
    str_user = config["userId"]
    headers = {"Accept": "application/json", "Authorization": config["token"]}

    # parse the OSCAL JSON to get related data (used to enrich base spreadsheet)
    catalog_arr = oscal_data["catalog"]
    str_uuid = catalog_arr["uuid"]
    resource_guid = ""
    resource_title = ""
    citation = ""
    links = ""

    # process resources for lookup
    resources = []
    if "back-matter" in catalog_arr:
        back_matter_arr = catalog_arr["back-matter"]
        for i in back_matter_arr["resources"]:
            # make sure values exist
            if "title" in i:
                resource_title = i["title"]
            if "uuid" in i:
                resource_guid = i["uuid"]
            if "citation" in i:
                citation = i["citation"]
                if "text" in citation:
                    citation = citation["text"]
            links = ""
            if "rlinks" in i:
                links = i["rlinks"]
                if len(links) > 1:
                    for x in links:
                        if "href" in x:
                            links += x["href"] + "<br/>"
                elif isinstance(links[0], dict) and len(links) == 1:
                    links = links[0].get("href")
            # add parsed/flattened resource to the array
            res = {
                "uuid": resource_guid,
                "short": resource_title,
                "title": citation,
                "links": links,
            }
            resources.append(res)

    # Write to file to visualize the output
    save_data_to(
        file_name=f"processing{sep}resources", file_type=".json", data=resources
    )
    # convert data to pandas dataframe
    raw_data = pd.DataFrame(resources)

    # copy the columns of data that we want while renaming them to a specific case
    resource_data = (
        raw_data[["uuid", "title", "links"]]
        .copy()
        .rename(columns={"uuid": "UUID", "title": "Title", "links": "Links"})
    )

    # convert the data table to an HTML formatted table
    str_resources = resource_data.to_html(index=False, justify="left")

    # set the catalog URL for your Atlasity instance
    url_cats = config["domain"] + "/api/catalogues/"

    # setup catalog data
    cat = {
        "title": catalog_arr["metadata"]["title"],
        "description": "This publication provides a catalog of security and privacy controls for information systems and organizations to protect organizational operations and assets, individuals, other organizations, and the Nation from a diverse set of threats and risks, including hostile attacks, human errors, natural disasters, structural failures, foreign intelligence entities, and privacy risks. <br/><br/><strong>Resources</strong><br/><br/>"
        + str_resources,
        "datePublished": catalog_arr["metadata"]["version"],
        "uuid": str_uuid,
        "lastRevisionDate": catalog_arr["metadata"]["version"],
        "url": "https://csrc.nist.gov/",
        "abstract": "This publication provides a catalog of security and privacy controls for federal information systems and organizations and a process for selecting controls to protect organizational operations (including mission, functions, image, and reputation), organizational assets, individuals, other organizations, and the Nation from a diverse set of threats including hostile cyber attacks, natural disasters, structural failures, and human errors (both intentional and unintentional). The security and privacy controls are customizable and implemented as part of an organization-wide process that manages information security and privacy risk. The controls address a diverse set of security and privacy requirements across the federal government and critical infrastructure, derived from legislation, Executive Orders, policies, directives, regulations, standards, and/or mission/business needs. The publication also describes how to develop specialized sets of controls, or overlays, tailored for specific types of missions/business functions, technologies, or environments of operation. Finally, the catalog of security controls addresses security from both a functionality perspective (the strength of security functions and mechanisms provided) and an assurance perspective (the measures of confidence in the implemented security capability). Addressing both security functionality and assurance helps to ensure that information technology component products and the information systems built from those products using sound system and security engineering principles are sufficiently trustworthy.",
        "keywords": "FIPS Publication 200; FISMA; Privacy Act; Risk Management Framework; security controls; FIPS Publication 199; security requirements; computer security; assurance;",
        "createdById": str_user,
        "lastUpdatedById": str_user,
    }

    # create the catalog and print success result
    if upload_flag is True:
        logger.info("RegScale creating catalog....")
        try:
            logger.debug(f"url={url_cats}, headers={headers}, json={cat}")
            response = api.post(url=url_cats, headers=headers, json=cat)
            # response = requests.request(url=url_cats, headers=headers, json=cat)
            json_response = response.json()
            logger.info("Catalog ID: %s.", json_response["id"])
            # get the catalog ID
            catalogue_id = json_response["id"]
        except requests.exceptions.RequestException as ex:
            error_and_exit(
                f"Unable to create catalog in RegScale, try logging in again to pull a fresh token.\n{ex}",
            )
    else:
        # don't set ID in debug mode
        catalogue_id = 0

    # process NIST families of controls
    families = []
    oscal_controls = []
    parameters = []
    parts = []
    assessments = []

    # process groups of controls
    for i in catalog_arr["groups"]:
        str_family = i["title"]
        f = {
            "id": i["id"],
            "title": i["title"],
        }
        # add parsed item to the family array
        families.append(f)

        # loop through controls
        for ctrl in i["controls"]:

            # process the control
            new_ctrl = processControl(
                ctrl, resources, str_family, parameters, parts, assessments
            )
            oscal_controls.append(new_ctrl)

            # check for child controls/enhancements
            if "controls" in ctrl:
                child_ctrls = ctrl["controls"]
                for child_ctrl in child_ctrls:
                    child = processControl(
                        child_ctrl,
                        resources,
                        str_family,
                        parameters,
                        parts,
                        assessments,
                    )
                    oscal_controls.append(child)

    # # Write to file to visualize the output
    save_data_to(file_name=f"processing{sep}families", file_type=".json", data=families)
    logger.info("%s total families processed.", len(families))

    # # Write to file to visualize the output
    save_data_to(
        file_name=f"processing{sep}controls", file_type=".json", data=oscal_controls
    )
    logger.info("%s total controls processed.", len(oscal_controls))

    # # Write to file to visualize the output
    save_data_to(
        file_name=f"processing{sep}parameters", file_type=".json", data=parameters
    )
    logger.info("%s total parameters processed.", len(parameters))

    # # Write to file to visualize the output
    save_data_to(file_name=f"processing{sep}parts", file_type=".json", data=parts)
    logger.info("%s total parts processed.", len(parts))

    # # Write to file to visualize the output
    save_data_to(file_name=f"processing{sep}tests", file_type=".json", data=assessments)
    logger.info("%s total assessments processed.", len(assessments))

    # use the progress object for the threaded process
    with job_progress:
        if oscal_controls:
            # log the information
            logger.info("Posting %s OSCAL control(s) to RegScale.", len(oscal_controls))
            # create task for job progress object
            creating_controls = job_progress.add_task(
                f"[#f8b737]Creating {len(oscal_controls)} control(s) in RegScale...",
                total=len(oscal_controls),
            )
            # create threads to create controls
            create_threads(
                process=post_controls,
                args=(
                    oscal_controls,
                    catalogue_id,
                    upload_flag,
                    config,
                    creating_controls,
                ),
                thread_count=len(oscal_controls),
            )
            # log the outcome
            logger.info(
                "%s OSCAL control(s) posted to RegScale.",
                len(loop_counter["controls"]),
            )
            # Write to file to visualize the output
            save_data_to(
                file_name=f"processing{sep}mappedControls",
                file_type=".json",
                data=controls,
            )
        # Write to file to visualize the output
        if upload_flag:
            global new_regscale_controls
            save_data_to(
                file_name=f"processing{sep}newControls",
                file_type=".json",
                data=new_regscale_controls,
            )
        else:
            with open(
                f"processing{sep}newControls.json", "r", encoding="utf-8-sig"
            ) as infile:
                new_regscale_controls = json.load(infile)
        # only process if the controls exists to map to
        if len(new_regscale_controls) > 0:
            if parameters:
                # log the information
                logger.info(
                    "Creating %s child control(s) in RegScale.", len(parameters)
                )
                # create task for analyzing child controls
                posting_child_controls = job_progress.add_task(
                    f"[#ef5d23]Creating {len(parameters)} child control(s) in RegScale..."
                )
                # create threads to post child controls
                create_threads(
                    process=post_child_controls,
                    args=(
                        parameters,
                        new_regscale_controls,
                        params_flag,
                        config,
                        posting_child_controls,
                    ),
                    thread_count=len(parameters),
                )
                # log the outcome
                logger.info(
                    "%s OSCAL child control(s) created in RegScale.",
                    len(loop_counter["child_controls"]),
                )

                # output the result
                save_data_to(
                    file_name=f"processing{sep}newParameters",
                    file_type=".json",
                    data=new_params,
                )
            if assessments:
                # log the information
                logger.info("Creating %s test(s) in RegScale.", len(assessments))
                # create task for creating assessments
                assigning_tests = job_progress.add_task(
                    f"[#21a5bb]Creating {len(assessments)} assessment(s) in RegScale..."
                )
                # create threads to create tests
                create_threads(
                    process=assign_control_tests,
                    args=(
                        assessments,
                        new_regscale_controls,
                        tests_flag,
                        config,
                        assigning_tests,
                    ),
                    thread_count=len(assessments),
                )
                # output the result
                save_data_to(
                    file_name=f"processing{sep}newTests",
                    file_type=".json",
                    data=new_tests,
                )
                # log the outcome
                logger.info(
                    "%s/%s tests(s) created in RegScale.",
                    len(assessments),
                    len(loop_counter["tests"]),
                )
            if parts:
                # log the information
                logger.info("Creating %s objective(s) in RegScale.", len(assessments))
                # create task for creating objectives
                creating_objectives = job_progress.add_task(
                    f"[#0866b4]Creating {len(parts)} objectives(s) in RegScale..."
                )
                # create threads to loop through controls
                create_threads(
                    process=create_objectives,
                    args=(
                        parts,
                        new_regscale_controls,
                        objects_flag,
                        config,
                        creating_objectives,
                    ),
                    thread_count=len(parts),
                )
                # log the outcome
                logger.info(
                    "%s objective(s) created in RegScale.",
                    len(loop_counter["objectives"]),
                )
                # output the result
                save_data_to(
                    file_name=f"processing{sep}newObjectives",
                    file_type=".json",
                    data=new_objectives,
                )
            if deep_links_flag:
                # process deep links
                try:
                    logger.info(
                        "Retrieving all objectives for this catalogue # %i from RegScale (this might take a minute)...",
                        catalogue_id,
                    )
                    url_deep = f'{config["domain"]}/api/controlObjectives/getByCatalogue/{catalogue_id}'
                    obj_list_response = api.get(
                        url_deep, headers={"Authorization": config["token"]}
                    )
                    obj_list = obj_list_response.json()
                    logger.info(
                        "%i total objectives now retrieved from RegScale for processing.",
                        len(obj_list),
                    )
                except Exception:
                    error_and_exit(
                        "Unable to retrieve control objective information from RegScale."
                    )
                # log the information
                logger.info(
                    "Analyzing %s objective(s) for potential updating in RegScale.",
                    len(assessments),
                )
                # create task for creating objectives
                updating_objectives = job_progress.add_task(
                    f"[#05d1b7]Analyzing {len(obj_list)} objectives(s) in RegScale..."
                )
                # create threads to loop through controls
                create_threads(
                    process=update_objectives,
                    args=(obj_list, parts, config, updating_objectives),
                    thread_count=len(obj_list),
                )
                # log the outcome
                logger.info(
                    "%s objective(s) analyzed & %s objective(s) updated in RegScale.",
                    len(obj_list),
                    len(loop_counter["updates"]),
                )
            if errors:
                # output the errors
                save_data_to(
                    file_name=f"processing{sep}errors",
                    file_type=".json",
                    data=new_objectives,
                )


def post_controls(args: Tuple, thread: int) -> None:
    """
    Function to analyze controls from OSCAL catalog and post them to RegScale while using threads
    :param Tuple args: Tuple of args to use during the process
    :param int thread: Thread number of current thread
    :raises: requests.exceptions.RequestException if API call experienced an error
    :return: None
    """
    # set up local variables from args passed
    controls, catalog_id, upload_flag, config, task = args

    # set up RegScale URL
    url_sc = config["domain"] + "/api/securitycontrols/"

    # update api pool limits to maxThread count from init.yaml
    api.pool_connections = (
        config["maxThreads"]
        if config["maxThreads"] > api.pool_connections
        else api.pool_connections
    )
    api.pool_maxsize = (
        config["maxThreads"]
        if config["maxThreads"] > api.pool_maxsize
        else api.pool_maxsize
    )

    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(controls))

    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the recommendation for the thread for later use in the function
        control = controls[threads[i]]

        # create each security control
        sc = {
            "title": control["id"] + " - " + control["title"],
            "controlType": "Stand-Alone",
            "controlId": control["id"],
            "description": control["parts"] + "<br/><br/>" + control["guidance"],
            "references": control["links"],
            "relatedControls": "",
            "subControls": "",
            "enhancements": control["enhancements"],
            "family": control["family"],
            "mappings": control["parameters"],
            "assessmentPlan": control["assessment"],
            "weight": 0,
            "practiceLevel": "",
            "catalogueID": catalog_id,
            "createdById": config["userId"],
            "lastUpdatedById": config["userId"],
        }
        # attempt to create the security control
        if upload_flag:
            try:
                # upload to RegScale
                response = api.post(url=url_sc, json=sc)
                json_response = response.json()
                logger.debug("\n\nSuccess - %s", sc["title"])
                loop_counter["controls"].append(control)

                # update id to the new control id
                sc["id"] = json_response["id"]

                # append the result
                controls.append(sc)

                # add the new controls
                new_regscale_controls.append(json_response)
            except requests.exceptions.RequestException:
                logger.error("Unable to create security control %s,", sc["title"])
                errors.append(sc)
        else:
            # append the result
            controls.append(sc)
        job_progress.update(task, advance=1)


def post_child_controls(args: Tuple, thread: int) -> None:
    """
    Function to analyze child controls from OSCAL catalog and posts them to RegScale while using threads
    :param Tuple args: Tuple of args to use during the process
    :param int thread: Thread number of current thread
    :raises: requests.exceptions.RequestException if API call experienced an error
    :return: None
    """
    # set up local variables from args passed
    parameters, regscale_controls, params_flag, config, task = args

    # set up RegScale URL
    url_params = config["domain"] + "/api/controlParameters/"

    # update api pool limits to maxThread count from init.yaml
    api.pool_connections = (
        config["maxThreads"]
        if config["maxThreads"] > api.pool_connections
        else api.pool_connections
    )
    api.pool_maxsize = (
        config["maxThreads"]
        if config["maxThreads"] > api.pool_maxsize
        else api.pool_maxsize
    )

    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(parameters))

    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the parameter for the thread for later use in the function
        parameter = parameters[threads[i]]

        # find the parent control
        ctrl_lookup = next(
            (
                item
                for item in regscale_controls
                if (item["controlId"] == parameter["controlId"])
            ),
            None,
        )
        if ctrl_lookup is None:
            logger.error(
                "Unable to locate %s for this parameter: %s.",
                parameter["controlId"],
                parameter["name"],
            )
        else:
            # create a new parameter to upload
            new_param = {
                "id": 0,
                "uuid": "",
                "text": parameter["value"],
                "dataType": "string",
                "parameterId": parameter["name"],
                "securityControlId": ctrl_lookup["id"],
                "archived": False,
                "createdById": config["userId"],
                "dateCreated": None,
                "lastUpdatedById": config["userId"],
                "dateLastUpdated": None,
            }
            # attempt to create the parameter
            if params_flag:
                try:
                    # upload to RegScale
                    response = api.post(url_params, json=new_param)
                    response_data = response.json()
                    logger.debug(
                        "\n\nSuccess - %s parameter uploaded successfully.",
                        new_param["parameterId"],
                    )
                    # update the id to the new parameter id
                    new_param["id"] = response_data["id"]

                    # add the control to the new array
                    new_params.append(new_param)
                    loop_counter["child_controls"].append(response)
                except requests.exceptions.RequestException:
                    logger.error(
                        "Unable to create parameter: %s.", new_param["parameterId"]
                    )
                    errors.append(new_param)
            else:
                # add the control to the new array
                new_params.append(new_param)
        job_progress.update(task, advance=1)


def assign_control_tests(args: Tuple, thread: int) -> None:
    """
    Function to analyze match controls to assessments while using threads
    :param Tuple args: Tuple of args to use during the process
    :param int thread: Thread number of current thread
    :raises: requests.exceptions.RequestException if API call experienced an error
    :return: None
    """
    # set up local variables from args passed
    assessments, regscale_controls, tests_flag, config, task = args

    # set up RegScale URL
    url_tests = config["domain"] + "/api/controlTestPlans/"

    # update api pool limits to maxThread count from init.yaml
    api.pool_connections = (
        config["maxThreads"]
        if config["maxThreads"] > api.pool_connections
        else api.pool_connections
    )
    api.pool_maxsize = (
        config["maxThreads"]
        if config["maxThreads"] > api.pool_maxsize
        else api.pool_maxsize
    )

    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(assessments))

    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the recommendation for the thread for later use in the function
        assessment = assessments[threads[i]]
        # find the parent control
        ctrl_lookup = next(
            (
                item
                for item in regscale_controls
                if (item["controlId"] == assessment["parentControl"])
            ),
            None,
        )
        if ctrl_lookup is None:
            logger.error(
                "Unable to locate %s for this test.", assessment["parentControl"]
            )
        else:
            # create a new test to upload
            new_test = {
                "id": 0,
                "uuid": "",
                "test": f'{assessment["testType"]} - {assessment["description"]}',
                "testId": str(uuid.uuid4()),
                "securityControlId": ctrl_lookup["id"],
                "archived": False,
                "createdById": config["userId"],
                "dateCreated": None,
                "lastUpdatedById": config["userId"],
                "dateLastUpdated": None,
            }
            # attempt to create the test
            if tests_flag:
                try:
                    # upload to RegScale
                    response = api.post(url_tests, json=new_test)
                    json_response = response.json()
                    logger.debug(
                        "\n\nSuccess - %s -  test uploaded successfully.",
                        new_test["test"],
                    )
                    # update the id to the new test id
                    new_test["id"] = json_response["id"]

                    # add the test to the new array
                    new_tests.append(new_test)

                    loop_counter["tests"].append(json_response)
                except requests.exceptions.RequestException:
                    logger.error("Unable to create test: %s.", new_test["test"])
                    errors.append(new_test)
            else:
                # add the test to the new array
                new_tests.append(new_test)
        job_progress.update(task, advance=1)


def create_objectives(args: Tuple, thread: int) -> None:
    """
    Function to create objectives from OSCAL catalog and post them to RegScale while using threads
    :param Tuple args: Tuple of args to use during the process
    :param int thread: Thread number of current thread
    :raises: requests.exceptions.RequestException if API call experienced an error
    :return: None
    """
    # set up local variables from args passed
    objectives, regscale_controls, objects_flag, config, task = args

    # set up RegScale URL
    url_objs = config["domain"] + "/api/controlObjectives/"

    # update api pool limits to maxThread count from init.yaml
    api.pool_connections = (
        config["maxThreads"]
        if config["maxThreads"] > api.pool_connections
        else api.pool_connections
    )
    api.pool_maxsize = (
        config["maxThreads"]
        if config["maxThreads"] > api.pool_maxsize
        else api.pool_maxsize
    )

    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(objectives))

    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the recommendation for the thread for later use in the function
        objective = objectives[threads[i]]

        # find the parent control
        ctrl_lookup = next(
            (
                item
                for item in regscale_controls
                if (item["controlId"] == objective["parentControl"])
            ),
            None,
        )
        if ctrl_lookup is None:
            logger.error(
                "Error: Unable to locate %s for this objective/part: %s.",
                objective["parentControl"],
                objective["name"],
            )
        else:
            # create a new test to upload
            new_obj = {
                "id": 0,
                "uuid": "",
                "name": objective["name"],
                "description": objective["description"],
                "objectiveType": objective["objectiveType"],
                "otherId": "",
                "securityControlId": ctrl_lookup["id"],
                "parentObjectiveId": None,
                "archived": False,
                "createdById": config["userId"],
                "dateCreated": None,
                "lastUpdatedById": config["userId"],
                "dateLastUpdated": None,
            }
            # attempt to create the objective
            if objects_flag:
                try:
                    # upload to RegScale
                    response = api.post(url_objs, json=new_obj)
                    json_response = response.json()
                    logger.debug(
                        "\n\nSuccess - %s -  objective uploaded successfully.",
                        new_obj["name"],
                    )
                    # update the id to the newly created id
                    new_obj["id"] = json_response["id"]
                    # add the part to the new array
                    new_objectives.append(new_obj)
                    loop_counter["objectives"].append(json_response)
                except requests.exceptions.RequestException as rex:
                    logger.error(
                        "Unable to create objective: %s.\n%s", new_obj["name"], rex
                    )
                    errors.append(new_obj)
            else:
                # add the part to the new array
                new_objectives.append(new_obj)
        job_progress.update(task, advance=1)


def update_objectives(args: Tuple, thread: int) -> None:
    """
    loop through each objective and see if it has a parent, if so,
    update parent ID and send update to RegScale while using threads
    :param Tuple args: Tuple of args to use during the process
    :param int thread: Thread number of current thread
    :raises: requests.exceptions.RequestException if API call experienced an error
    :return: None
    """
    # set up local variables from args passed
    objectives, parts, config, task = args

    # set up RegScale URL
    url_objs = config["domain"] + "/api/controlObjectives/"

    # update api pool limits to maxThread count from init.yaml
    api.pool_connections = (
        config["maxThreads"]
        if config["maxThreads"] > api.pool_connections
        else api.pool_connections
    )
    api.pool_maxsize = (
        config["maxThreads"]
        if config["maxThreads"] > api.pool_maxsize
        else api.pool_maxsize
    )

    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(objectives))

    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the recommendation for the thread for later use in the function
        objective = objectives[threads[i]]

        # find the part by name
        part_lookup = next(
            (item for item in parts if (item["name"] == objective["name"])), None
        )
        if part_lookup is not None:
            # see if the part has a parent
            if part_lookup["parentObjective"] != "":
                # lookup the parent objective from RegScale
                parent_lookup = next(
                    (
                        item
                        for item in objectives
                        if (item["name"] == part_lookup["parentObjective"])
                    ),
                    None,
                )
                if parent_lookup is not None:
                    logger.debug("Found Parent: %s.", parent_lookup["name"])
                    # update the parent
                    update_parent = parent_lookup["objective"]
                    update_parent["parentObjectiveId"] = parent_lookup["id"]
                    try:
                        # upload to RegScale
                        update_response = api.put(
                            f'{url_objs}{update_parent["id"]}',
                            json=update_parent,
                        )
                        # updateData = updateResponse.json()
                        logger.debug(
                            "Success - %s -  objective parent updated successfully.",
                            update_parent["name"],
                        )
                        loop_counter["updates"].append(update_response)
                    except requests.exceptions.RequestException:
                        logger.error(
                            "Unable to update parent objective: %s.",
                            update_parent["name"],
                        )
                        errors.append(update_parent)
        job_progress.update(task, advance=1)


#############################################################################
#
#   Supporting Functions
#
#############################################################################


def process_objectives(obj, parts, ctrl, parent_id) -> str:
    """
    Function for recursively working through objectives and formatting it as HTML description
    :param obj: RegScale object
    :param parts: Parts of the object
    :param ctrl: Controls for the object
    :param parent_id: Parent id of the Object
    :return: HTML formatted string of object
    :rtype: str
    """
    str_obj = "<ul>"
    # loop through parts/objectives recursively
    for o in obj:
        # check prose
        str_prose = ""
        if "prose" in o:
            str_prose = o["prose"]

        # check name
        str_name = ""
        if "name" in o:
            str_name = o["name"]

        # create the new part
        part = {
            "id": 0,
            "name": o["id"],
            "objectiveType": str_name,
            "description": str_prose,
            "parentControl": ctrl["id"],
            "parentObjective": parent_id,
        }
        parts.append(part)
        str_obj += "<li>{{" + o["id"] + "}}"
        if "prose" in o:
            str_obj += " - " + str_prose
        str_obj += "</li>"
        if "parts" in o:
            str_obj += process_objectives(o["parts"], parts, ctrl, o["id"])
    str_obj += "</ul>"
    return str_obj


def processControl(ctrl, resources, str_family, parameters, parts, assessments) -> dict:
    """
    function to process each control and formats it as a dictioanry
    :param ctrl: RegScale control
    :param resources: resources of control
    :param str_family: Family of control
    :param parameters: Parameters for the control
    :param parts: Parts of the control
    :param assessments: Assessments belonging to the control
    :return: Dictionary of new control
    :rtype: dict
    """
    # see if parameters exist
    if "params" in ctrl:
        # loop through each parameter
        for p in ctrl["params"]:
            # create a new parameter object
            p_new = {
                "name": p["id"],
                "value": "",
                "paramType": "",
                "controlId": ctrl["id"],
            }
            # process basic label
            if "label" in p:
                p_new["paramType"] = "text"
                p_new["value"] = p["label"]
            else:
                # initialize
                strParams = "Select ("
                # process select types
                if "select" in p:
                    select = p["select"]
                    if "how-many" in select:
                        strParams += select["how-many"]
                        p_new["paramType"] = "how-many"
                    if "choice" in select:
                        p_new["paramType"] = "choice"
                        strParams += "select) - "
                        for z in select["choice"]:
                            strParams += z + ", "
                    p_new["value"] = strParams
            # add to the array
            parameters.append(p_new)

    # get enhancements
    str_enhance = ""
    if "controls" in ctrl:
        child_enhc = ctrl["controls"]
        str_enhance += "<strong>Enhancements</strong><br/><br/>"
        str_enhance += "<ul>"
        for che in child_enhc:
            str_enhance += "<li>{{" + che["id"] + "}} - " + che["title"] + "</li>"
        str_enhance += "</ul>"

    # process control links
    int_link = 1
    str_links = ""
    if "links" in ctrl:
        for link in ctrl["links"]:
            # lookup the OSCAL control to enrich the data
            link_lookup = next(
                (item for item in resources if ("#" + item["uuid"]) == link["href"]),
                None,
            )
            if link_lookup is not None:
                str_links += (
                    str(int_link)
                    + ") "
                    + link_lookup["title"]
                    + " (OSCAL ID: "
                    + link_lookup["uuid"]
                    + ")<br/>"
                )
                int_link += 1
            else:
                str_links += link["href"] + "<br/>"

    # process parts
    part_info = process_parts(ctrl, parts, assessments)

    # add control
    new_ctrl = {
        "id": ctrl["id"],
        "title": ctrl["title"],
        "family": str_family,
        "links": str_links,
        "parameters": "",
        "parts": part_info["parts"],
        "assessment": part_info["assessments"],
        "guidance": part_info["guidance"],
        "enhancements": str_enhance,
    }

    # return the result
    return new_ctrl


def process_parts(ctrl, parts, assessments) -> dict:
    """
    Function to format control
    :param ctrl: RegScale control
    :param parts: Parts of the control
    :param assessments: Assessments of the control
    :return: Formatted dictionary
    :rtype: dict
    """
    # process parts
    if "parts" in ctrl:
        # initialize
        str_parts = ""
        str_guidance = ""
        str_assessment = ""

        # create text field for human display
        str_parts += "<ul>"
        for p in ctrl["parts"]:
            if ("id" in p) and (p["name"].startswith("assessment") is False):
                # check prose
                str_prose = ""
                if "prose" in p:
                    str_prose = p["prose"]

                # check name
                strName = ""
                if "name" in p:
                    strName = p["name"]

                # create the new part
                part = {
                    "id": 0,
                    "name": p["id"],
                    "objectiveType": strName,
                    "description": str_prose,
                    "parentControl": ctrl["id"],
                    "parentObjective": "",
                }
                parts.append(part)
                # process objectives
                if (
                    p["name"] == "objective"
                    or p["name"] == "statement"
                    or p["name"] == "item"
                ):
                    try:
                        str_parts += "<li>{{" + p["id"] + "}} - " + str_prose + "</li>"
                    except Exception:
                        logger.error("Unable to parse part - %s.", p["id"])
                    if "parts" in p:
                        str_parts += process_objectives(
                            p["parts"], parts, ctrl, p["id"]
                        )
                # process guidance
                if p["name"] == "guidance":
                    str_guidance = "<ul><li>Guidance</li>"
                    if "prose" in p:
                        str_guidance += "<ul>"
                        str_guidance += "<li>" + p["prose"] + "</li>"
                        str_guidance += "</ul>"
                    if "links" in p:
                        str_guidance += "<ul>"
                        for lkp in p["links"]:
                            str_guidance += (
                                "<li>" + lkp["href"] + ", " + lkp["rel"] + "</li>"
                            )
                        str_guidance += "</ul>"
                    str_guidance += "</ul>"
            else:
                # process assessments
                process_assessments(p, ctrl, assessments)

        str_parts += "</ul>"
    else:
        # no parts - set default values
        str_parts = ""
        str_guidance = ""
        str_assessment = ""

    # return the result
    part_info = {
        "parts": str_parts,
        "guidance": str_guidance,
        "assessments": str_assessment,
    }
    return part_info


def process_assessments(p, ctrl, assessments) -> None:
    """
    Process assessment data
    :param p: Data to process
    :param ctrl: Controls
    :param assessments: Assessments
    :return: None
    """
    # process assessments
    if p["name"].startswith("assessment") is True:
        # see if a lowe level objective that has prose
        if "prose" in p:
            # create new assessment objective
            ast = {
                "id": 0,
                "name": p["id"],
                "testType": p["name"],
                "description": p["prose"],
                "parentControl": ctrl["id"],
            }

            # see if it has any child tests
            if "parts" in p:
                if len(p["parts"]) > 0:
                    for item in p["parts"]:
                        process_assessments(item, ctrl, assessments)
        else:
            # check the id
            str_part_id = ""
            if "id" in p:
                str_part_id = p["id"]
            else:
                str_part_id = str(uuid.uuid4())

            # handle methods
            ast = {
                "id": 0,
                "name": str_part_id,
                "testType": "",
                "description": "",
                "parentControl": ctrl["id"],
            }
            if "props" in p:
                if len(p["props"]) > 0:
                    if "value" in p["props"][0]:
                        ast["testType"] = p["props"][0]["value"]
            if "parts" in p:
                if len(p["parts"]) > 0:
                    if "prose" in p["parts"][0]:
                        ast["description"] = p["parts"][0]["prose"]

        # add test of the array
        if ast["description"] != "":
            assessments.append(ast)


def check_oscal() -> None:
    """
    Check if oscal dependencies are installed
    :raises: General error if dependencies aren't found
    :return: None
    """
    """"""
    if (
        "unable to access jarfile".lower() in app.get_java()
        or not oscal_cli_path.exists()
    ):
        error_and_exit(
            "OSCAL CLI library not found, please check init.yaml and add the full cli path.  e.g. /opt/oscal-cli/bin/oscal-cli"
        )
