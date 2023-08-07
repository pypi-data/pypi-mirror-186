__all__ = []
import sys
import os
import inspect
from runpy import run_module
_importer = os.path.dirname(inspect.getouterframes(inspect.currentframe())[-1].filename)
if _importer:
    _pypackages_dir = os.path.realpath(os.path.join(_importer, '__pypackages__'))
    if os.path.isdir(_pypackages_dir):
        _requirements_file = os.path.join(_pypackages_dir, 'requirements.txt')
        if os.path.isfile(_requirements_file):
            _old_exit = sys.exit
            _old_argv = sys.argv
            sys.exit = lambda x: {}
            sys.argv = ['pip', 'install', '--upgrade', '--prefix', _pypackages_dir, '-r', _requirements_file]
            run_module('pip', run_name='__main__', alter_sys=True)
            sys.argv = _old_argv
            sys.exit = _old_exit
        for _site_packages in [os.path.join(root, dir)
                          for root, dirs, files in os.walk(_pypackages_dir)
                          for dir in dirs
                          if dir == 'site-packages']:
            if _site_packages not in sys.path:
                sys.path.insert(1, _site_packages)
