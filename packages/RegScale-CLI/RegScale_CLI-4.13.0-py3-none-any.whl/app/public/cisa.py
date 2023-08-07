#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Integrates CISA into RegScale"""

# standard python imports
import dataclasses
import logging
import re
from concurrent.futures import ALL_COMPLETED, ThreadPoolExecutor, wait
from datetime import date, datetime
from typing import Tuple
from urllib.error import URLError
from urllib.parse import urlparse

import click
import dateutil.parser as dparser
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from requests import exceptions
from rich.console import Console

from app.api import Api
from app.application import Application
from app.internal.login import is_valid
from app.logz import create_logger
from app.utils.regscale_utils import get_all_from_module
from models.regscale_models.threat import Threat

logger = create_logger()
console = Console()


@click.group()
def cisa():
    """Update CISA."""


@cisa.command(name="ingest_cisa_kev")
def ingest_cisa_kev():
    """Update RegScale threats with the latest Known Exploited Vulnerabilities (KEV) feed from cisa.gov."""
    data = update_known_vulnerabilities()
    update_regscale(data)


@cisa.command(name="ingest_cisa_alerts")
@click.option(
    "--year",
    type=click.INT,
    help="Enter the year to search for CISA alerts.",
    default=date.today().year,
    show_default=True,
    required=True,
)
def ingest_cisa_alerts(year: int):
    """Update RegScale threats with alerts from cisa.gov."""
    alerts(year)


def alerts(year: int) -> None:
    """
    Return CISA alerts for the specified year
    :param int year: A target year for CISA alerts
    :return: None
    """
    app = Application()
    api = Api(app)
    # Check to make sure we have a valid token
    reg_threats = get_all_from_module(api=api, module="threats")
    unique_threats = list(set([reg["description"] for reg in reg_threats]))
    if is_valid(app=app):
        config = app.config
        if "cisa_alerts" in config:
            cisa_url = f'{config["cisaAlerts"]}/{year}'
        else:
            cisa_url = f"https://www.cisa.gov/uscert/ncas/alerts/{year}"
        threats = parse_html(cisa_url, app=app)
        insert_threats = []
        update_threats = []
        if len(threats) > 0:
            logger.info(threats)
            for threat in threats:
                if threat.description in unique_threats:
                    old_dict = [
                        reg
                        for reg in reg_threats
                        if reg["description"] == threat.description
                    ][0]
                    # threat_id = old_dict["id"]
                    update_dict = threat.__dict__
                    update_dict = merge_old(update_dict, old_dict)
                    update_threats.append(update_dict)  # Update
                else:
                    insert_threats.append(threat.__dict__)  # Post
    else:
        logger.error("Login Error: Invalid Credentials, please login for a new token.")
    logging.getLogger("urllib3").propagate = False
    url_threats = config["domain"] + "/api/threats"
    api.update_server(
        url=url_threats,
        json_list=insert_threats,
        method="post",
        config=config,
        message=f"Inserting {len(insert_threats)} threats to RegScale...",
    )
    update_regscale_threats(json_list=update_threats)


def parse_html(page_url: str, app: Application) -> list:
    """
    Convert HTML from a given URL to a RegScale threat
    :param str page_url: A URL to parse
    :param app: Application object
    :return: List of RegScale threats
    :rtype: list
    """
    page = 0
    items = 999
    title = None
    short_description = None
    threats = []
    links = []
    while items > 0:
        soup = gen_soup(page_url + f"?page={page}", app)

        # date_created = convert_date_string(str(date.today().isoformat()))

        cvedivs = soup.find_all("div", {"class": "views-field views-field-title"})
        for div in cvedivs:
            if div.find_all("span", {"class": "field-content"}) is not None:
                for span in div.find_all("span", {"class": "field-content"}):
                    title = span.next.replace(":", "").strip()
                    logger.debug("Title: %s", title)
                    for a_tag in span.find_all("a"):
                        if not isinstance(a_tag, NavigableString):
                            short_description = a_tag.next
                            link = (
                                urlparse(page_url)._asdict()["netloc"]
                                + "/uscert/ncas/alerts"
                                + "/"
                                + title.lower()
                            )
                            if is_url("https://" + link):
                                detailed_link = "https://" + link
                                logger.debug("Short Description: %s", short_description)
                                links.append((detailed_link, short_description, title))
                                logger.info(
                                    "Building RegScale threat from %s.", detailed_link
                                )
                                detailed_link = None
        items = len(cvedivs)
        page += 1
        with ThreadPoolExecutor(max_workers=app.config["maxThreads"]) as executor:
            futures = []
            for link in links:
                logger.info("Building RegScale threat from %s.", link[0])
                futures.append(
                    executor.submit(
                        build_threat,
                        app=app,
                        detailed_link=link[0],
                        short_description=link[1],
                        title=link[2],
                    )
                )
    wait(futures, return_when=ALL_COMPLETED)
    threats = [future.result() for future in futures]
    return threats


