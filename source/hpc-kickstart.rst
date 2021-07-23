HPC Kickstart (Aalto)
=====================

This page contains a virtual high performance computing (HPC, or more
precisely, cluster computing) kickstart course.  It is not part of the
main Hands-on Scientific Computing flow, but is an expanded version of
the "D" level material.

This page currently contains an online course from Aalto University
(Aalto Scientific Computing), so the exact examples may not work on
other clusters, but the theory and concepts *will* - you need to
combine this outline with documentation from your own site.

In the future, this page will be adjusted to the best topics in the
best order from all courses combined, which means various material may
be mixed-and-matched so that the transitions are not perfect, but it
will still have the best effect overall.



Introductory material
---------------------

These can be used in whatever order suits you, or you can watch the
intro and then go on.

* Day 1 introduction (`Video
  <https://www.youtube.com/watch?v=N3UcSgS-SAw&list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S&index=2>`__,
  `Lecture <https://scicomp.aalto.fi/training/scip/summer-kickstart/intro>`__)
* HPC theory crash course: some background about high-performance and
  cluster computing, not strictly necessary to move on to the other
  material (and could even be watched at the end) (`Video
  <https://www.youtube.com/watch?v=Az9AVl1zatk&list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S&index=3>`__,
  `Slides <https://users.aalto.fi/degtyai1/SCiP2021_kick.HPC_crash_course.2021-06-04.pdf>`__)
* How to ask for help with supercomputers
  (`Video <https://www.youtube.com/watch?v=ZUVdGmSuE0g&list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S&index=12>`__,
  `Slides <https://cicero.xyz/v3/remark/0.14.0/github.com/bast/help-with-supercomputers/main/talk.md/>`__
  )
* Your future in scientific computing. (`Video
  <https://www.youtube.com/watch?v=AJnuOYJIBVo&list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S&index=7>`__,
  `Outline <https://scicomp.aalto.fi/training/scip/summer-kickstart/future/>`__)


Main tutorials
--------------

"How to connect and use software/data" track:

* Connecting to the cluster
  (`Video <https://www.youtube.com/watch?v=A3LafWWxaj4&list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S&index=10>`__
  `Reading <https://scicomp.aalto.fi/triton/tut/connecting/>`__
  `Q&A <>`__
  )
* Data storage
  (`Video <https://www.youtube.com/watch?v=qcaPA44gXM0&list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S&index=13>`__,
  `Reading <https://scicomp.aalto.fi/triton/tut/storage/>`__,
  `Q&A <>`__
  )
* Applications on the cluster
  (`Video <https://www.youtube.com/watch?v=t1aViYuUu-Q&list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S&index=11>`__,
  `Reading <https://scicomp.aalto.fi/triton/tut/applications/>`__,
  `Q&A <>`__)
* Software modules
  (`Video <https://www.youtube.com/watch?v=1zCRVP7Lzes&list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S&index=22>`__,
  `Reading <https://scicomp.aalto.fi/triton/tut/modules/>`__,
  `Q&A <>`__)

"How to actually run stuff" track.  This goes into detail about the
batch system and accessing resources:

* Interactive jobs
  (`Video <https://www.youtube.com/watch?v=9fh5Gh-fkJI&list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S&index=14>`__,
  `Reading <https://scicomp.aalto.fi/triton/tut/interactive/>`__,
  `Q&A <>`__
  )
* Serial jobs
  (`Video <https://www.youtube.com/watch?v=ln4hjNSdZJE&list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S&index=17>`__,
  `Reading <https://scicomp.aalto.fi/triton/tut/serial/>`__,
  `Q&A <>`__)
* Monitoring jobs
  (`Video <https://www.youtube.com/watch?v=Do1BwOL-j8I&list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S&index=18>`__,
  `Reading <https://scicomp.aalto.fi/triton/tut/monitoring/>`__,
  `Q&A <>`__)
* Parallel jobs
  (`Video <https://www.youtube.com/watch?v=B_gDDV7VenU&list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S&index=19>`__,
  `Reading <https://scicomp.aalto.fi/triton/tut/parallel/>`__,
  `Q&A <>`__)
* Array jobs
  (`Video <https://www.youtube.com/watch?v=YLOHj-biU10&list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S&index=20>`__,
  `Reading <https://scicomp.aalto.fi/triton/tut/array/>`__,
  `Q&A <>`__)
* GPU jobs
  (`Video <https://www.youtube.com/watch?v=Ds_WwAJJy3k&list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S&index=21>`__,
  `Reading <https://scicomp.aalto.fi/triton/tut/gpu/>`__,
  `Q&A <>`__)


Special topics
--------------

These special topics can be used in whatever order suits you, if they
are relevant to your interests.

* Scientific computing workflows: different ways of actually using
  computing resources.  Recommended to put the cluster into
  perspective with other types of needs.
  (`Video <https://www.youtube.com/watch?v=ExFbc5EikU0>`__,
  `Reading <https://scicomp.aalto.fi/training/scip/intro-linux-aalto-computing/>`__,
  `Q&A <>`__)
* Currently available resources at CSC, Finland: The above material is
  mostly abut what you can find at one university on a cluster (though
  even bigger clusters use the same interface).  This talks about
  other resources available at a national computing center (other
  countries will be somewhat similar).
  (`Video <https://www.youtube.com/watch?v=BGcKD3oEoyw&list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S&index=5>`__,
  `Reading <https://kannu.csc.fi/s/3K8q93XSwtSgHEa>`__,
  `Q&A <>`__)
* Cluster etiquette: We learned what you can do, but what *should* you
  do to not annoy others on the cluster?  See more in Research
  Software Hour
  (`Video <https://www.youtube.com/watch?v=NIW9mqDwnJE&list=PLpLblYHCzJAB6blBBa0O2BEYadVZV3JYf>`__)
* "How to tame the cluster", mostly the same material as this whole
  course, compressed into one hour, with a complete example worked
  out.
  (`Video <https://www.youtube.com/watch?v=5HN9-MW7Tw8&list=PLpLblYHCzJAB6blBBa0O2BEYadVZV3JYf>`__)


See also
--------

* `Full playlist of June 2021 Aalto kickstart course
  <https://www.youtube.com/playlist?list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S>`__
  and `the course page <https://scicomp.aalto.fi/training/scip/summer-kickstart/>`__.
