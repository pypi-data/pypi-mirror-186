# coding=utf-8

import os
import time


class Configuration:

    _explicit_settings = set()

    def __init__(self):
        # update this dict from default settings (but only for ALL_CAPS settings)
        from applyx.conf import defaults

        for setting in dir(defaults):
            if setting.isupper():
                setattr(self, setting, getattr(defaults, setting))

        if hasattr(time, "tzset") and self.TIME_ZONE:
            os.environ["TZ"] = self.TIME_ZONE
            time.tzset()

    def merge_config_module(self, config_module):
        for setting in dir(config_module):
            if setting.isupper():
                setting_value = getattr(config_module, setting)
                setattr(self, setting, setting_value)
                self._explicit_settings.add(setting)

    def is_overridden(self, setting):
        return setting in self._explicit_settings

    def convert_prefix_config(self, prefix):
        config = {}
        for setting in dir(self):
            if setting.isupper() and setting.startswith(prefix):
                config[setting[len(prefix) :]] = getattr(self, setting)

        return config

    def dump(self):
        config = {}
        for setting in dir(self):
            if setting.isupper():
                config[setting] = getattr(self, setting)

        return config

