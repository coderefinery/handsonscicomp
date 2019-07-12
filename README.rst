Hands-on Scientific Computing
=============================

Hands-on SciComp is a practical scientific computing reference and course.

Courses
--------


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
