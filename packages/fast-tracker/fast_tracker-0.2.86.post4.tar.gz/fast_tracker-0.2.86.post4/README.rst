======================
天眼Python探针
======================


"fast_tracker" base on Apache SkyWalking Python agent and Newrelic Python:

https://github.com/newrelic/newrelic-python-agent

https://github.com/apache/skywalking-python

Installation
------------

.. code:: bash

    $ pip install fast-tracker

Usage
-----

1. 配置好配置文件FastTracker.json.



2. Validate the agent configuration and test the connection to our data collector service.

   .. code:: bash

      $ FastTracker_ConfigPath=FastTracker.json fast-boot run-program $YOUR_COMMAND_OPTIONS

   Examples:

   .. code:: bash

      $ FastTracker_ConfigPath=FastTracker.json FastTracker_Debug_Level=true  fast-boot run-program hug -f app.py


License
-------

FAST for Python is free-to-use, proprietary software. Please see the LICENSE file in the distribution for details on the FAST License agreement and the licenses of its dependencies.

Copyright
---------

Copyright (c) 2019-2020 FAST, Inc. All rights reserved.