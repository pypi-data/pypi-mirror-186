from importlib import import_module
import sys


try:
    sys.modules[__name__] = import_module('squishtest.squishtest%d' % sys.version_info.major)
except ImportError as e:
    if 'No module named' in str(e):
        raise ImportError("Cannot load %s module with this Python version" % __name__)
    else:
        raise



