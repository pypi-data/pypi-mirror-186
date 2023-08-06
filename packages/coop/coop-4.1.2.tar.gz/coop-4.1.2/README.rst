Coop - base for all (most) Neon Jungle sites
============================================

This is a base to build all Neon Jungle sites off.
This package contains all the common code shared
between sites, with the ideal Neon Jungle site containing only
model definitions, templates, and front end assets.

Making a release
----------------

Upgrade the version in ``coop/_version.py``.
Coops version stays in step with Wagtail. i.e. Coop 2.4.x uses Wagtail 2.4.x.
Point releases are used to add features during a Wagtail version lifespan.

Update the CHANGELOG. Please.

Tag your release:

.. code-block:: bash

    $ git tag "x.y.z"
    $ git push --tags

And you are done! Gitlab is set up to automatically push the new package to pypi when a tag is pushed.


Local dev
---------

Create a virtual environment, activate and install the requirements:

.. code-block:: bash

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install .


First time you should run migrations and setup a superuser:

.. code-block:: bash

    $ ./manage.py migrate
    $ ./manage.py createsuperuser


You can run and debug the project locally using `./manage.py runserver`, or included is a launch.json for vscode to debug using the debugger.
