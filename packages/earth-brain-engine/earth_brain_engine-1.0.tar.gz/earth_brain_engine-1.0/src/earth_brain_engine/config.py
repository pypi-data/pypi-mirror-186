from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class ConfigDict(dict):
    """内置的配置方法"""
    IMMUTABLE = '__immutable__'

    def __init__(self, *args, **kwargs):
        super(ConfigDict, self).__init__(*args, **kwargs)
        self.__dict__[ConfigDict.IMMUTABLE] = False

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        elif name in self:
            return self[name]
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if not self.__dict__[ConfigDict.IMMUTABLE]:
            if name in self.__dict__:
                self.__dict__[name] = value
            else:
                self[name] = value
        else:
            raise AttributeError(f'Attempted to set "{name}" to "{value}", but AttrDict is immutable')

    def _immutable(self, is_immutable):
        """Set immutability to is_immutable and recursively apply the setting
        to all nested AttrDicts.
        """
        self.__dict__[ConfigDict.IMMUTABLE] = is_immutable
        # Recursively set immutable state
        for v in self.__dict__.values():
            if isinstance(v, ConfigDict):
                v._immutable(is_immutable)
        for v in self.values():
            if isinstance(v, ConfigDict):
                v._immutable(is_immutable)

    def is_immutable(self):
        return self.__dict__[ConfigDict.IMMUTABLE]


cfg = ConfigDict()

# ---------------------------------------------------------------------------- #
# Generic configuration fields
# ---------------------------------------------------------------------------- #
cfg.StopMaxAttemptNumber = 10
cfg.OperatorDirectoryServer = 'http://192.168.1.203:31067'
cfg.OperatorTaskServer = 'http://192.168.1.130:20250'
cfg.RequestTimeout = 60

# ---------------------------------------------------------------------------- #
# Request API Name
# ---------------------------------------------------------------------------- #
cfg.OperatorDirectoryURL = ConfigDict()
cfg.OperatorTaskServerURL = ConfigDict()
cfg.UserAuthToken = ""
