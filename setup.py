try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='EmotiReader'
    packages=['EmotiReader'],
    package_dir={'':'src'}
)