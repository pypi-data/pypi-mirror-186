.. _benchmark:

Benchmark Tests
===============

A numerical analysis of the performance of the functions are described in Section 4 of [1]_, which serves as a benchmark test to this package. Here, we provide supplemental details on how to reproduce the numerical results of the paper.


Install Package
---------------

First, install |project| by

.. prompt:: bash

    pip install detkit

Datasets
--------

The following numerical results are insensitive to the matrices used during the benchmark tests. However, here we use matrices that are obtained from real applications. The followings describe how to reproduce the datasets described in Appendix C of [1]_.

Figure 


.. image:: _static/images/plots/electrocardiogram.png
    :align: center
    :class: custom-dark


.. image:: _static/images/plots/covariance.png
    :align: center
    :class: custom-dark

Perform Numerical Tests
-----------------------

The followings show how to reproduce the results of Section 4 of [1]_. First, download the source code of |project| by

.. prompt:: bash

    git clone https://github.com/ameli/detkit.git

The scripts for the benchmark tests are located at |benchmark_folder|_ directory of the source code.

1. Run Locally
~~~~~~~~~~~~~~

* Run |benchmark_py|_ to reproduce results for Toeplitz matrices as follows
  
     .. prompt:: bash
    
         cd /detkit/benchmark/scripts
         python ./benchmark.py
  


2. Run on Cluster with Torque
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Submit |jobfile_benchmark|_ to reproduce results of log-determinant of simple matrices:
  
     .. prompt:: bash
    
         cd /imate/benchmark/jobfiles
         qsub jobfile_benchmark.pbs


Plot Results
------------

Run |notebook_benchmark|_ to generate plots for computing the log-determinants of Toeplitz matrices. The notebook stores the plots as `svg` files in |svg_plots|_ directory.

.. |benchmark_folder| replace:: ``/detkit/benchmark``
.. _benchmark_folder: https://github.com/ameli/detkit/tree/main/benchmark

.. |benchmark_py| replace:: ``/detkit/benchmark/scripts/benchmark.py``
.. _benchmark_py: https://github.com/ameli/detkit/blob/main/benchmark/scripts/benchmark.py

.. |jobfile_benchmark| replace:: ``/detkit/benchmark/jobfiles/jobfile_benchmark.pbs``
.. _jobfile_benchmark: https://github.com/ameli/detkit/blob/main/benchmark/jobfiles/jobfile_benchmark.pbs

.. |notebook_benchmark| replace:: ``/detkit/benchmark/notebooks/benchmark_plot_draft_3.ipynb``
.. _notebook_benchmark: https://github.com/ameli/detkit/blob/main/benchmark/notebooks/benchmark_plot_draft_3.ipynb

.. |svg_plots| replace:: ``/imate/benchmark/plots/``
.. _svg_plots: https://github.com/ameli/imate/blob/main/benchmark/plots

References
----------
   
.. [1] Ameli, S., and Shadden. S. C. (2022). *A Singular Woodbury and Pseudo-Determinant Matrix Identities and Application to Gaussian Process Regression* |ameli-woodbury| |btn-bib-1| |btn-view-pdf-1|
   
   .. raw:: html

        <div class="highlight-BibTeX notranslate collapse" id="collapse-bib1">
        <div class="highlight">
        <pre class="language-bib">
        <code class="language-bib">@misc{arxiv.2207.08038,
            doi = {10.48550/arXiv.2207.08038},
            author = {Ameli, S. and Shadden, S. C.}, 
            title = {A Singular Woodbury and Pseudo-Determinant Matrix Identities and Application to Gaussian Process Regression},
            year = {2022}, 
            archivePrefix={arXiv},
            eprint = {2207.08038},
            primaryClass={math.NA},
            howpublished={\emph{arXiv}: 2207.08038 [math.ST]},
        }</code></pre>
        </div>
        </div>

.. [2] Moody GB, Mark RG. The impact of the MIT-BIH Arrhythmia Database.
       IEEE Eng in Med and Biol 20(3):45-50 (May-June 2001).
       (PMID: 11446209); DOI: `10.13026/C2F305
       <https://doi.org/10.13026/C2F305>`__

.. [3] Goldberger AL, Amaral LAN, Glass L, Hausdorff JM, Ivanov PCh, Mark
       RG, Mietus JE, Moody GB, Peng C-K, Stanley HE. PhysioBank,
       PhysioToolkit, and PhysioNet: Components of a New Research Resource
       for Complex Physiologic Signals. Circulation 101(23):e215-e220;
       DOI: `10.1161/01.CIR.101.23.e215
       <https://doi.org/10.1161/01.CIR.101.23.e215>`__

.. |btn-bib-1| raw:: html

    <button class="btn btn-outline-info btn-sm btn-extra-sm" type="button" data-toggle="collapse" data-target="#collapse-bib1">
        BibTeX
    </button>
    
.. |btn-view-pdf-1| raw:: html

    <button class="btn btn-outline-info btn-sm btn-extra-sm" type="button" id="showPDF01">
        PDF
    </button>
    
.. |ameli-woodbury| image:: https://img.shields.io/badge/arXiv-2207.08038-b31b1b.svg
   :target: https://doi.org/10.48550/arXiv.2207.08038
   :alt: arXiv 2207.08038
