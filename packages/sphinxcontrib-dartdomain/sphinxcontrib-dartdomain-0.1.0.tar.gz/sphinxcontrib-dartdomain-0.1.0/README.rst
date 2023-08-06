Dart Domain
###########

:author: Hennik Hunsaker <hennik at insidiouslogic.systems>

About
=====

A domain for sphinx >= 1.0 that provides language support for Dart.

The Dart Domain supports the following objects:

* Packages

  * Variables
  * Functions
  * Classes

    * Constants
    * Methods
    * Properties

URLs
====

:PyPI: http://pypi.python.org/pypi/sphinxcontrib-dartdomain
:Detailed Documentation: https://pythonhosted.org/sphinxcontrib-dartdomain/

Quick Sample
============

This is source::

   .. dart:package:: package_info_plus

      .. dart:class:: PackageInfo

         .. dart:method:: fromPlatform()

            :returns: Future\<:dart:class:`PackageInfo`>

Result
------

.. dart:package:: package_info_plus

   .. dart:class:: PackageInfo

      .. dart:method:: fromPlatform()

         :returns: Future\<:dart:class:`PackageInfo`>

Cross referencing
-----------------

From other places, you can create cross references like this::

   Once you install :dart:pkg:`package_info_plus`, you can use
   :dart:meth:`package_info_plus.PackageInfo.fromPlatform` to initialize the
   static attributes of the class.

Result
------

Once you install :dart:pkg:`package_info_plus`, you can use
:dart:meth:`package_info_plus.PackageInfo.fromPlatform` to initialize the
static attributes of the class.

Install
=======

You can install ``dartdomain`` using ``pip``::

   pip -U sphinxcontrib-dartdomain
