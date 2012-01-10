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

Install the latest stable version of ghp-import_, sphinx_ and matplotlib_::

    $ pip install -U ghp-import sphinx matplotlib

If you run the above command outside of any virtualenv you might need to
prefix it with ``sudo``.


.. _`scikit-learn`: https://github.com/scikit-learn/scikit-learn
.. _ghp-import: http://sphinx.pocoo.org/
.. _sphinx: http://sphinx.pocoo.org/
.. _matplotlib: http://matplotlib.sourceforge.net/


Building the doc for the dev version of scikit-learn
----------------------------------------------------

The following will fetch the source from the repo, build ``scikit-learn``
in ``inplace`` mode, build the html documentation with sphinx_ along
with the examples, copy the result to the target folder of the website,
update the ``gh-pages`` branch with ghp-import_ and upload to github::

  $ make

You can also execute each of this steps individually::

  $ make clone
  $ make fetch
  $ make build
  $ make html
  $ make github

In particular only the last step is required if you make a manual change
to the ``webroot/index.html`` file for instance.

Also, **don't forget to commit your changes to ``master`` and push
them too**.


Building the doc for an official stable release
-----------------------------------------------

Here is the command to build the 0.9 from its tag::

  $ make SOURCE_BRANCH=0.9 TARGET_FOLDER=0.9

If the release is also the latest stable release, then::

  $ make SOURCE_BRANCH=0.9 TARGET_FOLDER=stable


Reusing a local scikit-learn clone
----------------------------------

By default the ``Makefile`` will attempt to clone the scikit-learn_
repository to fetch the source of the documentation to build
with sphinx. This clone will be hosted in a local folder named
``scikit-learn``.

If you already have a local scikit-learn, you can reuse it by creating
a symlink called ``scikit-learn``. However when-ever you are building
the documentation you should make sure that you have **no uncommitted
changes** in your working directory or staging area as the Makefile
might try to checkout out of it.


Continuous Integration configuration
------------------------------------

TODO: document here which buildbot or jenkins server is configured to
automatically update and give the email address of the people with the
credentials to update this configuration.


DNS configuration
-----------------

TODO: document the DNS configuration and give the email of the people
with the DNS configuration credentials.
