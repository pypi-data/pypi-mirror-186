=============================
django-simple-user
=============================

.. image:: https://badge.fury.io/py/simple_user.svg
    :target: https://badge.fury.io/py/simple_user

.. image:: https://travis-ci.org/tomasgarzon/simple_user.svg?branch=master
    :target: https://travis-ci.org/tomasgarzon/simple_user

.. image:: https://codecov.io/gh/tomasgarzon/simple_user/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/tomasgarzon/simple_user

Simple reusable user storing only uuid and manage JWT Token auth_uuidentication in remote

Documentation
-------------

The full documentation is at https://simple_user.readthedocs.io.

Quickstart
----------

Install django-simple-user::

    pip install simple_user

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'auth_uuid.apps.AuthConfig',
        ...
    )

Add django-simple-user's URL patterns:

.. code-block:: python

    from auth_uuid import urls as auth_uuid_urls


    urlpatterns = [
        ...
        url(r'^', include(auth_uuid_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
