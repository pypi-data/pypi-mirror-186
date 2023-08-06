.. _install_package:

Install
*******

.. contents::

Supported Platforms
===================

Successful installation and tests have been performed on the following platforms and Python/PyPy versions shown in the table below.


.. |y| unicode:: U+2714
.. |n| unicode:: U+2716

+----------+--------+-------+-------+-------+-------+-------+-------+-------+-----------------+
| Platform | Arch   | Python Version                        | PyPy Version  | Continuous      |
+          |        +-------+-------+-------+-------+-------+-------+-------+ Integration     +
|          |        |  3.6  |  3.7  |  3.8  |  3.9  |  3.10 |  3.6  |  3.7  |                 |
+==========+========+=======+=======+=======+=======+=======+=======+=======+=================+
| Linux    | X86-64 |  |y|  |  |y|  |  |y|  |  |y|  |  |y|  |  |y|  |  |y|  | |build-linux|   |
+----------+--------+-------+-------+-------+-------+-------+-------+-------+-----------------+
| macOS    | X86-64 |  |y|  |  |y|  |  |y|  |  |y|  |  |y|  |  |n|  |  |n|  | |build-macos|   |
+----------+--------+-------+-------+-------+-------+-------+-------+-------+-----------------+
| Windows  | X86-64 |  |y|  |  |y|  |  |y|  |  |y|  |  |y|  |  |n|  |  |n|  | |build-windows| |
+----------+--------+-------+-------+-------+-------+-------+-------+-------+-----------------+

.. |build-linux| image:: https://github.com/ameli/detkit/workflows/build-linux/badge.svg
   :target: https://github.com/ameli/detkit/actions?query=workflow%3Abuild-linux 
.. |build-macos| image:: https://github.com/ameli/detkit/workflows/build-macos/badge.svg
   :target: https://github.com/ameli/detkit/actions?query=workflow%3Abuild-macos
.. |build-windows| image:: https://github.com/ameli/detkit/workflows/build-windows/badge.svg
   :target: https://github.com/ameli/detkit/actions?query=workflow%3Abuild-windows

Python wheels for |project| for all supported platforms and versions in the above are available through `PyPI <https://pypi.org/project/detkit/>`__ and `Anaconda Cloud <https://anaconda.org/s-ameli/detkit>`_. If you need |project| on other platforms, architectures, and Python or PyPy versions, `raise an issue <https://github.com/ameli/detkit/issues>`_ on GitHub and we build its Python Wheel for you.

.. _install-wheels:

Install |project| From Wheels
=============================

Python wheels for |project| are available for various operating systems and Python versions on both PyPI and Anaconda Cloud.

Install with ``pip``
--------------------

|pypi|

Install |project| and its Python dependencies through `PyPI <https://pypi.org/project/detkit>`__ by

.. prompt:: bash
    
    python -m pip install --upgrade pip
    python -m pip install detkit

If you are using PyPy instead of Python, install with

.. prompt:: bash
    
    pypy -m pip install --upgrade pip
    pypy -m pip install detkit

Install with ``conda``
----------------------

|conda-version|

Alternately, install |project| and its Python dependencies from `Anaconda Cloud <https://anaconda.org/s-ameli/detkit>`_ by

.. prompt:: bash

    conda install -c s-ameli detkit -y

.. _virtual-env:

Dependencies
============

|project| can count the FLOPs of the computations, if the argument ``flops=True`` is used in the functions (see :ref:`API Reference <api>`). To this end, the `Linux Performance Counter tool <https://perf.wiki.kernel.org/index.php/Main_Page>`_, known as ``perf`` should be installed.

.. tab-set::

    .. tab-item:: Ubuntu/Debian
        :sync: ubuntu

        .. prompt:: bash

            sudo apt install linux-tools

    .. tab-item:: CentOS 7
        :sync: centos

        .. prompt:: bash

            sudo yum group install perf

    .. tab-item:: RHEL 9
        :sync: rhel

        .. prompt:: bash

            sudo dnf group install perf

.. attention::

    The ``perf`` tool is not available in macOS and Windows.

Install |project| in Virtual Environments
=========================================

If you do not want the installation to occupy your main python's site-packages (either you are testing or the dependencies may clutter your existing installed packages), install the package in an isolated virtual environment. Two common virtual environments are :ref:`virtualenv <virtualenv_env>` and :ref:`conda <conda_env>`.

.. _virtualenv_env:

Install in ``virtualenv`` Environment
-------------------------------------

