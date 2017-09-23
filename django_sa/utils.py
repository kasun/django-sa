import os


def get_default_settings_module(project_path):
    """ Get default settings module from absolute project path """

    project_dir = os.path.basename(project_path)
    settings_module = '{}.settings'.format(project_dir)
    return settings_module
