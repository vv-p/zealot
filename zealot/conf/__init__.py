"""
Settings and configuration for Zealot.
"""

import importlib
import os

from zealot.conf import defaults

ENVIRONMENT_VARIABLE = 'ZEALOT_SETTINGS_MODULE'


class Settings:
    def __init__(self, settings_module=None):
        for setting in dir(defaults):
            if setting.isupper():
                setattr(self, setting, getattr(defaults, setting))

        self.settings_module = settings_module or os.environ.get(ENVIRONMENT_VARIABLE)
        if settings_module:
            user_settings = importlib.import_module(settings_module)

            for setting in dir(user_settings):
                if setting.isupper():
                    setattr(self, setting, getattr(user_settings, setting))


settings = Settings()
