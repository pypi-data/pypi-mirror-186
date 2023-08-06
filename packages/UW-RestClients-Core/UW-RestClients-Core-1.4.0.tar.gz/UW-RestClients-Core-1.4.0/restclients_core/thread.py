# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from commonconf import settings
import threading

try:
    from django.db import connection as db_connection
except ImportError:
    db_connection = None


"""
This is a wrapper around threading.Thread, but it will only actually thread
if django configuration is enabled.  Otherwise, it will be an object with the
same api where start() just calls run().
"""


class Thread(threading.Thread):
    _use_thread = False
    parent = None

    def __init__(self, *args, **kwargs):
        self.parent = threading.currentThread()

        if self._db_compatible:
            self._use_thread = not getattr(
                settings, "RESTCLIENTS_DISABLE_THREADING", False)

        else:
            self._use_thread = getattr(
                settings, "RESTCLIENTS_USE_THREADING", False)

        super(Thread, self).__init__(*args, **kwargs)

    @property
    def _db_compatible(self):
        return db_connection is not None and db_connection.vendor != 'sqlite'

    def start(self):
        if self._use_thread:
            super(Thread, self).start()

        else:
            # Needed to test failures in the threads.
            # But it can't be on all the time - sqlite dbs aren't shared to
            # threads.
            if getattr(settings, "RESTCLIENTS_USE_INLINE_THREADS", False):
                super(Thread, self).start()
                super(Thread, self).join()
            else:
                self.run()

    def join(self):
        if self._use_thread:
            return super(Thread, self).join()
        return True

    def close_db_connection(self):
        if (self._use_thread and db_connection is not None and
                not db_connection.in_atomic_block):
            db_connection.close()


class GenericPrefetchThread(Thread):
    method = None

    def run(self):
        if self.method is None:
            return
        try:
            self.method()
        except Exception as ex:
            # Errors in prefetching should also manifest during actual
            # processing, where they can be handled appropriately
            pass

        self.close_db_connection()


def generic_prefetch(method, args):
    def ret():
        return method(*args)
    return ret
