Pyruse
======

Pyruse allows you to *peruse* metadata about Python releases, namely release
and versioning information. Its chief purpose is to provide said release
information in a script-friendly format to shell scripts, other Python
scripts, and so forth.

This is terrific in a development environment where someone using tools like
pyenv, pythonbrew, virtualenv, etc. can quickly verify the version of Python
they're using with a specific series is actually the most current, as well as
determine which historical versions are valid and available.

It's *especially* terrific for continuous integration environments where it's
handy to be able to know the latest version(s) of Python and where to grab
them. Throwing this into a Jenkins job or a crontabbed script, for instance,
that then automatically grabs new releases and makes them available to other
Jenkins jobs that use tools like tox to test against multiple versions of
Python, is an ideal use case. I know you're not doing this. Why aren't you
doing this?!

Do not deny these claims of terrificness.


Requirements
------------
* Python v2.7, v3.2, or v3.3


Pyrusing Some Stuff
-------------------

This initial release includes a command-line utility, ``pyruse-versions``::

    usage: pyruse-versions [-h] [-d] [-a] [-i] [-u] [series [series ...]]

    Outputs the latest version of Python, or the latest in a specific series or
    set of series.

    positional arguments:
      series                the version series (e.g., 2, 2.7, 3.3, etc.)

    optional arguments:
      -h, --help            show this help message and exit
      -d, --dev             include dev versions
      -a, --all             show all rather than just the latest
      -i, --ignore-unknown  ignore unknown series (otherwise outputs None)
      -u, --source-urls     outputs source tarball URLs for each known version
                            (assumes --ignore-unknown, ignores --dev)

which uses the official Python source repository to obtain a variety of useful
information:

* the latest version number of Python
* the latest version in a series (where a series is a partial version, such as
  2, 3, 2.7, 3.3, etc.)
* the full list of versions within a series
* the full list of versions
* any of the above with development/testing releases included (alpha, beta,
  rc, etc.), by specifying the ``-d`` flag

In addition to the above, the ``-u`` flag will assume you want URLs for any of
the versions it finds matching the series criteria you give it.


Examples
--------

Latest release::

    $ pyruse-versions
    3.3.4

Latest release in the Python 2.x series::

    $ pyruse-versions 2
    2.7.6

All releases in the 2.7.x series::

    $ pyruse-versions 2.7
    2.7.6
    2.7.5
    2.7.4
    2.7.3
    2.7.2
    2.7.1
    2.7

The latest releases in the 3.3.x, 3.2.x, 2.7.x, and 2.6.x series::

    $ pyruse-versions 3.3 3.2 2.7 2.6
    3.3.4
    3.2.5
    2.7.6
    2.6.9

Source tarball URLs for the above::

    $ pyruse-versions -u 3.3 3.2 2.7 2.6
    http://www.python.org/ftp/python/3.3.4/Python-3.3.4.tgz
    http://www.python.org/ftp/python/3.2.5/Python-3.2.5.tgz
    http://www.python.org/ftp/python/2.7.6/Python-2.7.6.tgz
    http://www.python.org/ftp/python/2.6.9/Python-2.6.9.tgz

The last 10 releases in the 3.3 series, including development releases::

    $ pyruse-versions -a -d 3 | head -n10
    3.4.0rc1
    3.4.0b3
    3.4.0b2
    3.4.0b1
    3.4.0a4
    3.4.0a3
    3.4.0a2
    3.4.0a1
    3.3.4
    3.3.4rc1

License
-------
Licensed under the MIT license. See the LICENSE file.
