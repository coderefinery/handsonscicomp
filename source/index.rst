.. Hands-on Scientific Computing documentation master file, created by
   sphinx-quickstart on Thu Jul 11 14:04:10 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Hands-on Scientific Computing
=============================

Hands-on SciCompm is an self-study course and reference material for
the *practical* side of scientific computing - what you need to know
but don't learn in courses.  It is focused on what is needed as you
transition from academic studies to hands-on computational research.

There are already plenty of places you can find material: `Software
Carpentry`_, CodeRefinery_, and more have basically unlimited
information --- but what do you actually need?  How do you find it?
Hands-on SciComp is written by those supporting researchers and is
designed to help you know how deep you need to go, direct you to the
right material, and get some credit for it.

.. _Software Carpentry: https://software-carpentry.org
.. _CodeRefinery: https://coderefinery.org


Our material is divided into different levels.  First, check how
demanding your work is so that you can choose the right courses to
focus on.

.. list-table::
   :header-rows: 1

   * * Level
     * For who?
     * Covers what?

   * * **A:** Basic background
     * Everyone who's doing science with your computer or may need to
       ask for help with their research.
     * How to set up your computer to do scientific work and how to
       ask for help.  What you may need to know next.

   * * **B:** Scientific computing
     * Everyone who's doing more than pointing and clicking single
       applications on your own computer or needs more computing power.
     * In this level, you learn how to extend your power beyond your
       own computer or existing applications.
       Includes data management, scripting, Linux, and servers.  Linux
       and the shell are a major point here: this is the defacto (and
       only) good way to increase power.


   * * **C:** Scientific programming
     * When you start writing your own software to do your research.
     * Version control, how to manage code, software, and data even
       more.

   * * **D:** High-performance computing
     * Those who need more power than their own computer and need to
       move to a cluster, whether or not it's highly parallelized.
     * Advanced Linux, more scripting, batch systems, HPC data
       management.

   * * **E:** Advanced high performance computing
     * Those who are programming the most demanding parallel
       scientific applications.
     * MPI (message passing interface, a parallel programming
       framework), OpenMP (another one), GPU programming, etc.

We have material for different learning styles:

.. list-table::
   :header-rows: 1

   * * Video intro
     * Material
     * Local info
     * Exercises

   * * A short video introduction and demo to get you started
     * Reference material to read, which covers anything you may need.
     * If your university has specific local information to supplement
       the general info, it can be found here.
     * Practice exercises.  In the future, doing these will allow you
       to get study credits.


A: Basics
=========

B: Scientific computing
=======================

.. yaml-table::
   :header-rows: 1
   :file: ../courses/B.yaml


**Other courses:**

.. list-table::
   :header-rows: 1

   * *

     *

     * Video

     * Reading

   * * B30

       Makefiles
     * Makefiles are like smart shell scripts.  We learn some about
       them and in the process, become ever more efficient.

     *

     * `Software
       Carpentry make-novice
       <http://swcarpentry.github.io/make-novice/>`__.

   * * B50

       Version control for teams
     * Previously, you learned only the basics.  Now for the real
       stuff.

     *

     * `CodeRefinery collaborative distributed version control
       lesson <http://coderefinery.org/lessons/>`__

   * * B51

       Jupyter Notebooks
     * Notebooks are an efficient way to make self-documenting code
       and scripts and do data science well.

     *

     * `CodeRefinery Jupyter
       course <http://coderefinery.org/lessons/>`__.


C: Scientific programming
=========================

D: High performance computing
=============================

E: Advanced high performance computing
======================================



.. toctree::
   :maxdepth: 2



* :ref:`genindex`
