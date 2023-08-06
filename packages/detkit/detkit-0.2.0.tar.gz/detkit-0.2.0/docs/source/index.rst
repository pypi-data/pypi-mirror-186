detkit
******

|license| |deploy-docs|

A python package to compute some common functions involving determinant of matrices used in machine learning.

.. grid:: 4

    .. grid-item-card:: GitHub
        :link: https://github.com/ameli/detkit
        :text-align: center
        :class-card: custom-card-link

    .. grid-item-card:: PyPI
        :link: https://pypi.org/project/detkit/
        :text-align: center
        :class-card: custom-card-link

    .. grid-item-card:: Anaconda Cloud
        :link: https://anaconda.org/s-ameli/detkit
        :text-align: center
        :class-card: custom-card-link

    .. grid-item-card:: Docker Hub
        :link: https://hub.docker.com/r/sameli/detkit
        :text-align: center
        :class-card: custom-card-link

List of Functions
=================

.. autosummary::
    :recursive:
    :nosignatures:
    :template: autosummary/member.rst

    detkit.logdet
    detkit.loggdet
    detkit.logpdet

See :ref:`api` for a list of all functions.

Install
=======

|conda-downloads|

.. grid:: 2

    .. grid-item-card:: 

        Install with ``pip`` from `PyPI <https://pypi.org/project/detkit/>`_:

        .. prompt:: bash
            
            pip install detkit

    .. grid-item-card::

        Install with ``conda`` from `Anaconda Cloud <https://anaconda.org/s-ameli/detkit>`_:

        .. prompt:: bash
            
            conda install -c s-ameli detkit

For complete installation guide, see:

.. toctree::
    :maxdepth: 2
    :numbered:

    Install <install>
    Test <tests>

Docker
======

|docker-pull| |deploy-docker|

The docker image comes with a pre-installed |project|, an NVIDIA graphic driver, and a compatible version of CUDA Toolkit libraries.

.. grid:: 1

    .. grid-item-card::

        Pull docker image from `Docker Hub <https://hub.docker.com/r/sameli/detkit>`_:

        .. prompt:: bash
            
            docker pull sameli/detkit

For a complete guide, see:

.. toctree::
    :maxdepth: 2
    :numbered:

    Docker <docker>

Tutorials
=========

|binder|

Launch an online interactive tutorial in `Jupyter notebook <https://mybinder.org/v2/gh/ameli/detkit/HEAD?filepath=notebooks%2FSpecial%20Functions.ipynb>`_.

.. toctree::
    :maxdepth: 1
    :hidden:

    API Reference <api>

Benchmarks
==========

See :ref:`benchmark test <benchmark>` for evaluating the numerical performance of the functions in real applications.

Features
========

|tokei-2| |languages|

* Functions are implemented with a novel algorithm described in [1]_.
* The underlying library is implemented in C++ and wrapped in cython.
* An accurate count of computational FLOPs during the execution of functions can be measured.

How to Contribute
=================

We welcome contributions via `Github's pull request <https://github.com/ameli/detkit/pulls>`_. If you do not feel comfortable modifying the code, we also welcome feature request and bug report as `Github issues <https://github.com/ameli/detkit/issues>`_.

Related Projects
================

|project| is used in the following python packages:

.. grid:: 2

   .. grid-item-card:: |glearn-light| |glearn-dark|
       :link: https://ameli.github.io/glearn/index.html
       :text-align: center
       :class-card: custom-card-link
   
       A high-performance python package for machine learning using Gaussian process regression.

   .. grid-item-card:: |imate-light| |imate-dark|
       :link: https://ameli.github.io/imate/index.html
       :text-align: center
       :class-card: custom-card-link
   
       A high-performance python package for scalable randomized algorithms for matrix functions in machine learning.

.. How to Cite
.. include:: cite.rst

.. |deploy-docs| image:: https://img.shields.io/github/actions/workflow/status/ameli/detkit/deploy-docs.yml?label=docs
   :target: https://github.com/ameli/detkit/actions?query=workflow%3Adeploy-docs
.. |deploy-docker| image:: https://img.shields.io/github/actions/workflow/status/ameli/detkit/deploy-docker.yml?label=build%20docker
   :target: https://github.com/ameli/detkit/actions?query=workflow%3Adeploy-docker
.. |codecov-devel| image:: https://img.shields.io/codecov/c/github/ameli/detkit
   :target: https://codecov.io/gh/ameli/detkit
.. |license| image:: https://img.shields.io/github/license/ameli/detkit
   :target: https://opensource.org/licenses/BSD-3-Clause
.. |implementation| image:: https://img.shields.io/pypi/implementation/detkit
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/detkit
.. |format| image:: https://img.shields.io/pypi/format/detkit
.. |conda| image:: https://anaconda.org/s-ameli/traceinv/badges/installer/conda.svg
   :target: https://anaconda.org/s-ameli/traceinv
.. |platforms| image:: https://img.shields.io/conda/pn/s-ameli/traceinv?color=orange?label=platforms
   :target: https://anaconda.org/s-ameli/traceinv
.. |conda-version| image:: https://img.shields.io/conda/v/s-ameli/traceinv
   :target: https://anaconda.org/s-ameli/traceinv
.. |binder| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/ameli/detkit/HEAD?filepath=notebooks%2FInterpolateTraceOfInverse.ipynb
.. |conda-downloads| image:: https://img.shields.io/conda/dn/s-ameli/detkit
   :target: https://anaconda.org/s-ameli/detkit
.. |tokei| image:: https://tokei.rs/b1/github/ameli/detkit?category=lines
   :target: https://github.com/ameli/detkit
.. |tokei-2| image:: https://img.shields.io/badge/code%20lines-12.9k-blue
   :target: https://github.com/ameli/detkit
.. |languages| image:: https://img.shields.io/github/languages/count/ameli/detkit
   :target: https://github.com/ameli/detkit
.. |docker-pull| image:: https://img.shields.io/docker/pulls/sameli/detkit?color=green&label=downloads
   :target: https://hub.docker.com/r/sameli/detkit
.. |glearn-light| image:: _static/images/icons/logo-glearn-light.svg
   :height: 30
   :class: only-light
.. |glearn-dark| image:: _static/images/icons/logo-glearn-dark.svg
   :height: 30
   :class: only-dark
.. |imate-light| image:: _static/images/icons/logo-imate-light.svg
   :height: 23
   :class: only-light
.. |imate-dark| image:: _static/images/icons/logo-imate-dark.svg
   :height: 23
   :class: only-dark
.. |detkit-light| image:: _static/images/icons/logo-detkit-light.svg
   :height: 27
   :class: only-light
.. |detkit-dark| image:: _static/images/icons/logo-detkit-dark.svg
   :height: 27
   :class: only-dark
