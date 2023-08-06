*************************
ByteBlower Test Framework
*************************

  An easy accessible library of basic test flows and reporting engines.

.. footer::
   Copyright |copy| |year| - Excentis N.V.

.. |registered| unicode:: U+00AE .. registered sign
.. |copy| unicode:: U+00A9 .. copyright sign
.. |year| date:: %Y

ByteBlower |registered| is a traffic generator/analyser system
for TCP/IP networks.

This library provides you with the building blocks for:

#. Generating test traffic
#. Collect statistics
#. Analyse traffic statistics
#. Generate reports

Requirements
============

* byteblowerll_ (`ByteBlower API`_): Our lower layer API for client-server
  communication (`API documentation <https://api.byteblower.com/python>`_)
* scapy_: Used for frame generation and parsing
* junit-xml_: Used for Unit test report generation
* pandas_: Used for data collection
* python-highcharts_: Used for generating graphs
* jinja2_: User for HTML report templating

.. _ByteBlower API: https://setup.byteblower.com/
.. _byteblowerll: https://pypi.org/project/byteblowerll/
.. _scapy: https://pypi.org/project/scapy/
.. _junit-xml: https://pypi.org/project/junit-xml/
.. _pandas: https://pypi.org/project/pandas/
.. _python-highcharts: https://pypi.org/project/python-highcharts/
.. _jinja2: https://pypi.org/project/Jinja2/

Supported platforms
-------------------

The ByteBlower Test Framework in general supports Python version 3.7 to 3.9.

.. note::
   **NOTE**: *Python >= 3.10 is not yet supported because of an issue with
   one of the dependent Python libraries* (`python-highcharts`_).

The framework has been tested for the following operating system platforms
and Python versions:

+------------------+----------------------------+----------------+------------------------+
| OS platform      | Distribution               | Python version | source                 |
+==================+============================+================+========================+
| Windows 10       | up to feature release 21H2 | Python 3.9     | `Official Python`_     |
+------------------+----------------------------+----------------+------------------------+
| Windows 10       | up to feature release 21H2 | Python 3.8     | `Official Python`_     |
+------------------+----------------------------+----------------+------------------------+
| Windows 10       | up to feature release 21H2 | Python 3.7     | `Official Python`_     |
+------------------+----------------------------+----------------+------------------------+
| Windows 10       | up to feature release 21H2 | Python 3.9     | `Windows Apps`_        |
+------------------+----------------------------+----------------+------------------------+
| Windows 10       | up to feature release 21H2 | Python 3.8     | `Windows Apps`_        |
+------------------+----------------------------+----------------+------------------------+
| Windows 10       | up to feature release 21H2 | Python 3.7     | `Windows Apps`_        |
+------------------+----------------------------+----------------+------------------------+
| macOS            | up to Monterey             | Python 3.9     | `Official Python`_     |
|                  |                            |                | (**Intel-only!**)      |
+------------------+----------------------------+----------------+------------------------+
| macOS            | up to Monterey             | Python 3.8     | `Official Python`_     |
|                  |                            |                | (**Intel-only!**)      |
+------------------+----------------------------+----------------+------------------------+
| Linux            | Debian 11 (bullseye)       | Python 3.9.2   | `Debian packages`_     |
+------------------+----------------------------+----------------+------------------------+
| Linux            | Debian 10 (buster)         | Python 3.7.3   | `Debian packages`_     |
+------------------+----------------------------+----------------+------------------------+
| Linux            | Ubuntu 20.04 (Focal Fossa) | Python 3.8.2   | `Ubuntu packages`_     |
+------------------+----------------------------+----------------+------------------------+
| Docker           | python:3.7-slim-buster     | Python 3.7.3   | `Docker Python`_       |
+------------------+----------------------------+----------------+------------------------+

