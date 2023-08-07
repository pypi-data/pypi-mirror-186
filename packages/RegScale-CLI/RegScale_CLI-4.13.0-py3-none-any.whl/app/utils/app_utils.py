#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Functions used throughout the application """

# standard python imports
import csv
import glob
import json
import ntpath
import os
import re
import sys
from datetime import datetime
from collections.abc import MutableMapping
from pathlib import Path
from tempfile import gettempdir

import pandas as pd
import requests
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
)

from app.application import Application
from app.internal.login import is_licensed
from app.logz import create_logger
from exceptions.license_exception import LicenseException

logger = create_logger()


def check_license() -> Application:
    """
    Check RegScale license
    :raises: LicenseException if Application license isn't at the requested level of the feature
    :return: Application object
    """
    app = Application()
    if not is_licensed(app):
        raise LicenseException(
            "This feature is limited to RegScale Enterprise, please check RegScale license."
        )
    return app


def validate_mac_address(mac_address: str) -> bool:
    """
    Simple validation of a mac address input
    :param str mac_address: mac address
    :return: Whether mac address is valid or not
    :rtype: bool
    """
    if re.match(
        "[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address.lower()
    ):
        return True
    return False


def str_to_date(date_str: str) -> datetime:
    """
    Function to convert string into a date object
    :param str date_str:
    :return: datetime object of provided string date
    :rtype: datetime
    """
    # replace the T with a space and create list of result
    date_str = date_str.replace("T", " ").split(" ")

    # convert the first part of the date list into a date
    date = datetime.strptime(date_str[0], "%Y-%m-%d")

    # return date result
    return date


def uncamel_case(camel_str: str) -> str:
    """
    Function to convert camelCase strings to Title Case
    :param camel_str:
    :return: Title Case string from provided camelCase
    :rtype: str
    """
    # check to see if a string with data was passed
    if camel_str != "":
        # split at any uppercase letters
        result = re.sub("([A-Z])", r" \1", camel_str)

        # use title to Title Case the string and strip to remove leading
        # and trailing white spaces
        result = result.title().strip()
        return result
    return ""


def get_css(file_path: str) -> str:
    """
    Function to load the CSS properties from the given file_path
    :param str file_path: file path to the desired CSS file
    :return: CSS as a string
    :rtype: str
    """
    # create variable to store the string and return
    css = ""

    # check if the filepath exists before trying to open it
    if os.path.exists(file_path):
        # file exists so open the file
        with open(file_path, "r", encoding="utf-8") as file:
            # store the contents of the file in the css str variable
            css = file.read()
    # return the css variable
    return css


def epoch_to_datetime(epoch: str, format="%Y-%m-%d %H:%M:%S") -> str:
    """
    Return datetime from unix epoch
    :param str epoch: unix epoch
    :param str format: datetime string format, defaults to "%Y-%m-%d %H:%M:%S"
    :return: datetime string
    :rtype: str
    """
    return datetime.fromtimestamp(int(epoch)).strftime(format)


def get_current_datetime(format="%Y-%m-%d %H:%M:%S") -> str:
    """
    Return current datetime
    :param str format: desired format for datetime string, defaults to "%Y-%m-%d %H:%M:%S"
    :return: Current datetime as a string
    :rtype: str
    """
    return datetime.now().strftime(format)


def cci_control_mapping(file_path: Path) -> list:
    """
    Simple function to read csv artifact to help with STIG mapping
    :param Path file_path: file path to the csv artifact
    :return: List of the csv contents
    :rtype: list
    """
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)


def create_progress_object() -> Progress:
    """
    Function to create and return a progress object
    :return: Progress object for live progress in console
    :rtype: Progress
    """
    job_progress = Progress(
        "{task.description}",
        SpinnerColumn(),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
    )
    return job_progress


def get_file_type(file_name: str) -> str:
    """
    Function to get the file type of the provided file_path and returns it as a string
    :param str file_name: Path to the file
    :return: Returns string of file type
    :rtype: str
    """
    file_type = Path(file_name).suffix
    return file_type.lower()