1. Install ``virtualenv``:

   .. prompt:: bash

       python -m pip install virtualenv

2. Create a virtual environment and give it a name, such as ``imate_env``

   .. prompt:: bash

       python -m virtualenv imate_env

3. Activate python in the new environment

   .. prompt:: bash

       source imate_env/bin/activate

4. Install ``imate`` package with any of the :ref:`above methods <install-wheels>`. For instance:

   .. prompt:: bash

       python -m pip install imate
   
   Then, use the package in this environment.

5. To exit from the environment

   .. prompt:: bash

       deactivate

.. _conda_env:

Install in ``conda`` Environment
--------------------------------

In the followings, it is assumed `anaconda <https://www.anaconda.com/products/individual#Downloads>`_ (or `miniconda <https://docs.conda.io/en/latest/miniconda.html>`_) is installed.

1. Initialize conda

   .. prompt:: bash

       conda init

   You may need to close and reopen your terminal after the above command. Alternatively, instead of the above, you can do

   .. prompt:: bash

       sudo sh $(conda info --root)/etc/profile.d/conda.sh

2. Create a virtual environment and give it a name, such as ``imate_env``

   .. prompt:: bash

       conda create --name imate_env -y

   The command ``conda info --envs`` shows the list of all environments. The current environment is marked by an asterisk in the list, which should be the default environment at this stage. In the next step, we will change the current environment to the one we created.

3. Activate the new environment

   .. prompt:: bash

       source activate imate_env

4. Install ``imate`` with any of the :ref:`above methods <install-wheels>`. For instance:

   .. prompt:: bash

       conda install -c s-ameli imate
   
   Then, use the package in this environment.

5. To exit from the environment

   .. prompt:: bash

       conda deactivate
       
Compile from Source
===================

When to Compile |project|
-------------------------

Generally, it is not required to compile |project| as the installation through ``pip`` and ``conda``. You may compile |project| if you want to:

* modify |project|.
* enable `debugging mode`.
* or, build this `documentation`.

Otherwise, install |project| through the :ref:`Python Wheels <install-wheels>`.

This section walks you through the compilation process.

Install C++ Compiler and OpenMP (`Required`)
--------------------------------------------

Compile |project| with either of GCC, Clang/LLVM, or Intel C++ compiler on UNIX operating systems. For Windows, compile |project| with `Microsoft Visual Studio (MSVC) Compiler for C++ <https://code.visualstudio.com/docs/cpp/config-msvc#:~:text=You%20can%20install%20the%20C,the%20C%2B%2B%20workload%20is%20checked.>`_.

.. rubric:: Install GNU GCC Compiler

.. tab-set::

    .. tab-item:: Ubuntu/Debian
        :sync: ubuntu

        .. prompt:: bash

            sudo apt install build-essential

    .. tab-item:: CentOS 7
        :sync: centos

        .. prompt:: bash

            sudo yum group install "Development Tools"

    .. tab-item:: RHEL 9
        :sync: rhel

        .. prompt:: bash

            sudo dnf group install "Development Tools"

    .. tab-item:: macOS
        :sync: osx

        .. prompt:: bash

            sudo brew install gcc libomp

Then, export ``C`` and ``CXX`` variables by

.. prompt:: bash

  export CC=/usr/local/bin/gcc
  export CXX=/usr/local/bin/g++

.. rubric:: Install Clang/LLVN Compiler
  
.. tab-set::

    .. tab-item:: Ubuntu/Debian
        :sync: ubuntu

        .. prompt:: bash

            sudo apt install clang

    .. tab-item:: CentOS 7
        :sync: centos

        .. prompt:: bash

            sudo yum install yum-utils
            sudo yum-config-manager --enable extras
            sudo yum makecache
            sudo yum install clang

    .. tab-item:: RHEL 9
        :sync: rhel

        .. prompt:: bash

            sudo dnf install yum-utils
            sudo dnf config-manager --enable extras
            sudo dnf makecache
            sudo dnf install clang

    .. tab-item:: macOS
        :sync: osx

        .. prompt:: bash

            sudo brew install llvm libomp-dev

Then, export ``C`` and ``CXX`` variables by

.. prompt:: bash

  export CC=/usr/local/bin/clang
  export CXX=/usr/local/bin/clang++

.. rubric:: Install Intel oneAPI Compiler

To install `Intel Compiler` see `Intel oneAPI Base Toolkit <https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html?operatingsystem=linux&distributions=aptpackagemanager>`_.

