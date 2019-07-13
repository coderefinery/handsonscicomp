Hands-on Scientific Computing
=============================

Hands-on SciComp is a practical scientific computing reference and course.

Courses
--------



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
