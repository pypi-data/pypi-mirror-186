====
Idem
====

.. image:: https://img.shields.io/badge/made%20with-pop-teal
   :alt: Made with pop, a Python implementation of Plugin Oriented Programming
   :target: https://pop.readthedocs.io/

.. image:: https://img.shields.io/badge/docs%20on-docs.idemproject.io-blue
   :alt: Documentation is published with Sphinx on docs.idemproject.io
   :target: https://docs.idemproject.io/idem/en/latest/index.html

.. image:: https://img.shields.io/badge/made%20with-python-yellow
   :alt: Made with Python
   :target: https://www.python.org/

.. rubric:: Transform configuration into idempotent action.

About
=====

Idem is an idempotent dataflow programming language. It exposes stateful
programming constructs that makes things like enforcing the state
of an application, configuration, SaaS system, or others very
simple.

Since Idem is a programming language, it can also be used for data
processing and pipelining. Idem can be used not only to manage
the configuration of interfaces, but also for complex rule engines
and processing files or workflows.

Idem is a language to glue together management of all sorts of
interfaces. You can think of it like having idempotent
scripts. Automation that can be run over and over again that
enforces a specific state or process.

Idem is unique in that it is built purely as a language. It
can be added to any type of management system out there and can
be applied in a cross platform way easily.

Idem's functionality can also be expanded easily. Instead of storing
all of the language components in a single place, the libraries
used by Idem can be written independently and seamlessly merged
into Idem, just like a normal programming language!

* `idem source code <https://gitlab.com/vmware/idem/idem>`__
* `idem documentation <https://docs.idemproject.io/idem/en/latest/index.html>`__
* `Idem Project Website <https://www.idemproject.io/>`__
* `Idem Project docs portal <https://docs.idemproject.io/>`__

========


What does Idempotent mean?
==========================

The concept of Idempotent is simple! It just means that every time
something is run, it always has the same end result regardless of the state
of a system when the run starts!

At first glance this might seem useless, but think more deeply. Have you
ever needed to make sure that something was set up in a consistent way? It
can be very nice to be able to enforce that setup without worrying about
breaking it. Or think about data pipelines, have you ever had input data
that needed to be processed? Idempotent systems allow for data to be
easily processed in a consistent way, over and over again!

========


How Does This Language Work?
============================

Idem works by taking language files called ``sls`` files and compiling them
down to data instructions. These data instructions are then run through the
Idem runtime. These instructions inform Idem what routines to call to
enforce state or process data. It allows you to take a high level dataset
as your input, making the use of the system very easy.

Idem is built using two critical technologies: ``Python`` and ``POP``. Since Idem
is built on Python, it should be easy to extend for most software developers.
Extending Idem can be very easy because simple Python modules are all you need
to add capabilities!

The other technology, ``POP``, may be new to you. This is the truly secret sauce
behind Idem as well as a number of emerging exciting technologies. ``POP`` stands
for *Plugin Oriented Programming*. It is the brainchild of `the creator of
Salt <https://github.com/thatch45>`__ and a new way to write software. The ``POP``
system makes the creation of higher level paradigms like Idem possible, but also
provides the needed components to make Idem extensible and flexible.

For more information on ``POP``:

* `Intro to Plugin Oriented Programming (POP) <https://pop-book.readthedocs.io/en/latest/>`__
* `pop documentation <https://pop.readthedocs.io/en/latest/>`__
* `pop-awesome <https://gitlab.com/saltstack/pop/pop-awesome>`__
* `pop-create <https://gitlab.com/saltstack/pop/pop-create/>`__

========


Paradigms and Languages, This Sounds Complicated!
=================================================

Under the hood, it is complicated! The guts of a programming language are
complicated, but it is all there to make your life easier! You don't need to
understand complex computer science theory to benefit from Idem. You just need
to learn a few simple things and you can start making your life easier today!
