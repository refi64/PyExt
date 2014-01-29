try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst', 'r') as f:
    readme = f.read()

setup(name='pyext',
      version='0.5',
      author='Ryan Gonzalez',
      author_email='kirbyfan64sos@gmail.com',
      py_modules=['pyext'],
      description='Simple Python extensions.',
      long_description=readme,
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3']
      )

