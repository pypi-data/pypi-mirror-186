# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase
from restclients_core import models
from datetime import datetime


class TestModelCleanMethods(TestCase):
    def test_date_clean(self):
        class ModelTest(models.Model):
            d1 = models.DateField()

        now = datetime.now()
        m1 = ModelTest(d1=now)

        self.assertEquals(now, m1.d1)
        m1.clean_fields()
        self.assertEquals(now.date(), m1.d1)
