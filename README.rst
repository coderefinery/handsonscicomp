Hands-on Scientific Computing
=============================

Hands-on SciComp is a practical scientific computing reference and
course.  The intention is not to make a new course, but to organize
all the best material that is already available and provide better
introductions and motivation.



Courses
--------

See `DESIGN.rst <DESIGN.rst>`__ for the philosophy behind choosing the
courses and levels.



Local customization
-------------------

One primary design criteria is *standard material with local
customizations*.  Thus, we can share the work of finding the overall
best material and still allow local customization - either as
standalone or embedding within another Sphinx project.  This is done
using our custom-developed Sphinx extension `sphinx_ext_substitution
<https://github.com/NordicHPC/sphinx_ext_substitution/>`__.

To make local customizations, see the ``sites/`` directory for
examples.  Define a yaml file with the key ``site-name``, and then any
other substitutions you would like.  Set the path to this file using
``SPHINX_EXT_SUBSTITUTION_PATH`` and you'll get your local version.
See ``sites/aalto/aalto.yaml`` for an example.



Embedding in another Sphinx project
-----------------------------------

These docs are designed to be embedded within another Sphinx project
with your site-specific customizations.  It is not fully automatic
yet, but here are some hints:

::
   git clone <handsonscicomp-url>
   _handsonscicomp --recurse-submodules
      # Link the source path to where you want it to appear, do what
   you want.
   ln -s training _handsonscicomp/source/
   # ensure that PyYAML is installed

If your ``conf.py``::
  sys.path.insert(0, '_handsonscicomp/source/')
  import conf as handsonscicomp_conf
  handsonscicomp_conf.embed(globals())
    globals().setdefault('exclude_patterns',
  []).append('_handsonscicomp')

  # Set substitute_path to your site's own config
  substitute_path = '_handsonscicomp/sites/aalto/'

  def setup(app):
  handsonscicomp_conf.setup(app)



Technical development
----------------------

Structure
~~~~~~~~~
* ``source/``: Sphinx project
* ``courses/``: YAML files defining the "global" courses
* ``sites/``: YAML files defining site-specific (local) course data,
  to fill out the "Local" column.  Site-specific config does *not*
  have to be in this repository, it can be tracked separately and
  referenced with an environment variables.
* ``_ext/``: Sphinx extensions.



Building
~~~~~~~~
* Clone the repo, update the extension submodule.
* ``make html``
* You can set the environment variable
  ``SPHINX_EXT_SUBSTITUTION_PATH`` to the path of your site-local YAML
  configuration.


Maintenance and contributing
----------------------------

This is currently an alpha-level project.  Until there is enough
critical mass for code review, minor changes are pushed directly to
master and more significant changes are pull-requested.

Hands-On Scicomp is currently under the CodeRefinery umbrella, but
currently led by Aalto University.  However, the intention is that
this is a cross-university project so contributions from all members
are considered equally.  Contact: Richard Darst
