# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from restclients_core.tests.dao_implementation.test_backend import TDAO
from unittest import TestCase
from prometheus_client import generate_latest, REGISTRY


class TestPrometheusObservations(TestCase):
    def test_prometheus_observation(self):
        response = TDAO().getURL('/ok')

        metrics = generate_latest(REGISTRY).decode('utf-8')
        self.assertRegexpMatches(
            metrics,
            r'.*\nrestclient_request_duration_seconds_bucket{le="0.005",'
            r'service="backend_test"} [1-9].*', metrics)
        self.assertRegexpMatches(
            metrics,
            r'.*\nrestclient_response_status_code_bucket{le="200.0",'
            r'service="backend_test"} [1-9].*', metrics)
        self.assertIn('restclient_request_timeout_total counter', metrics)
        self.assertIn('restclient_request_ssl_error_total counter', metrics)