def build_threat(app, detailed_link: str, short_description: str, title: str) -> Threat:
    """
    Parse HTML from a given URL/link and build a RegScale threat
    :param app: Application object
    :param str detailed_link: URL of the CISA threat
    :param str short_description: Description of the threat
    :param str title: Title for the threat
    :return: RegScale threat class
    :rtype: Threat
    """
    (
        date_created,
        vulnerability,
        mitigation,
        notes,
    ) = parse_details(detailed_link, app)
    threat = Threat(
        uuid=Threat.xstr(None),
        title=title,
        threatType="Specific",
        threatOwnerId=app.config["userId"],
        dateIdentified=date_created,
        targetType="Other",
        source="Open Source",
        description=short_description if short_description else "",
        vulnerabilityAnalysis="\n".join(vulnerability),
        mitigations="\n".join(mitigation),
        notes="\n".join(notes),
        dateCreated=date_created,
        status="Under Investigation",
    )
    return threat


def parse_details(link: str, app) -> Tuple[str, list, list, list]:
    """
    Parse details
    :param str link: URL to parse
    :param app: Application object
    :raises: AttributeError if unable to find an attribute
    :return: Tuple[create date, vulnerability, mitigation, notes]
    :rtype: Tuple[str, list, list, list]
    """
    nav_string = ""
    vulnerability = []
    mitigation = []
    notes = []
    detailed_soup = gen_soup(link, app)
    headers = None
    dateCreated = fuzzy_find_date(detailed_soup)
    for article in detailed_soup.find_all(
        "article", {"class": "activity-alert full clearfix"}
    ):
        for elements in article.find_all("div", {"class": "content"}):
            for ele in elements:
                if isinstance(ele, Tag):
                    headers = ele.find_all(re.compile("^h[1-6]$"))
                    if headers:
                        for tag in ele.children:
                            if isinstance(tag, Tag):
                                if (
                                    (tag.text).lower()
                                    in ["technical details", "mitigations", "summary"]
                                ) and tag.name == "h3":
                                    nav_string = tag.text.lower()
                                    if isinstance(ele, Tag) and nav_string in [
                                        "technical details",
                                        "mitigations",
                                        "summary",
                                    ]:
                                        try:
                                            nav = nav_string.replace(" ", "-")
                                            sel = f'div[class*="{nav}"]'
                                            content = ele.select(sel)
                                            for cnt in content:
                                                if nav_string.lower() == "summary":
                                                    notes.append(cnt.text)
                                                if (
                                                    nav_string.lower()
                                                    == "technical details"
                                                ):
                                                    vulnerability.append(cnt.text)
                                                if nav_string.lower() == "mitigations":
                                                    mitigation.append(cnt.text)
                                        except AttributeError as ex:
                                            logger.debug("AttributeError: %s", ex)
    return dateCreated, vulnerability, mitigation, notes


def fuzzy_find_date(detailed_soup: BeautifulSoup) -> str:
    """
    Perform a fuzzy find to pull a date from a bs4 object
    :param BeautifulSoup detailed_soup: A BeautifulSoup object representing a webpage
    :raises: dparser.ParserError if unable to parse data
    :return: An ISO-formatted datetime string
    :rtype: str
    """
    fuzzy_dt = None
    try:
        fuzzy_dt = dparser.parse(
            str(detailed_soup.find_all("div", {"class": "submitted meta-text"})[0].text)
            .strip("\n")
            .strip()
            .split("|")[0]
            .strip(),
            fuzzy=True,
        ).isoformat()
    except dparser.ParserError as pex:
        logger.error("Error Processing Alert datecreated: %s.", pex)
    return fuzzy_dt


