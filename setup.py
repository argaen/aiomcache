import os
import sys
from setuptools import setup, find_packages

version = '0.1'

if sys.version_info >= (3,4):
    install_requires = []
else:
    install_requires = ['asyncio']

tests_require = install_requires + ['nose']


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


setup(name='aiomemcache',
      version=version,
      description=('Minimal pure python memcached client'),
      long_description='\n\n'.join((read('README.rst'), read('CHANGES.txt'))),
      classifiers=[
          'License :: OSI Approved :: BSD License',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Internet :: WWW/HTTP'],
      author='Nikolay Kim',
      author_email='fafhrd91@gmail.com',
      url='https://github.com/fafhrd91/aiomemcache/',
      license='BSD',
      packages=find_packages(),
      install_requires = install_requires,
      tests_require = tests_require,
      test_suite = 'nose.collector',
      include_package_data = True)