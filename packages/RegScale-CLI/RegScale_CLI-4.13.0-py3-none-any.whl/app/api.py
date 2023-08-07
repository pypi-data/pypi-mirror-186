#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" standard imports """

import concurrent.futures
import sys
from typing import Tuple

import requests
from requests.adapters import HTTPAdapter, Retry
from rich.progress import Progress

from app.application import Application
from app.logz import create_logger


class Api:
    """Wrapper for interacting with the RegScale API"""

    def __init__(self, app: Application):
        """
        Initialize API object
        :param app: Application object
        """
        logger = create_logger()
        self.app = app
        self.timeout = 10
        config = app.config
        self.config = config
        self.accept = "application/json"
        self.content_type = "application/json"
        self.logger = logger
        r_session = requests.Session()
        self.pool_connections = 200
        self.pool_maxsize = 200
        if "ssl_verify" in self.config:
            r_session.verify = self.config["ssl_verify"]
        if "timeout" in self.config:
            self.timeout = self.config["timeout"]
        retries = Retry(
            total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504]
        )
        # get the user's domain prefix eg https:// or http://
        domain = config["domain"]
        domain = domain[: (domain.find("://") + 3)]
        r_session.mount(
            domain,
            HTTPAdapter(
                max_retries=retries,
                pool_connections=self.pool_connections,
                pool_maxsize=self.pool_maxsize,
                pool_block=False,
            ),
        )
        self.session = r_session
        self.auth = None

    def get(
        self, url: str, headers: dict = None, params: Tuple = None
    ) -> requests.models.Response:
        """
        Get Request for API
        :param str url: URL for API call
        :param dict headers: headers for the api get call, defaults to None
        :param Tuple params: any parameters for the API call, defaults to None
        :return: Requests response
        :rtype: requests.models.Response
        """
        if self.auth:
            self.session.auth = self.auth
        if headers is None:
            headers = {
                "Authorization": self.config["token"],
                "accept": self.accept,
                "Content-Type": self.content_type,
            }
        try:
            response = self.session.get(
                url=self.normalize_url(url),
                headers=headers,
                params=params,
                timeout=self.timeout,
            )
        except requests.exceptions.RequestException as ex:
            self.logger.error("Unable to login to Regscale, exiting.\n%s", ex)
            sys.exit(1)
        return response

    def delete(self, url: str, headers: dict = None) -> requests.models.Response:
        """
        Delete data using API
        :param url: URL for the API call
        :param headers: headers for the API call, defaults to None
        :return: API response
        :rtype: requests.models.Response
        """
        if self.auth:
            self.session.auth = self.auth
        if headers is None:
            headers = {
                "Authorization": self.config["token"],
                "accept": self.accept,
            }
        return self.session.delete(url=self.normalize_url(url), headers=headers)

    def post(
        self,
        url: str,
        headers: dict = None,
        json: dict = None,
        data: dict = None,
        files: list = None,
    ) -> requests.models.Response:
        """
        Post data to API
        :param str url: URL for the API call
        :param dict headers: Headers for the API call, defaults to None
        :param dict json: Dictionary of data for the API call, defaults to None
        :param dict data: Dictionary of data for the API call, defaults to None
        :param list files: Files to post during API call, defaults to None
        :return: API response
        :rtype: requests.models.Response
        """
        if self.auth:
            self.session.auth = self.auth
        if headers is None:
            try:
                headers = {
                    "Authorization": self.config["token"],
                }
            except KeyError as kex:
                self.config["token"] = "Please Enter Token"
                self.app.save_config(self.config)
                self.logger.error(
                    "Token not found in init.yaml, but we have added it. Please login again.\n%s",
                    kex,
                )
        if not json and data:
            response = self.session.post(
                url=self.normalize_url(url),
                headers=headers,
                data=data,
                files=files,
                timeout=self.timeout,
            )
        else:
            response = self.session.post(
                url=self.normalize_url(url),
                headers=headers,
                json=json,
                files=files,
                timeout=self.timeout,
            )
        self.logger.debug("URL: %s, headers: %s, data: %s", url, headers, json)
        return response

    def put(
        self, url: str, headers: dict = None, json: dict = None
    ) -> requests.models.Response:
        """
        Update data via API call
        :param str url: URL for the API call
        :param dict headers: Headers for the API call, defaults to None
        :param dict json: Dictionary of data for the API call, defaults to None
        :return: API response
        :rtype: requests.models.Response
        """
        if self.auth:
            self.session.auth = self.auth
        if headers is None:
            headers = {
                "Authorization": self.config["token"],
            }
        response = self.session.put(
            url=self.normalize_url(url),
            headers=headers,
            json=json,
            timeout=self.timeout,
        )
        self.logger.debug(response.text)
        return response

    def update_server(
        self,
        url: str,
        headers: dict = None,
        json_list=None,
        method: str = "post",
        config: dict = None,
        message: str = "Working",
    ) -> None:
        """
        Concurrent Post or Put of multiple objects
        :param str url: URL for the API call
        :param dict headers: Headers for the API call, defaults to None
        :param json_list: Dictionary of data for the API call, defaults to None
        :param str method: Method for API to use, defaults to "post"
        :param dict config: Config for the API, defaults to None
        :param str message: Message to display in console, defaults to "Working"
        :raises: General Exception if response status code != 200
        :return: None
        """
        if headers is None and config:
            headers = {"Accept": "application/json", "Authorization": config["token"]}
        if json_list and len(json_list) > 0:
            with Progress(transient=False) as progress:
                task = progress.add_task(message, total=len(json_list))
                with concurrent.futures.ThreadPoolExecutor(
                    max_workers=self.config["maxThreads"]
                ) as executor:
                    if method.lower() == "post":
                        result_futures = list(
                            map(
                                lambda x: executor.submit(self.post, url, headers, x),
                                json_list,
                            )
                        )
                    if method.lower() == "put":
                        result_futures = list(
                            map(
                                lambda x: executor.submit(
                                    self.put, url + f"/{x['id']}", headers, x
                                ),
                                json_list,
                            )
                        )
                    if method.lower() == "delete":
                        result_futures = list(
                            map(
                                lambda x: executor.submit(
                                    self.delete, url + f"/{x['id']}", headers
                                ),
                                json_list,
                            )
                        )
                    for future in concurrent.futures.as_completed(result_futures):
                        try:
                            if future.result().status_code != 200:
                                self.logger.warning(
                                    "Status code is %s.", future.result().status_code
                                )
                            progress.update(task, advance=1)
                        except Exception as ex:
                            self.logger.error("Error is %s, type: %s", ex, type(ex))

    def normalize_url(self, url: str) -> str:
        """
        Function to remove extra slashes and trailing slash from a given URL.
        :param str module: url
        :return: A normalized URL.
        :rtype: str
        """
        url = str(url)
        segments = url.split("/")
        correct_segments = []
        for segment in segments:
            if segment != "":
                correct_segments.append(segment)
        first_segment = str(correct_segments[0])
        if first_segment.find("http") == -1:
            correct_segments = ["http:"] + correct_segments
        correct_segments[0] = correct_segments[0] + "/"
        normalized_url = "/".join(correct_segments)
        return normalized_url
