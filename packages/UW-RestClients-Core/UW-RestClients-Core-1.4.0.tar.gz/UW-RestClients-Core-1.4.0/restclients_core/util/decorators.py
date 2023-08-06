# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from commonconf import override_settings


def use_mock(*args):
    kw_args = {}

    for service in args:
        key = "RESTCLIENTS_{}_DAO_CLASS".format(
            service.service_name().upper())

        kw_args[key] = 'Mock'

    return override_settings(**kw_args)