def get_file_name(file_path: str) -> str:
    """
    Function to parse the provided file path and returns the file's name as a string
    :param str file_path: path to the file
    :return: File name
    :rtype: str
    """
    # split the provided file_path with ntpath
    directory, file_name = ntpath.split(file_path)
    # return the file_path or directory
    return file_name or ntpath.basename(directory)


def get_recent_files(file_path: Path, file_count: int, file_type: str = None) -> list:
    """
    Function to go to the provided file_path and get the x number of recent items
    optional argument of file_type to filter the directory
    :param Path file_path: Directory to get recent files in
    :param int file_count: # of files to return
    :param str file_type: file type to sort directory for, defaults to none
    :return: list of recent files in the provided directory
    :rtype: list
    """
    # verify the provided file_path exists
    if os.path.exists(file_path):
        # get the list of files from the provided path, get the desired
        # file_type if provided
        file_list = (
            glob.glob(f"{file_path}/*{file_type}")
            if file_type
            else glob.glob(f"{file_path}/*")
        )

        # sort the file_list by modified date in descending order
        file_list.sort(key=os.path.getmtime, reverse=True)

        # check if file_list has more items than the provided number, remove the rest
        if len(file_list) > file_count:
            file_list = file_list[:file_count]
    else:
        error_and_exit(f"The provided file path doesn't exist! Provided: {file_path}")
    # return the list of files
    return file_list


def check_file_path(file_path) -> None:
    """
    Function to check the provided file path, if it doesn't exist it will be created
    :param file_path: Path to the directory
    :return: None
    """
    # see if the provided directory exists, if not create it
    if not os.path.exists(file_path):
        os.mkdir(file_path)
        # notify user directory has been created
        logger.info("%s didn't exist, but has been created.", file_path)


def error_and_exit(error_desc: str) -> None:
    """
    Function to display and log the provided error_desc and exits the application
    :param str error_desc: Description of the error encountered
    :return: None
    """
    logger.error(error_desc)
    sys.exit(1)


def download_file(url: str, download_path: Path = gettempdir()) -> Path:
    """
    Download file from the provided url and save it to the provided download_path
    :param str url: URL location of the file to download
    :param Path download_path: Path to download the file to
    :return: Path to the downloaded file
    :rtype: Path
    """
    download_path = Path(download_path)
    local_filename = url.split("/")[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True, timeout=10) as response:
        response.raise_for_status()
        with open(download_path / local_filename, "wb+") as file:
            for chunk in response.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                file.write(chunk)
    return download_path / local_filename


def capitalize_words(word: str) -> str:
    """
    Function to convert string to title case
    :param str word: Desired string to process
    :return: str
    """
    return re.sub(r"\w+", lambda m: m.group(0).capitalize(), word)


def save_data_to(file_name: str, file_type: str, data) -> None:
    """
    Function to save the provided data to the provided file_name and file_type
    :param str file_name: Desired name to save the file as
    :param str file_type: Desired file type
    :param data: The data to save to the file
    :raises: PermissionError if the file already exists and is opened
    :raises: TypeError if data provided for json cannot be converted to a json object
    :raises: General Error if unable to save json data with .write() after trying json.dump() method
    :return: None
    """
    logger.info("Prepping data to be saved to: %s%s", file_name, file_type)

    if file_type in [".csv", ".xlsx"]:
        # convert the provided data to a pandas dataframe
        df = pd.DataFrame(data)

        # transpose the dataset
        df = df.transpose()

    # check the file type, so we can export the data to the correct file
    if file_type.lower() == ".csv":
        try:
            # try to save the data as a csv file
            df.to_csv(file_name + file_type)
            logger.info("Data successfully saved to: %s%s", file_name, file_type)
        except PermissionError:
            error_and_exit(
                f"Unable to save {file_name}{file_type}. Please verify it is closed and try again."
            )
    elif file_type.lower() == ".xlsx":
        try:
            # try save the data as a xlsx file
            df.to_excel(file_name + file_type)
            logger.info("Data successfully saved to: %s%s", file_name, file_type)
        except PermissionError:
            # notify user unable to save because the file is open
            error_and_exit(
                f"Unable to save {file_name}{file_type}. Please verify it is closed and try again."
            )
    elif file_type.lower() == ".json":
        try:
            with open(file_name + file_type, "w", encoding="utf-8") as outfile:
                json.dump(data, outfile, indent=4)
            logger.info("Data successfully saved to %s%s", file_name, file_type)
        except json.JSONDecodeError as err:
            error_and_exit(
                f"Unable to save {file_name}{file_type} due to a decode error.\n{err}\n{data}"
            )
        except TypeError:
            try:
                with open(file_name, "w", encoding="utf-8") as outfile:
                    outfile.write(data)
                logger.info("Data successfully saved to %s%s", file_name, file_type)
            except Exception as err:
                error_and_exit(
                    f"Unable to save {file_name}{file_type} due to an unexpected error.\nError: {err}\n{data}"
                )
    else:
        # notify the user an incorrect file type was provided
        error_and_exit(f"Unsupported file type provided, {file_type} is not supported.")


