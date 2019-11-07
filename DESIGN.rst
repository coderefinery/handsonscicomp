Design of course modules
========================

This page documents the overall reasoning behind choosing our levels
and modules, and helps you in proposing new modules.

Each level should have a reasonably small number of modules on the
front page - something that we can consider the "theoretical minimum".
Of course it won't cover everything, but it should be able to let
people know what the important aspects are.  There can be more
supplementary material on later pages.



Levels
------

Rather than throw a bunch of stuff at people, we want to classify it
into logical **levels** so that one can say, for example, "if you are
doing research X you need to be at level D".  We want enough levels to
express what is needed, but not too much to overwhelm people.

We initially put scientists into three categories.  Our core focus is
the second two:

* You just run applications (we don't target this in our course)
* You need to script applications or libraries together ("Linux"-level, C)
* You need to run stuff using HPC or clusters - ("HPC"-level, D)

So we got these levels:

* **A**: Basics about your site.  Doesn't go into anything technical,
  but makes sure you know who you should ask for help, and what local
  best practices are.  This should be a part of the normal induction
  process, so that you don't get a "oh, I didn't know we had a
  cluster" right before someone graduates.

  * After this level, a new researcher is able to know who what
    resources they may need to use later and how to ask for help when
    they need it.

* **B**: A "sideshow" of background knowledge but isn't really about
  computation specifically.  Things that are often missed in academic
  courses like making good figures and LaTeX.  This includes data
  management, Jupyter, "what is open source", and why to give your
  stuff a license.

  * After this level, a researcher is not lost with things like
    managing their data, LaTex, making figures, etc. when when
    computational groups.  Basically, a first step beyond the world of
    "Word, Excel, Powerpoint".

* **C**: The "Linux user's level", this is focused on shell stuff and
  basic tools (regardless of operating system).  Version control,
  shell scripting, automation, and so on.

  * After this level, a researcher is able to use the benefits of
    Linux/shell locally.  They can run run programs from the command
    line, automate things, not be lost when following directions found
    online, and use version control to keep things tidy.

* **D**: It's a minor step to HPC work.  A lot of this is about batch
  systems and HPC data management.  The "use remote servers without
  batch systems" is a middle case somewhere between C and D.

  * After this level, a researcher is able to use remote computer
    clusters.  They already have basic shell knowledge, this focuses
    on automating things, batch systems, more scripting, and
    parallelism.

* **E**: Scientific programming: advanced version control, testing,
  packages.  This doesn't need to be one of the more advanced topics,
  but we choose to focus on using other people's work first.  This
  types of material takes you from an academic programmer to a
  research programmer.

  * After this level, a researcher is able to produce high-quality
    research code.  They can properly modularize, test, package, and
    in general run/be part of open source projects.

* **F**: Anything more advanced that is special-use.  For example,
  writing your own MPI applications.  We'd expect that most people
  pick and choose from here as they need to.

  * After this level, a researcher is able to act independently in
    almost every aspect of scientific computing.  Of course, the
    learning never ends.



Course IDs
----------

**Course IDs** provide a way to link the data together, and a sense of
seriousness.  A course ID consists of the level's letter and two numbers,
e.g. ``A01``.

* 00-19 are "basics" for that level.
* 20-79 are the core technical material.
* 80-99 are advanced level courses.

Numbering within this is sort of ad-hoc but we'll try to make
patterns.  For example, ``x30`` -- ``x39`` can be the range of version
control (which can also connect to ``E`` level), from more basic to
more advanced.  We'll just see how it goes.

We want the course numbers to make somewhat of sense, but also we
don't want them to change without good reason.  This probably means
they will end up being disorganized and we shouldn't worry so much
about them.

If only we use them, it doesn't matter if they change so much.  But
they could link across projects, or be used to track progress towards
earning credits.



Modules
-------

Each **module** should ideally be no longer than an hour to get a basic
understanding.  You should be able to explain the point in one
sentence.  There can, of course, be advanced follow-up material too.



Types of courses
----------------

Please think of the following types of courses when adding material:

* **Overview:** 10-15 minute light reading, which explains a) why the
  topic is interesting b) why and when the topic is useful c) shows a
  brief example of using it and the outcome.
* **Introduction:** about an hour, shows how to do the minimum amount
  needed to do something useful.  Should form a complete mental model,
  so that students can begin to search for their own information.
* **Course:** Half day to day of material, goes into depth to make an
  independent user.



Material
--------

We try to have different types of video material for each thing we cover:

* **Video intro:** "An example is worth a thousand pictures".  We start
  with a simple video which motivates and explains the why, not goes
  into the how.  Some real examples of the end state would be good.
  It should make people interested in moving to the reading material
  if they need it - and able to understand it.
* **About:** Tell the people why it's important directly and so that they
  can tell how it applies to them.
* **Reading:** bulk reference material.  Can be both tutorials and
  reference.  Ideally try to have some of both.
* **Local material:**. Via the substitution system, you can add another
  column which has some material specific to your site.
* **Exercises:** practice for those who would like to get credit.  Not
  implemented yet.
