.. _Run_Tests:

Running Tests
*************

|codecov-devel|

The package can be tested by running the `test scripts <https://github.com/ameli/detkit/tree/main/tests>`_, which tests all `modules <https://github.com/ameli/detkit/tree/main/detkit>`_. 

Running Tests with `pytest`
===========================

The package can be tested by running several `test scripts <https://github.com/ameli/detkit/tree/main/tests>`_, which test all `sub-packages <https://github.com/ameli/detkit/tree/main/detkit>`_.

1. Clone the source code from the repository and install the required test packages by
  
   .. prompt:: bash
  
      git clone https://github.com/ameli/detkit.git
      cd detkit
      python -m pip install -r tests/requirements.txt
      python setup.py install

2. To automatically run all tests, use ``pytest`` which is installed by the above commands.
  
   .. prompt:: bash
   
       mv detkit detkit-do-not-import
       pytest

   .. attention::
  
      To properly run ``pytest``, rename ``/detkit/detkit`` directory as shown in the above code. This makes ``pytest`` to properly import |project| from the installed location, not from the source code directory.

Running Tests with `tox`
========================

To run a test in a virtual environment, use ``tox`` as follows:

1. Install `tox`:
   
   .. prompt:: bash
       
       python -m pip install tox

2. Clone the source code from the repository:
   
   .. prompt:: bash
       
       git clone https://github.com/ameli/detkit.git

3. run tests by
   
   .. prompt:: bash

       cd detkit
       tox
  
.. |codecov-devel| image:: https://img.shields.io/codecov/c/github/ameli/detkit
   :target: https://codecov.io/gh/ameli/detkit
.. |build-linux| image:: https://github.com/ameli/detkit/workflows/build-linux/badge.svg
   :target: https://github.com/ameli/detkit/actions?query=workflow%3Abuild-linux 
.. |build-macos| image:: https://github.com/ameli/detkit/workflows/build-macos/badge.svg
   :target: https://github.com/ameli/detkit/actions?query=workflow%3Abuild-macos
.. |build-windows| image:: https://github.com/ameli/detkit/workflows/build-windows/badge.svg
   :target: https://github.com/ameli/detkit/actions?query=workflow%3Abuild-windows
