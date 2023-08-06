from setuptools import setup

setup(name='fmwrapper',
      version='0.1',
      description='Wrapper for https://facts.museum',
      packages=['fmwrapper'],
      zip_safe=False,
      requires=['requests'])