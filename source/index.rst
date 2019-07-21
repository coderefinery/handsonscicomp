
Hands-on Scientific Computing
=============================

Hands-on SciComp is an self-study course and reference material for
the *practical* side of scientific computing - what you need to know
but don't learn in your studies.  It is focused on what is needed as you
transition from academic studies to real-life computational research.

What you find here isn't unique, and you can find similar materials
from `Software Carpentry`_, CodeRefinery_, and more --- but these all
are roughly designed as single, guided courses.  Hands-on SciComp
links to all of these materials and organizes them for self-study and
determining where you need to start?  Hands-on SciComp is written by
those supporting researchers and is designed to help you know how deep
you need to go, direct you to the right material, and get some credit
for it.

.. _Software Carpentry: https://software-carpentry.org
.. _CodeRefinery: https://coderefinery.org

Our material is divided into different levels.  First, check how
demanding your work is so that you can choose the right courses to
focus on.

.. image:: levels.svg
   :align: center
   :alt: Level dependencies
   :scale: 75%


.. list-table::
   :header-rows: 1

   * * Level
     * For who?
     * Covers what?

   * * **A:** Basics: What computing and how?
     * Mini-level for everyone who's doing science with your computer
       or may need to rely on computing resources later.
     * What types of resources are available, when you'd use them, and
       how to get help.  How to set up your computer to do scientific
       work.  What comes next.

   * * **B:** Related science skills
     * Everyone publishing in a somewhat computational field.
     * Making figures, papers, posters, and so on they way it's done
       in computational fields.

   * * **C:** Scientific computing (Linux and shell)
     * Everyone who's doing more than pointing and clicking single
       applications on your own computer or needs more computing power.
     * In this level, you learn how to extend your power beyond your
       own computer or existing applications.
       Includes data management, scripting, Linux, and servers.  Linux
       and the shell are a major point here: this is the defacto (and
       only) good way to increase power.  Equal to the B level.

   * * **D:** Clusters and high-performance computing
     * Those who need more power than their own computer and need to
       move to a cluster, whether or not it's highly parallelized.
     * Computing on clusters and remote servers, more advanced Linux,
       more scripting, batch systems, HPC data management.

   * * **E:** Scientific coding
     * When you start writing your own software to do your research.
     * Version control, how to manage code, software, and data even
       more.  We don't cover programming itself, just the untaught
       parts about how to use it as a researcher.  Equal to the D level.

   * * **F:** Advanced high performance computing
     * Those who are programming the most demanding parallel
       scientific applications.
     * MPI (message passing interface, a parallel programming
       framework), OpenMP (another one), GPU programming, etc.  And
       anything more advanced.

We have material for different learning styles:

.. list-table::
   :header-rows: 1

   * * Video intro
     * Material
     * Local info
     * Exercises

   * * A short video introduction and demo to get you started and show
       you real examples.
     * Reference material to read, which covers anything you may need.
     * If your university has specific local information to supplement
       the general info, it can be found here.
     * Practice exercises.  In the future, doing these will allow you
       to get study credits.

.. _course:

The course
==========

..
 .. toctree::

   about
   genindex


.. _A:

A: Basics
~~~~~~~~~

.. course-table::
   :header-rows: 1
   :file: ../courses/A.yaml



B: Related science skills
~~~~~~~~~~~~~~~~~~~~~~~~~

.. course-table::
   :header-rows: 1
   :file: ../courses/B.yaml



C: Scientific computing
~~~~~~~~~~~~~~~~~~~~~~~

.. course-table::
   :header-rows: 1
   :file: ../courses/C.yaml


**Other courses:**

.. course-table::
   :header-rows: 1
   :file: ../courses/C2.yaml



D: Clusters and High performance computing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. course-table::
   :header-rows: 1
   :file: ../courses/D.yaml



E: Scientific coding
~~~~~~~~~~~~~~~~~~~~

.. course-table::
   :header-rows: 1
   :file: ../courses/E.yaml



F: Advanced high performance computing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. course-table::
   :header-rows: 1
   :file: ../courses/F.yaml



..
  .. toctree::
   :titlesonly:
   :caption: Programming



* :ref:`genindex`