Install OpenMP (`Required`)
---------------------------

OpenMP comes with the C++ compiler installed. However, you may alternatively install it directly on UNIX. Install `OpenMP` library on UNIX as follows:

.. tab-set::

    .. tab-item:: Ubuntu/Debian
        :sync: ubuntu

        .. prompt:: bash

            sudo apt install libgomp1 -y

    .. tab-item:: CentOS 7
        :sync: centos

        .. prompt:: bash

            sudo yum install libgomp -y

    .. tab-item:: RHEL 9
        :sync: rhel

        .. prompt:: bash

            sudo dnf install libgomp -y

    .. tab-item:: macOS
        :sync: osx

        .. prompt:: bash

            sudo brew install libomp

.. _config-env-variables:

Configure Compile-Time Environment Variables (`Optional`)
---------------------------------------------------------

Set the following environment variables as desired to configure the compilation process.

.. glossary::

    ``CYTHON_BUILD_IN_SOURCE``

        By default, this variable is set to `0`, in which the compilation process generates source files outside of the source directory, in ``/build`` directry. When it is set to `1`, the build files are generated in the source directory. To set this variable, run

        .. tab-set::

            .. tab-item:: UNIX
                :sync: unix

                .. prompt:: bash

                    export CYTHON_BUILD_IN_SOURCE=1

            .. tab-item:: Windows (Powershell)
                :sync: win

                .. prompt:: powershell

                    $env:export CYTHON_BUILD_IN_SOURCE = "1"

        .. hint::

            If you generated the source files inside the source directory by setting this variable, and later you wanted to clean them, see :ref:`Clean Compilation Files <clean-files>`.

    ``CYTHON_BUILD_FOR_DOC``

        Set this variable if you are building this documentation. By default, this variable is set to `0`. When it is set to `1`, the package will be built suitable for generating the documentation. To set this variable, run

        .. tab-set::

            .. tab-item:: UNIX
                :sync: unix

                .. prompt:: bash

                    export CYTHON_BUILD_FOR_DOC=1

            .. tab-item:: Windows (Powershell)
                :sync: win

                .. prompt:: powershell

                    $env:export CYTHON_BUILD_FOR_DOC = "1"

        .. warning::

            Do not use this option to build the package for `production` (release) as it has a slower performance. Building the package by enabling this variable is only suitable for generating the documentation.

        .. hint::

            By enabling this variable, the build will be `in-source`, similar to setting ``CYTHON_BUILD_IN_SOURCE=1``. To clean the source directory from the generated files, see :ref:`Clean Compilation Files <clean-files>`.

    ``DEBUG_MODE``

        By default, this variable is set to `0`, meaning that |project| is compiled without debugging mode enabled. By enabling debug mode, you can debug the code with tools such as ``gdb``. Set this variable to `1` to enable debugging mode by

        .. tab-set::

            .. tab-item:: UNIX
                :sync: unix

                .. prompt:: bash

                    export DEBUG_MODE=1

            .. tab-item:: Windows (Powershell)
                :sync: win

                .. prompt:: powershell

                    $env:export DEBUG_MODE = "1"

        .. attention::

            With the debugging mode enabled, the size of the package will be larger and its performance may be slower, which is not suitable for `production`.

Compile and Install
-------------------

|repo-size|

Get the source code of |project| from the GitHub repository by

.. prompt:: bash

    git clone https://github.com/ameli/detkit.git
    cd detkit

To compile and install, run

.. prompt:: bash

    python setup.py install

The above command may need ``sudo`` privilege. 

.. rubric:: A Note on Using ``sudo``

If you are using ``sudo`` for the above command, add ``-E`` option to ``sudo`` to make sure the environment variables (if you have set any) are accessible to the root user. For instance

.. tab-set::

    .. tab-item:: UNIX
        :sync: unix

        .. code-block:: Bash

            export CYTHON_BUILD_FOR_DOC=1
            sudo -E python setup.py install

    .. tab-item:: Windows (Powershell)
        :sync: win

        .. code-block:: PowerShell

            $env:export CYTHON_BUILD_FOR_DOC = "1"
            sudo -E python setup.py install

Once the installation is completed, check the package can be loaded by

.. prompt:: bash

    cd ..  # do not load detkit in the same directory of the source code
    python -c "import detkit"

.. attention::

    Do not load |project| if your current working directory is the root directory of the source code of |project|, since python cannot load the installed package properly. Always change the current directory to somewhere else (for example, ``cd ..`` as shown in the above).

