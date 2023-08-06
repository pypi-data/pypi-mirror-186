.. contents:: Table of Contents:


About
-----

Slpkg is a software package manager that installs, updates and removes packages on `Slackware <http://www.slackware.com/>`_-based systems.
It automatically calculates dependencies and figures out what things need to happen to install packages. 
Slpkg makes it easier to manage groups of machines without the need for manual updates.

Slpkg works in accordance with the standards of the `SlackBuilds.org <https://www.slackbuilds.org>`_ organization to build packages. 
It also uses the Slackware Linux instructions for installing, upgrading or removing packages.

.. image:: https://gitlab.com/dslackw/images/raw/master/slpkg/slpkg_package.png
    :target: https://gitlab.com/dslackw/slpkg


Requirements
------------

.. code-block:: bash

    SQLAlchemy >= 1.4.36
    pythondialog >= 3.5.3
    progress >= 1.6

Install
-------

Install from the official third-party `SBo repository <https://slackbuilds.org/repository/15.0/system/slpkg/>`_ or directly from source:

.. code-block:: bash

    $ tar xvf slpkg-4.5.0.tar.gz
    $ cd slpkg-4.5.0
    $ ./install.sh

Screenshots
-----------

.. image:: https://gitlab.com/dslackw/images/raw/master/slpkg/slpkg_install.png
    :target: https://gitlab.com/dslackw/slpkg

.. image:: https://gitlab.com/dslackw/images/raw/master/slpkg/slpkg_remove.png
    :target: https://gitlab.com/dslackw/slpkg

.. image:: https://gitlab.com/dslackw/images/raw/master/slpkg/slpkg_dependees.png
    :target: https://gitlab.com/dslackw/slpkg

.. image:: https://gitlab.com/dslackw/images/raw/master/slpkg/slpkg_view_packages.png
    :target: https://gitlab.com/dslackw/slpkg


Usage
-----

.. code-block:: bash

    $ slpkg --help
      USAGE: slpkg [OPTIONS] [COMMAND] <packages>

      DESCRIPTION:
        Packaging tool that interacts with the SBo repository.

      COMMANDS:
        update                        Update the package lists.
        upgrade                       Upgrade all the packages.
        check-updates                 Check for news on ChangeLog.txt.
        configs                       Edit the configuration file.
        clean-logs                    Clean dependencies log tracking.
        clean-tmp                     Deletes all the downloaded sources.
        -b, build <packages>          Build only the packages.
        -i, install <packages>        Build and install the packages.
        -d, download <packages>       Download only the scripts and sources.
        -r, remove <packages>         Remove installed packages.
        -f, find <packages>           Find installed packages.
        -w, view <packages>           View packages from the repository.
        -s, search <packages>         Search and print packages from the repository.
        -e, dependees <packages>      Show which packages depend.
        -t, tracking <packages>       Tracking the packages dependencies.

      OPTIONS:
        --yes                         Answer Yes to all questions.
        --jobs                        Set it for multicore systems.
        --resolve-off                 Turns off dependency resolving.
        --reinstall                   Upgrade packages of the same version.
        --skip-installed              Skip installed packages.
        --full-reverse                Full reverse dependency.
        --search                      Search packages from the repository.
        --no-silent                   Disable silent mode.

        -h, --help                    Show this message and exit.
        -v, --version                 Print version and exit.

    Edit the configuration file in the /etc/slpkg/slpkg.toml
    or run 'slpkg configs'.
    If you need more information try to use slpkg manpage.


Configuration files
-------------------

.. code-block:: bash

    /etc/slpkg/slpkg.toml
        General configuration of slpkg

    /etc/slpkg/blacklist.toml
        Blacklist of packages

Donate
------

If you feel satisfied with this project and want to thanks me make a donation.

.. image:: https://gitlab.com/dslackw/images/raw/master/donate/paypaldonate.png
   :target: https://www.paypal.me/dslackw


Copyright
---------

- Copyright 2014-2023 © Dimitris Zlatanidis.
- Slackware® is a Registered Trademark of Patrick Volkerding. 
- Linux is a Registered Trademark of Linus Torvalds.
