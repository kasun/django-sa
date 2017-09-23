=============================
django-sa
=============================

Utility to convert a python script into a standalone django script.
For Python2/Python3 and Django 1.7+

Installation
----------

Install::

    pip install django-sa

Implementation Notes with Short Examples
----------

What happens when you try to run a script with django code in it?::

    python backup.py

.. code-block:: python

    Traceback (most recent call last):
    File "backup.py", line 6, in <module>
    ↓
    ↓
    ↓
    django.core.exceptions.ImproperlyConfigured: Requested setting DEFAULT_INDEX_TABLESPACE, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.

django-sa way::

+ The script needs to be run from the project root directory
+ This uses the default django settings file which is in project_dir/settings.py

.. code-block:: python

    from django_sa import setup_django
    setup_django(__file__)

    # django code

Using a different django settings file:

.. code-block:: python

    from django_sa import setup_django
    setup_django(__file__, 'my_project.settings.production')

    # django code
