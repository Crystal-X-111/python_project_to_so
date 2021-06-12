import os
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize


REQUIRED = [
    'cmake', 'scikit-build',
    'numpy', 'python-rapidjson', 'protobuf>=3.5.0', 'grpcio',
]

# Override standard setuptools commands.
# Enforce the order of dependency installation.
#-------------------------------------------------

from setuptools.command.install import install

def requires( packages ):
    from os import system
    from sys import executable as PYTHON_PATH
    from pkg_resources import require
    require( "pip" )
    CMD_TMPLT = '"' + PYTHON_PATH + '" -m pip install %s'
    for pkg in packages: system( CMD_TMPLT % (pkg,) )

class OrderedInstall( install ):
    def run( self ):
        # requires( REQUIRED )
        install.run( self )

CMD_CLASSES = {
    "install" : OrderedInstall
}
#-------------------------------------------------


VERSION = "0.1"

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):

        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False

        def get_tag(self):
            pyver, abi, plat = 'py3', 'none', 'any'
            return pyver, abi, plat
except ImportError:
    bdist_wheel = None

CMD_CLASSES['bdist_wheel'] = bdist_wheel

sourcefiles = [
    'maidabu/bootstrap.py',
    "maidabu/main_module.py",
    "maidabu/utils/__init__.py",
    "maidabu/sub_module_a/__init__.py",
    "maidabu/sub_module_a/test_module_a.py",
    "maidabu/sub_module_a/test_module_b.py",
    "maidabu/sub_module_b/__init__.py",
]

extensions = cythonize(Extension(
    name="maidabu.bootstrap",
    sources=sourcefiles,
))

kwargs = {
    'name': 'maidabu',
    'version': VERSION,
    'packages': find_packages(),
    'install_requires': REQUIRED,
    'ext_modules': extensions,
    'cmdclass': CMD_CLASSES,
}

setup(**kwargs)
