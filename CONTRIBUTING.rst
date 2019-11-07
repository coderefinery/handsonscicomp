How to contribute
=================

Your help is needed for Hands-on SciComp!  There is so much good
material that your help is needed in order to find the best.  Don't
worry, it's easy to contribute.



Design philosophy
-----------------
If you're doing extensive contributions, check out the `design
phisolophy <DESIGN.rst>`.  This gives you an idea of the overall
arrangement, but is not needed to contribute ideas to individual
modules.

The most important thing to consider is the length of the courses.  We
have these terms:

* **Overview:** 10-15 minute light reading, which explains a) why the
  topic is interesting b) why and when the topic is useful c) shows a
  brief example of using it and the outcome.
* **Introduction:** about an hour, shows how to do the minimum amount
  needed to do something useful.  Should form a complete mental model,
  so that students can begin to search for their own information.
* **Course:** Half day to day of material, goes into depth to make an
  independent user.

Video overviews should be overviews (obviously), the reading material
should be introductions, and courses should be under extra
information.



Github issues
-------------
You can always just file a Github issue with your suggestions.



How to add material directly
----------------------------
In general, don't worry: just look at what's there and copy it!  It's
simple, if you make a mistake someone else can always fix it.

Edit the file ``courses/A.yaml`` (or so on for any other level).  This
is where all material is defined.  The ``A-extra.yaml`` (and so on)
files are extra stuff, which is displayed on the level page but not
the main page.

In order for the prolog/epilog/see also to appear, you must create a
**course page**.  The course page is produced using by copying the
template ``source/A/XNN.rst.template`` to the right location.
Everything will be automatically populated - there is no need to even
change the title.



YAML schema
-----------
Let's show by example.  All normal YAML syntax can be used.  The
course ID is taken from the first word of the ``id`` line::

  - id: X01 This is the title
    desc: This is the description.
    video: |
      `Some video <https://example.com/abcdefghij>`__
    reading: |
      `X01 tutorial <https://example.com/tutorial>`__
    exercises: |
      Exercises are not actually rendered yet, but see `Something <https://example.com/tutorial>`__

    prolog: |
      This text is before the table on the course page.

      Multiple paragraphs are OK.

    epilog: |
      This text is after the table on the course page

``desc``, ``video``, ``reading``, ``exercises`` are all shown on the
front page (in addition to ``ID-local`` if it's defined in the local
substitutions - it can't be in the main YAML).

To create a site-specific extensions, copy ``sites/aalto/`` as an
example.  ``README.rst`` explains how to build your local version.
You can use the substitutions ``ID-local`` (the most important), and
to override all the others ``ID-desc``, ``ID-video``, ``ID-reading``,
``ID-prolog``, ``ID-epilog``.  as substitutions.  There is also the
special ``ID-prolog-local`` and ``ID-epilog-local``.
