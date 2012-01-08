scikit-learn.org website publishing tools
=========================================

This git repository hosts the prebuilt HTML and resources of the
http://scikit-learn.org website in its ``gh-pages`` branch along with
the tools to build and upload in its master branch.

We don't use the official `scikit-learn`_ repo to do this to avoid to
force regular developers to download all the generated website graphical
resources when cloning the source tree just to build and use the software.


Dependencies
------------

We assume that you already git-cloned and built `scikit-learn`_
sucessfully and that all tests pass when running ``make`` in the top
level source folder.

Install the latest stable version of sphinx_ and matplotlib_.

.. _`scikit-learn`: https://github.com/scikit-learn/scikit-learn
.. _sphinx: http://sphinx.pocoo.org/
.. _matplotlib: http://matplotlib.sourceforge.net/


Building the doc for the dev version of scikit-learn
----------------------------------------------------

TODO: write me!


Building the doc for an official stable release
-----------------------------------------------

TODO: write me!


Continuous Integration configuration
------------------------------------

TODO: document here which buildbot or jenkins server is configured to
automatically update and give the email address of the people with the
credentials to update this configuration.


DNS configuration
-----------------

TODO: document the DNS configuration and give the email of the people
with the DNS configuration credentials.
