# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase
from commonconf import settings, override_settings
from restclients_core.thread import Thread
from mock import patch


class MockSQLite():
    vendor = 'sqlite'


class MockMySQL():
    vendor = 'mysql'


class TestThread(TestCase):
    @patch('restclients_core.thread.db_connection', MockMySQL)
    def test_use_threading_mysql(self):
        thread = Thread()
        self.assertTrue(thread._use_thread)

        with override_settings(RESTCLIENTS_DISABLE_THREADING=True):
            thread = Thread()
            self.assertFalse(thread._use_thread)

        with override_settings(RESTCLIENTS_DISABLE_THREADING=False):
            thread = Thread()
            self.assertTrue(thread._use_thread)

    @patch('restclients_core.thread.db_connection', MockSQLite)
    def test_use_threading_sqlite(self):
        thread = Thread()
        self.assertFalse(thread._use_thread)

        with override_settings(RESTCLIENTS_DISABLE_THREADING=True):
            thread = Thread()
            self.assertFalse(thread._use_thread)

        with override_settings(RESTCLIENTS_DISABLE_THREADING=False):
            thread = Thread()
            self.assertFalse(thread._use_thread)

    def test_use_threading_nodb(self):
        thread = Thread()
        self.assertFalse(thread._use_thread)

        with override_settings(RESTCLIENTS_USE_THREADING=True):
            thread = Thread()
            self.assertTrue(thread._use_thread)

        with override_settings(RESTCLIENTS_USE_THREADING=False):
            thread = Thread()
            self.assertFalse(thread._use_thread)
