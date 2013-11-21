try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='pyext',
      version='0.1',
      author='Ryan Gonzalez',
      py_modules=['pyext'],
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3']
      )