def gen_soup(url: str, app: Application) -> None:
    """
    Generate a BeautifulSoup instance for the given URL
    :param str url: URL string
    :param app: Application object
    :raises: URLError if URL is unvalid
    :return: None
    """
    if is_url(url):
        req = Api(app).get(url)
        req.raise_for_status()
        content = req.content
        return BeautifulSoup(content, "html.parser")
    raise URLError("URL is invalid, exiting...")


def update_known_vulnerabilities() -> list:
    """
    Pull the latest Known Exploited Vulnerabilities (KEV) data from CISA.
    :raises: Request Exception if unexpected response received from API
    :return: List of known vulnerabilities via API
    :rtype: list
    """
    app = Application()
    api = Api(app)
    config = app.config
    if "cisa_kev" in config:
        cisa_url = config["cisaKev"]
    else:
        cisa_url = (
            "https://www.cisa.gov/sites/default/files/feeds/"
            "known_exploited_vulnerabilities.json"
        )
        config["cisaKev"] = cisa_url
        app.save_config(config)
    response = api.get(url=cisa_url, headers={})
    try:
        response.raise_for_status()
    except exceptions.RequestException as ex:
        # Whoops it wasn't a 200
        logger.error("Error retrieving CISA KEV data: %s.", str(ex))
    # Must have been a 200 status code
    json_obj = response.json()
    return json_obj


def convert_date_string(date_str: str) -> str:
    """
    Convert the given date string for use in RegScale
    :param str date_str: date as a string
    :return: RegScale accepted datetime string format
    :rtype: str
    """
    fmt = "%Y-%m-%d"
    result_dt = datetime.strptime(
        date_str, fmt
    )  # 2022-11-03 to 2022-08-23T03:00:39.925Z
    return result_dt.isoformat() + ".000Z"


def update_regscale(data: dict) -> None:
    """
    Update RegScale threats with the latest Known Exploited Vulnerabilities (KEV) data
    :param dict data: Threat data from CISA
    :return: None
    """
    app = Application()
    api = Api(app)
    config = app.config
    reg_threats = get_all_from_module(api=api, module="threats")
    unique_threats = list(set([reg["description"] for reg in reg_threats]))
    matching_threats = [
        d for d in data["vulnerabilities"] if d["vulnerabilityName"] in unique_threats
    ]
    # reg_threats = api.get(url_threats).json()
    threats_inserted = []
    threats_updated = []
    new_threats = [
        dat for dat in data["vulnerabilities"] if dat not in matching_threats
    ]
    console.print(f"Found {len(new_threats)} new threats from CISA")
    if len([dat for dat in data["vulnerabilities"] if dat not in matching_threats]) > 0:
        for rec in new_threats:

            threat = Threat(
                uuid=Threat.xstr(None),
                title=rec["cveID"],
                threatType="Specific",
                threatOwnerId=config["userId"],
                dateIdentified=convert_date_string(rec["dateAdded"]),
                targetType="Other",
                source="Open Source",
                description=rec["vulnerabilityName"],
                vulnerabilityAnalysis=rec["shortDescription"],
                mitigations=rec["requiredAction"],
                notes=rec["notes"].strip() + " Due Date: " + rec["dueDate"],
                dateCreated=(datetime.now()).isoformat(),
                status="Under Investigation",
            )
            threats_inserted.append(dataclasses.asdict(threat))
    update_threats = [dat for dat in data["vulnerabilities"] if dat in matching_threats]
    if len(matching_threats) > 0:
        for rec in update_threats:
            update_vuln = dataclasses.asdict(
                Threat(
                    uuid=Threat.xstr(None),
                    title=rec["cveID"],
                    threatType="Specific",
                    threatOwnerId=config["userId"],
                    dateIdentified=convert_date_string(rec["dateAdded"]),
                    targetType="Other",
                    description=rec["vulnerabilityName"],
                    vulnerabilityAnalysis=rec["shortDescription"],
                    mitigations=rec["requiredAction"],
                    dateCreated=convert_date_string(rec["dateAdded"]),
                )
            )
            old_vuln = [
                threat
                for threat in reg_threats
                if threat["description"] == update_vuln["description"]
            ][0]
            update_vuln = merge_old(update_vuln=update_vuln, old_vuln=old_vuln)
            if old_vuln:
                threats_updated.append(update_vuln)
    # Update Matching Threats
    url_threats = config["domain"] + "/api/threats"
    if len(threats_inserted) > 0:
        logging.getLogger("urllib3").propagate = False
        api.update_server(
            url=url_threats,
            json_list=threats_inserted,
            method="post",
            config=config,
            message=f"Inserting {len(threats_inserted)} threats to RegScale...",
        )
    update_regscale_threats(json_list=threats_updated)


