import os
import re
from typing import Union


class D:
    def __init__(self, data):
        self.data = data


___ = D("")


class DesignConfig:

    def __init__(self, data: dict = os.environ):
        self._data = data

        for attr in dir(self):
            if not attr.startswith('_'):
                setattr(self, attr, self(attr))

    def __call__(self, template: str, default: str = None):
        if type(template) != str:
            return template

        reg = re.compile(r'{([^{}]*)}')
        if not reg.search(template):
            return self._get(template, default)

        template = self._get_format(template)
        if default and reg.search(template):
            return default
        else:
            return template

    def _get(self, key, default: str = None):
        if hasattr(self, key):
            value = getattr(self, key)
            if type(value) == D:
                type_value = type(value.data)

                assert type_value in [str, bool, int, float], \
                    f"D-function only handles atomic values, not {type_value}"

                if key not in self._data:
                    value = value.data
                else:
                    value = self._data[key]

                    if type_value is bool:
                        if type(value) == str:
                            if value.lower() in ['false','no','0']:
                                value = False
                        value = bool(value)
                    elif type_value is int:
                        try:
                            value = int(value)
                        except ValueError:
                            value = 0
                    elif type_value is float:
                        try:
                            value = float(value)
                        except ValueError:
                            value = 0

            if type(value) == str:
                return self._get_format(value)
            else:
                return value

        elif default is not None:
            return default
        else:
            return key

    def _get_format(self, template: str, path=()):
        if len(path) != len(set(path)):
            return template
        reg = re.compile(r'{([^{}]*)}')
        if reg.search(template):
            return template.format(**{key: self._get_format(self._get(key), path+(key,)) for key in reg.findall(template)})
        else:
            return template

    def __getitem__(self, item):
        return self(item)

    def __str__(self):
        return '\n'.join([f'{attr}\t->\t{self._get(attr)}' for attr in dir(self) if not attr.startswith('_')])

    def path(self, *args):
        return self(os.path.join(*args))