.. _Official Python: https://www.python.org
.. _Windows Apps: https://apps.microsoft.com/
.. _Debian packages: https://packages.debian.org/search?suite=all&exact=1&searchon=names&keywords=python3
.. _Ubuntu packages: https://packages.ubuntu.com/search?keywords=python3&searchon=names&exact=1&suite=all&section=all
.. _Docker Python: https://hub.docker.com/_/python

Installation
============

Prepare runtime environment
---------------------------

We encourage to manage the runtime environment in a Python virtual
environment. This guarantees proper separation of the system-wide
installed Python and pip packages.

Python virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^

Using Python ``venv`` (*included in Python >= 3.3*):

Prepare Python virtual environment: Create the virtual environment
and install/update ``pip`` and ``build``.

.. note::
   **NOTE**: *Mind the leading* ``.`` *which means* **sourcing**
   ``./env/bin/activate``.

.. code-block:: shell

   python3 -m venv env
   . ./env/bin/activate
   pip install -U pip build

Install the ByteBlower Test Framework from PyPI
-----------------------------------------------

First make sure that your *activated* your virtual environment:

.. code-block:: shell

   . ./env/bin/activate

Now install (or update) the ByteBlower Test Framework:

.. code-block:: shell

   python3 -m pip install -U byteblower-test-framework

Documentation
=============

Online usage documentation: `ByteBlower Test Framework documentation`_

.. _ByteBlower Test Framework documentation: https://api.byteblower.com/test-framework/latest/

The API documentation is also always available in the API:

.. code-block:: python

   help(any_api_object)

Some examples:

For classes (and their members):

.. code-block:: python

   from byteblower_test_framework.host import Server
   from byteblower_test_framework.endpoint import IPv4Port
   from byteblower_test_framework.traffic import FrameBlastingFlow
   help(Server)
   help(Server.start)
   help(Server.info)
   help(IPv4Port)
   help(FrameBlastingFlow)
   from byteblower_test_framework.report import ByteBlowerHtmlReport
   help(ByteBlowerHtmlReport)

For objects (and their members):

.. code-block:: python

   from byteblower_test_framework.host import Server
   my_server = Server('byteblower-39.lab.excentis.com.')
   help(my_server)
   help(my_server.start)

Usage
=====

First make sure that your *activated* your virtual environment:

.. code-block:: shell

   . ./env/bin/activate

Let's give it a test run: Import the test framework and show its
documentation:

.. code-block:: shell

   python

.. code-block:: python

   import byteblower_test_framework
   help(byteblower_test_framework)

This shows you the ByteBlower Test Framework module documentation.

.. TODO: Provide a quick start guide
.. note::
   **To-do**: *We will provide a quick start guide in the future.*

Development
===========

Would you like to contribute to this project? You're very welcome! 😊

Please contact us at `ByteBlower Support`_ and we'll be there to guide you.

Support
=======

.. See http://docutils.sourceforge.net/0.4/docs/ref/rst/directives.html#image

If you have any questions or feature request you can contact the ByteBlower
support team using:

|globe|: `Excentis Support Portal`_

|e-mail|: `ByteBlower Support`_

|telephone|: +32 (0) 9 269 22 91

.. e-mail icon:
.. |e-mail| unicode:: U+1F582

.. globe icon:
.. |globe| unicode:: U+1F30D
.. .. |globe| unicode:: U+1F310

.. telephone icon:
.. |telephone| unicode:: U+1F57D

.. ByteBlower logo
.. image:: http://static.excentis.com/byteblower_blue_transparent_background.png
   :width: 400
   :scale: 60
   :align: right
   :alt: ByteBlower
   :target: byteblower_

.. "A product by Excentis" logo
.. image:: http://static.excentis.com/Aproductby.png
   :width: 320
   :scale: 60
   :align: right
   :alt: A product by Excentis
   :target: excentis_

.. _byteblower: https://byteblower.com
.. _excentis: https://www.excentis.com
.. _Excentis Support Portal: https://support.excentis.com
.. _ByteBlower Support: mailto:support.byteblower@excentis.com