def remove_nested_dict(data: dict, skip_keys: list = None) -> dict:
    """
    Function to remove nested dictionaries in the provided dictionary,
    also allows the option to remove a key from the provided dictionary
    :param dict data: The raw data that needs to have nested dictionaries removed
    :param list skip_keys: List of Keys to skip during iteration of the provided dict
    :return: Clean dictionary without nested dictionaries
    :rtype: dict
    """
    # create blank dictionary to store the clean dictionary
    result = {}
    # iterate through the keys and values in the provided dictionary
    for key, value in data.items():
        # see if skip_key was provided and if the current key == skip_key
        if skip_keys and key in skip_keys:
            # continue to the next key
            continue
        # check if the item is a nested dictionary
        elif type(value) is dict:
            # evaluate the nested dictionary passing the nested dictionary and skip_key
            new_keys = remove_nested_dict(value, skip_keys=skip_keys)
            # update the value to a non-nested dictionary
            result[key] = value
            # iterate through the keys of the nested dictionary
            for inner_key in new_keys:
                # make sure key doesn't already exist in result
                if f"{key}_{inner_key}" in result:
                    last_char = inner_key[-1]
                    # see if the inner_key ends with a number
                    if isinstance(last_char, int):
                        # increment the number by 1 and replace the old one with the new one
                        last_char += 1
                        inner_key[-1] = last_char
                    else:
                        inner_key += "2"
                # combine the key + nested key and store it into the clean dictionary
                result[f"{key}_{inner_key}"] = result[key][inner_key]
        else:
            # item isn't a nested dictionary, save the data
            result[key] = value
    # return the un-nested dictionary
    return result


def flatten_dict(data: MutableMapping) -> MutableMapping:
    """

    :param data: data that needs to be flattened
    :return: A flattened dictionary that has camelcase keys
    :rtype: MutableMapping
    """
    # create variable to store the clean and flattened dictionary
    flat_dict_clean = {}

    # flatten the dictionary using panda's json_normalize function
    [flat_dict] = pd.json_normalize(data, sep="@").to_dict(orient="records")

    # iterate through the keys to camelcase them and
    for key, value in flat_dict.items():
        # find the location of all the @, which are the separator for nested keys
        sep_locations = key.find("@")

        # check if there are more than one period
        if isinstance(sep_locations, list):
            # iterate through the period locations
            for period in sep_locations:
                # capitalize the character following the period
                key = key[:period] + key[period + 1].upper() + key[period + 2 :]

                # remove the @
                key = key.replace("@", "")
            # add the cleaned key with the original value
            flat_dict_clean[key] = value
        elif sep_locations == -1:
            # no period find
            flat_dict_clean[key] = value
        else:
            # capitalize the character following the @
            key = (
                key[:sep_locations]
                + key[sep_locations + 1].upper()
                + key[sep_locations + 2 :]
            )

            # remove the @
            key = key.replace("@", "")

            # add the cleaned key with the original value
            flat_dict_clean[key] = value

    return flat_dict_clean
