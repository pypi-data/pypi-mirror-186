# Base class and utils for UW REST Clients

[![Build Status](https://github.com/uw-it-aca/uw-restclients-core/workflows/tests/badge.svg?branch=main)](https://github.com/uw-it-aca/uw-restclients-core/actions)
[![Coverage Status](https://coveralls.io/repos/uw-it-aca/uw-restclients-core/badge.svg?branch=main)](https://coveralls.io/r/uw-it-aca/uw-restclients-core?branch=main)
[![PyPi Version](https://img.shields.io/pypi/v/uw-restclients-core.svg)](https://pypi.python.org/pypi/uw-restclients-core)
![Python versions](https://img.shields.io/pypi/pyversions/uw-restclients-core.svg)


This module provides useful interfaces for webservice clients.

If you're writing an application that includes mock resource files, you'll want to include code like this somewhere in your application's startup process:

```
from restclients_core.dao import MockDAO
import os
custom_path = os.path.join(abspath(dirname(__file__), "app_resources"))
MockDAO.register_mock_path(custom_path)
```

For more information, see https://github.com/uw-it-aca/uw-restclients-core/wiki/Mock-resources

If you're writing a webservice client, here is some documentation: https://github.com/uw-it-aca/uw-restclients-core/wiki/Writing-a-webservice-client

If you want to contribute, please send a pull request to the develop branch, or submit an issue.
