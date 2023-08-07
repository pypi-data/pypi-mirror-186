#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import sys
import tempfile
from typing import Tuple

import pytest

from app.api import Api
from app.application import Application
from app.internal.login import login
from app.logz import create_logger
from app.public.oscal import process_component, upload_catalog, upload_profile
from app.utils.app_utils import check_file_path
from app.utils.threadhandler import create_threads, thread_assignment

sys.path.append("..")  # Adds higher directory to python modules path.


def delete_inserted_items(args: Tuple, thread: int) -> None:
    """
    Delete items that were added to the catalog
    :return: None
    """
    inserted_items, regscale_module, config, api, logger = args
    headers = {
        "accept": "*/*",
        "Authorization": config["token"],
    }
    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(inserted_items))

    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the recommendation for the thread for later use in the function
        item = inserted_items[threads[i]]

        url = f'{config["domain"]}/api/{regscale_module}/{item["id"]}'
        response = api.delete(url=url, headers=headers)
        if response.status_code == 200:
            logger.info("Deleted #%s from %s\n%s", item["id"], regscale_module, item)
        else:
            logger.error(
                "Unable to delete #%s from %s\n%s",
                item["id"],
                regscale_module,
                item,
            )


class Test_Oscal:
    """Oscal Test Class"""

    logger = create_logger()

    def test_init(self):
        with open("init.yaml", "r", encoding="utf-8") as file:
            data = file.read()
            self.logger.debug("init file: %s", data)
            assert len(data) > 5

    @pytest.mark.skip(
        reason="This test is way too slow and causes too much stress on the database."
    )
    def test_catalog(self):
        """Test Catalog Code"""
        app = Application()
        api = Api(app)
        self.logger.debug(os.getenv("REGSCALE_USER"))
        self.logger.debug(os.getenv("REGSCALE_PASSWORD"))
        check_file_path("processing")
        # Need a runner to allow click to work with pytest
        # Get fresh token
        login(os.getenv("REGSCALE_USER"), os.getenv("REGSCALE_PASSWORD"), app=app)
        file_url = "https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog-min.json"
        tmp_file = tempfile.NamedTemporaryFile(delete=False)
        f = open(tmp_file.name, "w", encoding="utf-8")
        r = api.get(url=file_url, headers={})
        f.write(r.text)
        f.close()
        cat_name = r.json()["catalog"]["metadata"]["title"]
        # Pass default argument to click function
        self.logger.debug(f.name)

        Test_Oscal.upload_catalog(self, f.name)
        # delete extra data after we are finished
        Test_Oscal.delete_catalog_items(self)
        # delete the catalog
        Test_Oscal.delete_inserted_catalog(self, cat_name)
        self.logger.debug(cat_name)
        tmp_file.close()
        os.remove(tmp_file.name)
        # shutil.rmtree('processing')
        # Test_Oscal.delete_inserted_catalog(cat_name)

    def test_profile(self):
        """Test Profile Code"""
        app = Application()
        api = Api(app)
        self.logger.debug(os.getenv("REGSCALE_USER"))
        self.logger.debug(os.getenv("REGSCALE_PASSWORD"))
        if not os.path.exists("processing"):
            os.mkdir("processing")
        # Need a runner to allow click to work with pytest
        # Get fresh token
        login(os.getenv("REGSCALE_USER"), os.getenv("REGSCALE_PASSWORD"), app=app)
        file_url = "https://raw.githubusercontent.com/GSA/fedramp-automation/2229f10cc0b143410522026b793f4947eebb0872/dist/content/baselines/rev4/json/FedRAMP_rev4_HIGH-baseline_profile.json"
        tmp_file = tempfile.NamedTemporaryFile(delete=False)
        r = api.get(url=file_url, headers={})
        f = open(tmp_file.name, "w", encoding="utf-8")
        f.write(r.text)
        f.close()
        prof_name = r.json()["profile"]["metadata"]["title"]
        # Pass default argument to click function
        self.logger.debug(f.name)

        Test_Oscal.upload_profile(self, file_name=f.name, title=prof_name)
        # delete extra data after we are finished
        Test_Oscal.delete_inserted_profile(self, prof_name)
        self.logger.debug(prof_name)
        tmp_file.close()
        os.remove(tmp_file.name)
        # shutil.rmtree('processing')
        # Test_Oscal.delete_inserted_catalog(cat_name)

    def test_component(self):
        app = Application()
        api = Api(app)
        if not os.path.exists("processing"):
            os.mkdir("processing")
        login(os.getenv("REGSCALE_USER"), os.getenv("REGSCALE_PASSWORD"), app=app)
        r = api.get(
            url="https://repo1.dso.mil/platform-one/big-bang/apps/sandbox/loki/-/raw/main/oscal-component.yaml",
            headers={},
        )
        assert r.text
        tmp_file = tempfile.NamedTemporaryFile(delete=False)
        tmp_file.write(bytes(r.text, "utf-8"))
        tmp_file.close()
        os.rename(tmp_file.name, tmp_file.name + ".yaml")
        filename = tmp_file.name + ".yaml"
        process_component(filename)
        os.remove(filename)

    def upload_profile(self, file_name, title) -> None:
        """
        Upload the catalog
        :param str file_name: file path to the catalog to upload to RegScale
        :param str title: title of the catalog
        """
        upload_profile(
            file_name=file_name, title=title, catalog=84, categorization="Moderate"
        )

    def upload_catalog(self, file_name) -> None:
        """Upload the catalog"""
        upload_catalog(file_name=file_name)

    def delete_catalog_items(self):
        """testing out deleting items for a catalog for debugging"""
        app = Application()
        api = Api(app)

        # update api pool limits to max_thread count from init.yaml
        api.pool_connections = (
            app.config["maxThreads"]
            if app.config["maxThreads"] > api.pool_connections
            else api.pool_connections
        )
        api.pool_maxsize = (
            app.config["maxThreads"]
            if app.config["maxThreads"] > api.pool_maxsize
            else api.pool_maxsize
        )
        inserted_items: list[dict] = [
            {"file_name": "newParameters.json", "regscale_module": "controlParameters"},
            {
                "file_name": "newTests.json",
                "regscale_module": "controlTestPlans",
            },
            {
                "file_name": "newObjectives.json",
                "regscale_module": "controlObjectives",
            },
            {
                "file_name": "newControls.json",
                "regscale_module": "securitycontrols",
            },
        ]
        for file in inserted_items:
            with open(
                f".{os.sep}processing{os.sep}{file['file_name']}", "r", encoding="utf-8"
            ) as infile:
                data = json.load(infile)
            create_threads(
                process=delete_inserted_items,
                args=(data, file["regscale_module"], app.config, api, self.logger),
                thread_count=len(data),
            )

    def delete_inserted_catalog(self, cat_name):
        """delete catalog"""
        app = Application()
        api = Api(app)
        config = app.config
        headers = {
            "accept": "*/*",
            "Authorization": config["token"],
        }
        cats = api.get(
            url=config["domain"] + "/api/catalogues/getList", headers=headers
        ).json()
        delete_this_cat = sorted(
            [x for x in cats if x["title"] == cat_name],
            key=lambda d: d["id"],
            reverse=True,
        )[0]
        self.logger.info(delete_this_cat)
        response = api.delete(
            url=f"https://dev.regscale.com/api/catalogues/{delete_this_cat['id']}",
            headers=headers,
        )
        self.logger.info(headers)
        self.logger.info(response)

    def delete_inserted_profile(self, prof_name):
        """delete profile"""
        app = Application()
        api = Api(app)
        config = app.config
        headers = {
            "accept": "*/*",
            "Authorization": config["token"],
        }
        profs = api.get(
            url=config["domain"] + "/api/profiles/getList", headers=headers
        ).json()
        delete_this_prof = sorted(
            [x for x in profs if x["name"] == prof_name],
            key=lambda d: d["id"],
            reverse=True,
        )[0]
        self.logger.info(delete_this_prof)
        response = api.delete(
            url=f"https://dev.regscale.com/api/profiles/{delete_this_prof['id']}",
            headers=headers,
        )
        self.logger.info(headers)
        self.logger.info(response)