.. _clean-files:
   
.. rubric:: Cleaning Compilation Files

If you set ``CYTHON_BUILD_IN_SOURCE`` or ``CYTHON_BUILD_FOR_DOC`` to ``1``, the output files of Cython's compiler will be generated inside the source code directories. To clean the source code from these files (`optional`), run the following:

.. prompt:: bash

    python setup.py clean

Generate Documentation
======================

Before generating the Sphinx documentation, you should compile the package. First, get the source code from the GitHub repository.

.. prompt:: bash

    git clone https://github.com/ameli/detkit.git
    cd detkit

If you already had the source code, clean it from any previous build (especially if you built `in-source`):

.. prompt:: bash

    python setup.py clean

Compile Package
---------------

Set ``CYTHON_BUILD_FOR_DOC`` to `1` (see :ref:`Configure Compile-Time Environment variables <config-env-variables>`). Compile and install the package by

.. tab-set::

    .. tab-item:: UNIX
        :sync: unix

        .. prompt:: bash

            export CYTHON_BUILD_FOR_DOC=1
            sudo -E python setup.py install

    .. tab-item:: Windows (Powershell)
        :sync: win

        .. prompt:: powershell

            $env:export CYTHON_BUILD_FOR_DOC = "1"
            sudo -E python setup.py install

Generate Sphinx Documentation
-----------------------------

Install `Pandoc <https://pandoc.org/>`_ by

.. tab-set::

   .. tab-item:: Ubuntu/Debian
      :sync: ubuntu

      .. prompt:: bash

            sudo apt install pandoc -y

   .. tab-item:: CentOS 7
      :sync: centos

      .. prompt:: bash

          sudo yum install pandoc -y

   .. tab-item:: RHEL 9
      :sync: rhel

      .. prompt:: bash

          sudo dnf install pandoc -y

   .. tab-item:: macOS
      :sync: osx

      .. prompt:: bash

          sudo brew install pandoc -y

   .. tab-item:: Windows (Powershell)
      :sync: win

      .. prompt:: powershell

          scoop install pandoc

Install the requirements for the Sphinx documentation by

.. prompt:: bash

    python -m pip install -r docs/requirements.txt

The above command installs the required packages in Python's path directory. Make sure python's directory is on the `PATH`, for instance, by

.. tab-set::

    .. tab-item:: UNIX
        :sync: unix

        .. prompt:: bash

            PYTHON_PATH=`python -c "import os, sys; print(os.path.dirname(sys.executable))"`
            export PATH=${PYTHON_PATH}:$PATH

    .. tab-item:: Windows (Powershell)
        :sync: win

        .. prompt:: powershell

            $PYTHON_PATH = (python -c "import os, sys; print(os.path.dirname(sys.executable))")
            $env:Path += ";$PYTHON_PATH"

Now, build the documentation:

.. tab-set::

    .. tab-item:: UNIX
        :sync: unix

        .. prompt:: bash

            make clean html --directory=docs

    .. tab-item:: Windows (Powershell)
        :sync: win

        .. prompt:: powershell

            cd docs
            make.bat clean html

The main page of the documentation can be found in ``/docs/build/html/index.html``. 

.. |implementation| image:: https://img.shields.io/pypi/implementation/detkit
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/detkit
.. |format| image:: https://img.shields.io/pypi/format/detkit
.. |pypi| image:: https://img.shields.io/pypi/v/detkit
   :target: https://pypi.org/project/detkit
.. |conda| image:: https://anaconda.org/s-ameli/detkit/badges/installer/conda.svg
   :target: https://anaconda.org/s-ameli/detkit
.. |platforms| image:: https://img.shields.io/conda/pn/s-ameli/detkit?color=orange?label=platforms
   :target: https://anaconda.org/s-ameli/detkit
.. |conda-version| image:: https://img.shields.io/conda/v/s-ameli/detkit
   :target: https://anaconda.org/s-ameli/detkit
.. |release| image:: https://img.shields.io/github/v/tag/ameli/detkit
   :target: https://github.com/ameli/detkit/releases/
.. |conda-platform| image:: https://anaconda.org/s-ameli/detkit/badges/platforms.svg
   :target: https://anaconda.org/s-ameli/detkit
.. |repo-size| image:: https://img.shields.io/github/repo-size/ameli/detkit
   :target: https://github.com/ameli/detkit
