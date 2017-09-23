import os
import sys

import django

from .utils import get_default_settings_module


def setup_django(script_file_name, django_settings_module=None):
    """ Run django setup mechanism.

        Args:
            script_file_name (str):
                script file name relative to application root directory
                Can be obtained with __file__
            django_settings_module (str):
                Dotted path to settings module ( my_project.settings.prod )
                Optional, default to project_dir.settings
    """
    abs_path = os.path.realpath(script_file_name)
    project_path = abs_path.replace('/{}'.format(script_file_name), '')
    sys.path.append(project_path)

    if not django_settings_module:
        django_settings_module = get_default_settings_module(project_path)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings_module)
    django.setup()