def merge_old(update_vuln: dict, old_vuln: dict) -> dict:
    """
    Merge dictionaries of old and updated vulnerabilities
    :param dict update_vuln: An updated vulnerability dictionary
    :param dict old_vuln: An old vulnerability dictionary
    :return: A merged vulnerability dictionary
    :rtype: dict
    """
    update_vuln["id"] = old_vuln["id"]
    update_vuln["uuid"] = old_vuln["uuid"]
    update_vuln["status"] = old_vuln["status"]
    update_vuln["source"] = old_vuln["source"]
    update_vuln["threatType"] = old_vuln["threatType"]
    update_vuln["threatOwnerId"] = old_vuln["threatOwnerId"]
    update_vuln["status"] = old_vuln["status"]
    update_vuln["notes"] = old_vuln["notes"]
    update_vuln["mitigations"] = old_vuln["mitigations"]
    update_vuln["targetType"] = old_vuln["targetType"]
    update_vuln["dateCreated"] = old_vuln["dateCreated"]
    # update_vuln['dateLastUpdated'] = old_vuln['dateLastUpdated']
    update_vuln["isPublic"] = old_vuln["isPublic"]
    update_vuln["investigated"] = old_vuln["investigated"]
    if "investigationResults" in old_vuln.keys():
        update_vuln["investigationResults"] = old_vuln["investigationResults"]
    return update_vuln


def insert_or_upd_threat(
    threat: dict, app: Application, threat_id=None
) -> requests.Response:
    """
    Insert or update the given threats in RegScale
    :param dict threat: RegScale threat
    :param app: Application object
    :param threat_id: RegScale ID of the threat, defaults to none
    :return: An API response based on the PUT or POST action
    :rtype: requests.Response
    """
    api = Api(app)
    config = app.config
    url_threats = config["domain"] + "/api/threats"
    headers = {"Accept": "application/json", "Authorization": config["token"]}
    response = None
    if not threat_id:
        response = api.post(url=url_threats, headers=headers, json=threat)

    else:
        response = api.put(
            url=f"{url_threats}/{threat_id}", headers=headers, json=threat
        )
    return response


def update_regscale_threats(
    headers: dict = None,
    json_list=None,
) -> None:
    """
    Update the given threats in RegScale via concurrent POST or PUT of multiple objects
    :param dict headers: Headers used for the RegScale API, defaults to None
    :param json_list: list of threats to be updated, defaults to None
    :return: None
    """
    logging.getLogger("urllib3").propagate = False
    app = Application()
    api = Api(app)
    url_threats = app.config["domain"] + "/api/threats"
    if headers is None and app.config:
        headers = {"Accept": "application/json", "Authorization": app.config["token"]}
    if json_list and len(json_list) > 0:
        api.update_server(
            url=url_threats,
            method="put",
            headers=headers,
            json_list=json_list,
            message="Updating {0} RegScale threats...".format(len(json_list)),
        )


def is_url(url: str) -> bool:
    """
    Determines if the given string is a URL
    :param str url: A candidate URL string
    :return: True if the given string is a URL; false, otherwise
    :rtype: bool
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
