=============================
Hands-on Scientific Computing
=============================

The transition between courses and exercise and computational research
can be difficult - there are so many important things to know that
aren't academic, thus they aren't taught in courses.  This guide is
your starting point - we guide you through the practical tools and
tricks that you would otherwise have to figure out on your own or
learn from friends.

Hands-on SciComp is a "map" of diverse skills that you need for
scientific computing, which are often not directly taught in classes
these days.  It is the practice

Using the material
------------------

This is primarily a self-study course and reference material, which
you can browse at your own pace as it becomes relevant to you.  A
coordinated set of levels (~1 day) and modules (~ 1 hour) splits
skills into levels depending on your needs.  A course instructor or
research supervisor might point you at what is most important for your
current work.  Then, focus on those levels at your own pace.


.. image:: levels.svg
   :align: center
   :alt: Level dependencies
   :scale: 75%


This course is coordinated by `Aalto University Science-IT`_ (See
:doc:`about` for contact info)

.. _Aalto University Science-IT: https://scicomp.aalto.fi/about/


Study credits
-------------

If you are at Aalto University, you can get :doc:`study credits
<study-credits>`.  If you are in Finland but not Aalto, :doc:`you can
get credits via the free FiTech program <fitech-info>`.


Course video introduction
-------------------------

See course video introduction series `here <https://www.youtube.com/playlist?list=PLZLVmS9rf3nOkAFz63oKNSOKk7N47PoSJ>`__


Outline
-------

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

We have material for different learning styles: you might prefer to
watch a video to see quick live examples, or read something for more
detail.  All of these aspects compliment each other, and you can do
what suits you the best.



.. _course:

.. toctree::
   :hidden:

   Home <https://hands-on.coderefinery.org/>

.. _A:

A: Basics
~~~~~~~~~

What's available?  How can it be found?  What basic things do you need
to install?

.. toctree::
   :caption: The material
   :hidden:

   A


.. course-table::
   :header-rows: 1
   :file: ../courses/A.yaml

..
   See the :doc:`full list <A>` for more.





B: Related science skills
~~~~~~~~~~~~~~~~~~~~~~~~~

Assorted things that help you with your work, but not directly related
to doing computations.

.. toctree::
   :hidden:

   B


.. course-table::
   :header-rows: 1
   :file: ../courses/B.yaml

..
   See the :doc:`full list <B>` for more.





C: Linux and shell
~~~~~~~~~~~~~~~~~~

The basics which everything else is built on.

.. toctree::
   :hidden:

   C

.. course-table::
   :header-rows: 1
   :file: ../courses/C.yaml

..
   See the :doc:`full list <C>` for more.





D: Clusters and High Performance Computing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using advanced computational resources.  This will be highly
site-specific.  We include some basic information here, but you will
always have to refer to specific site's instructions.

.. toctree::
   :hidden:

   D

.. course-table::
   :header-rows: 1
   :file: ../courses/D.yaml

..
   See the :doc:`full list <D>` for more.





E: Scientific coding
~~~~~~~~~~~~~~~~~~~~

This isn't about doing the programming itself, but managing it in
research projects.  A prerequisite is knowing some programming
language already.

.. toctree::
   :hidden:

   E

.. course-table::
   :header-rows: 1
   :file: ../courses/E.yaml

..
   See the :doc:`full list <E>` for more.





F: Advanced high performance computing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assorted advanced topics which we can't go into details of, but might
be interesting to you.

.. toctree::
   :hidden:

   F

.. course-table::
   :header-rows: 1
   :file: ../courses/F.yaml

..
   See the :doc:`full list <F>` for more.





.. toctree::
   :caption: About
   :hidden:

   about
   study-credits
   fitech-info
   for-teachers

.. toctree::
   :hidden:
   :caption: Other virtual courses

   coderefinery
   hpc-kickstart

.. toctree::
   :caption: See also
   :hidden:

   similar

..
   * :ref:`genindex`
