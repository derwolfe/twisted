
:LastChangedDate: $LastChangedDate$
:LastChangedRevision: $LastChangedRevision$
:LastChangedBy: $LastChangedBy$

Getting started with Twisted development
========================================




Working on Twisted requires the installation of several development dependencies. These are specified in the dev-requirements.txt file located in Twisted's top level directory. To develop Twisted in an isolated environment, it is recommened to use a virtual environment. If you are not familiar with this, please see `virtualenv`_. 

All of the dependencies required to build documentation, run tests, and check for compliance with the :doc:`policy/coding-standard` can be installed into your virtual environment using `pip`_.

.. code-block:: console

		$ # Create a virtualenv and activate it
		$ pip install --requirement dev-requirements.txt


.. _`virtualenv`: https://pypi.python.org/pypi/virtualenv
.. _`pip`: https://pypi.python.org/pypi/pip

