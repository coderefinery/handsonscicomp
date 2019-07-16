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
into logical levels so that one can say, for example, "if you are
doing research X you need to be at level D".  We want enough levels to
express what is needed, but not too much to overwhelm people.

We initially put scientists into three categories:
* You just run applications (we don't target this in our course)
* You need to script applications or libraries together ("Linux"-level, C)
* You need to run stuff using HPC or clusters - ("HPC"-level, D)

So we got these levels:

* **A**: Basics about your site.  Doesn't go into anything technical,
  but makes sure you know who you should ask for help, and what local
  best practices are.  This should be a part of the normal induction
  process, so that you don't get a "oh, I didn't know we had a
  cluster" right before someone graduates.

* **B**: A "sideshow" of background knowledge but isn't really about
  computation specifically.  Things that are often missed in academic
  courses like making good figures and LaTeX.

* **C**: The "Linux user's level", this is focused on shell stuff and
  basic tools (regardless of operating system).  Version control,
  shell scripting, automation, and so on.

* **D**: It's a minor step to HPC work.  A lot of this is about batch
  systems and HPC data management.  The "use remote servers without
  batch systems" is a middle case somewhere between C and D.

* **E**: Scientific programming: advanced version control, testing,
  packages.  This doesn't need to be one of the more advanced topics,
  but we choose to focus on using other people's work first.  This
  types of material takes you from an academic programmer to a
  research programmer.

* **F**: Anything more advanced that is special-use.  For example,
  writing your own MPI applications.  We'd expect that most people
  pick and choose from here as they need to.


Course IDs
----------

Course IDs provide a way to link the data together, and a sense of
seriousness.  A course ID consists of the level's letter and two numbers,
e.g. ``A01``.

* 00-19 are "basics" for that level.
* 20-79 are the core technical material.
* 80-99 are advanced level courses.

Numbering within this is sort of ad-hoc but we'll try to make
patterns.  For example, ``C30`` -- ``C39`` can be a sequence of
version control from more basic to more advanced.  The middle digit
might correspond across levels.  We'll just see how it goes.



Modules
-------

Each module should ideally be no longer than an hour to get a basic
understanding.  You should be able to explain the point in one
sentence.  There can, of course, be advanced follow-up material too.



Material
--------

We try to have different types of video material for each thing we cover:

* Video intro: "An example is worth a thousand pictures".  We start
  with a simple video which motivates and explains the why, not goes
  into the how.  Some real examples of the end state would be good.
  It should make people interested in moving to the reading material
  if they need it - and able to understand it.
* About: Tell the people why it's important directly and so that they
  can tell how it applies to them.
* Reading: bulk reference material.  Can be both tutorials and
  reference.  Ideally try to have some of both.
* Local material: Via the substitution system, you can add another
  column which has some material specific to your site.
* Exercises: practice for those who would like to get credit.  Not
  implemented yet.
