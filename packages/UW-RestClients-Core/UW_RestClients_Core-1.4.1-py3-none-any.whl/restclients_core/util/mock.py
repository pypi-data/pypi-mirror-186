# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

import re
import os
from os.path import isfile, join, dirname
import json
from urllib.parse import unquote
from restclients_core.exceptions import DataFailureException
from restclients_core.models import MockHTTP


def load_resource_from_path(resource_dir,
                            service_name,
                            implementation_name,
                            url,
                            headers):
    if url == "///":
        # Just a placeholder to put everything else in an else.
        # If there are things that need dynamic work, they'd go here
        pass
    else:
        response = MockHTTP()
        response.status = 404
        response.headers = None
        RESOURCE_ROOT = os.path.join(resource_dir,
                                     service_name,
                                     implementation_name)
        orig_file_path = RESOURCE_ROOT + url

        handle = open_file(orig_file_path)
        if handle is not None:
            response.status = 200
            response.data = handle.read()

        header_handle = open_file(orig_file_path + ".http-headers")
        if header_handle is not None:
            __read_header(header_handle, response, service_name)

        # Check query permutations even on success
        # so that if there are multiple files we throw an exception
        if "?" in url:
            handle = attempt_open_query_permutations(
                url, orig_file_path, False)
            if handle is not None and response.status == 404:
                response.status = 200
                response.data = handle.read()

            header_handle = attempt_open_query_permutations(
                url, orig_file_path, True)
            if header_handle is not None and response.headers is None:
                __read_header(header_handle, response, service_name)
        return response


def __read_header(header_handle, response, service_name):
    try:
        data = header_handle.read()
        file_values = json.loads(data)

        if response.headers is None:
            response.headers = {
                "X-Data-Source": service_name + " file mock data",
            }

        if "headers" in file_values:
            response.headers.update(file_values['headers'])

            if 'status' in file_values:
                response.status = file_values['status']
        else:
            response.headers.update(file_values)
    except UnicodeDecodeError:
        pass
    except IOError:
        pass


def convert_to_platform_safe(dir_file_name):
    """
    :param dir_file_name: a string to be processed
    :return: a string with all the reserved characters replaced
    """
    return re.sub(r'[\?|<>=:*,;+&"@$]', '_', dir_file_name)


def open_file(orig_file_path):
    """
    Taking in a file path, attempt to open mock data files with it.
    """
    unquoted = unquote(orig_file_path)
    paths = [
        convert_to_platform_safe(orig_file_path),
        "{}/index.html".format(convert_to_platform_safe(orig_file_path)),
        orig_file_path,
        "{}/index.html".format(orig_file_path),
        convert_to_platform_safe(unquoted),
        "{}/index.html".format(convert_to_platform_safe(unquoted)),
        unquoted,
        "{}/index.html".format(unquoted),
        ]

    file_path = None
    handle = None
    for path in paths:
        try:
            file_path = path
            handle = open(path, "rb")
            break
        except IOError:
            pass

    return handle


def attempt_open_query_permutations(url, orig_file_path, is_header_file):
    """
    Attempt to open a given mock data file with different permutations of the
    query parameters
    """
    directory = dirname(convert_to_platform_safe(orig_file_path)) + "/"

    # get all filenames in directory
    try:
        filenames = [f for f in os.listdir(directory)
                     if isfile(join(directory, f))]
    except OSError:
        return

    # ensure that there are not extra parameters on any files
    if is_header_file:
        filenames = [f for f in filenames if ".http-headers" in f]
        filenames = [f for f in filenames if
                     _compare_file_name(orig_file_path + ".http-headers",
                                        directory,
                                        f)]
    else:
        filenames = [f for f in filenames if ".http-headers" not in f]
        filenames = [f for f in filenames if _compare_file_name(orig_file_path,
                                                                directory,
                                                                f)]

    url_parts = url.split("/")
    url_parts = url_parts[len(url_parts) - 1].split("?")

    base = url_parts[0]
    params = url_parts[1]

    params = params.split("&")

    # check to ensure that the base url matches
    filenames = [f for f in filenames if f.startswith(base)]

    params = [convert_to_platform_safe(unquote(p)) for p in params]

    # ensure that all parameters are there
    for param in params:
        filenames = [f for f in filenames if param in f]

    # if we only have one file, return it
    if len(filenames) == 1:
        path = join(directory, filenames[0])
        return open_file(path)

    # if there is more than one file, raise an exception
    if len(filenames) > 1:
        raise DataFailureException(url,
                                   "Multiple mock data files matched the " +
                                   "parameters provided!",
                                   404)


def _compare_file_name(orig_file_path, directory, filename):
    return (len(unquote(orig_file_path)) - len(unquote(directory)) ==
            len(unquote(filename)))
