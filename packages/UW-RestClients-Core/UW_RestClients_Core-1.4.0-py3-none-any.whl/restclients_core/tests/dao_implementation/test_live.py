# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase, skipUnless
from commonconf import override_settings
from restclients_core.dao import DAO
from restclients_core.exceptions import DataFailureException
from urllib3.connectionpool import HTTPConnectionPool
from urllib3.exceptions import MaxRetryError, SSLError
import mock
import os


class TDAO(DAO):
    def service_name(self):
        return "live_test"

    def get_default_service_setting(self, key):
        if "DAO_CLASS" == key:
            return "Live"

        if "HOST" == key:
            return "http://localhost:9876/"


class SSLTDAO(DAO):
    def service_name(self):
        return "live_ssl_test"

    def get_default_service_setting(self, key):
        if "DAO_CLASS" == key:
            return "Live"

        if "HOST" == key:
            return "https://localhost:9443/"


class SSLClientCertTDAO(DAO):
    def service_name(self):
        return "live_ssl_test_cert"

    def get_default_service_setting(self, key):
        if "DAO_CLASS" == key:
            return "Live"

        if "HOST" == key:
            return "https://localhost:9443/"

        if "CERT_FILE" == key:
            return "test/certs/client-cert.pem"

        if "KEY_FILE" == key:
            return "test/certs/client_key.pem"


class SSLBadFailTDAO(DAO):
    def service_name(self):
        return "live_ssl_test_fail"

    def get_default_service_setting(self, key):
        if "DAO_CLASS" == key:
            return "Live"

        if "HOST" == key:
            return "https://localhost:9444/"


class SSLBadIgnoreTDAO(DAO):
    def service_name(self):
        return "live_ssl_test_ignore"

    def get_default_service_setting(self, key):
        if "DAO_CLASS" == key:
            return "Live"

        if "HOST" == key:
            return "https://localhost:9444/"

        if "VERIFY_HTTPS" == key:
            return False


@skipUnless("RUN_LIVE_TESTS" in os.environ, "RUN_LIVE_TESTS=1 to run tests")
class TestLive(TestCase):
    def test_found_resource(self):
        response = TDAO().getURL('/ok', {})
        self.assertEquals(response.status, 200)
        self.assertEquals(response.data, b'ok')
        self.assertEquals(response.headers["X-Custom-Header"], "header-test")
        self.assertEquals(response.getheader("X-Custom-Header"), "header-test")

    def test_clear_cached_response(self):
        self.assertIsNone(TDAO().clear_cached_response('/ok'))

    def test_missing_resource(self):
        response = TDAO().getURL('/missing.json', {})
        self.assertEquals(response.status, 404)

    def test_other_status(self):
        response = TDAO().getURL('/403', {})
        self.assertEquals(response.status, 403)

    def test_one_redirect(self):
        response = TDAO().getURL('/301', {})
        self.assertEquals(response.status, 200)
        self.assertEquals(response.data, b'ok')

    def test_multiple_redirects(self):
        self.assertRaises(DataFailureException, TDAO().getURL, '/redirect', {})

        try:
            TDAO().getURL('/redirect', {})
        except DataFailureException as ex:
            self.assertEqual(ex.url, '/redirect')
            self.assertEqual(ex.status, 0)

    @mock.patch.object(HTTPConnectionPool, 'urlopen')
    def test_max_retry_error(self, mock_urlopen):
        mock_urlopen.side_effect = MaxRetryError(None, '/ok')

        self.assertRaises(DataFailureException, TDAO().getURL, '/ok', {})

        try:
            TDAO().getURL('/ok', {})
        except DataFailureException as ex:
            self.assertEqual(ex.url, '/ok')
            self.assertEqual(ex.status, 0)

    def test_settings_defaults(self):
        live_dao = TDAO().get_implementation()

        self.assertEqual(live_dao._get_connect_timeout(), 3)

        with override_settings(RESTCLIENTS_DEFAULT_CONNECT_TIMEOUT=0.2):
            self.assertEqual(live_dao._get_connect_timeout(), 0.2)

        with override_settings(RESTCLIENTS_LIVE_TEST_CONNECT_TIMEOUT=0.1):
            self.assertEqual(live_dao._get_connect_timeout(), 0.1)

        self.assertEqual(live_dao._get_timeout(), 10)

        with override_settings(RESTCLIENTS_LIVE_TEST_TIMEOUT=5):
            self.assertEqual(live_dao._get_timeout(), 5)

        with override_settings(RESTCLIENTS_DEFAULT_TIMEOUT=0.25):
            self.assertEqual(live_dao._get_timeout(), 0.25)

        self.assertEqual(live_dao._get_max_pool_size(), 10)

        with override_settings(RESTCLIENTS_LIVE_TEST_POOL_SIZE=5):
            self.assertEqual(live_dao._get_max_pool_size(), 5)

        with override_settings(RESTCLIENTS_DEFAULT_POOL_SIZE=25):
            self.assertEqual(live_dao._get_max_pool_size(), 25)


@skipUnless("RUN_SSL_TESTS" in os.environ, "RUN_SSL_TESTS=1 to run tests")
class TestLiveSSL(TestCase):
    def test_ssl_found_resource(self):
        response = SSLTDAO().getURL('/ok', {})
        self.assertEquals(response.status, 200)
        self.assertEquals(response.data, b'ok: ')
        self.assertEquals(response.headers["X-Custom-Header"], "header-test")
        self.assertEquals(response.getheader("X-Custom-Header"), "header-test")

    def test_ssl_client_cert(self):
        response = SSLClientCertTDAO().getURL('/ok', {})
        self.assertEquals(response.status, 200)
        self.assertEquals(response.data, b'ok: my.app')

    def test_ssl_non_validated_cert(self):
        self.assertRaises(DataFailureException, SSLBadFailTDAO().getURL, '/')

        try:
            SSLBadFailTDAO().getURL('/')
        except DataFailureException as ex:
            self.assertEqual(ex.url, '/')
            self.assertEqual(ex.status, 0)

    def test_ssl_non_valid_ignore(self):
        response = SSLBadIgnoreTDAO().getURL('/ok', {})
        self.assertEquals(response.status, 200)
        self.assertEquals(response.data, b'ok')
