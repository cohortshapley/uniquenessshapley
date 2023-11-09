from setuptools import setup, find_packages
import sys

setup(name='uniquenessshapley',
      packages=[package for package in find_packages()
                if package.startswith('uniquenessshapley')],
      install_requires=[
          'numpy',
          'pandas',
          'scipy',
          'requests'
      ],
      description='Uniqueness Shapley',
      author='Benjamin Seiler',
      url='https://github.com/cohortshapley/uniquenessshapley',
      author_email='bbseiler@stanford.edu',
      license='GPL2',
      version='0.1.0')