from setuptools import setup, find_packages
import os

version = '1.0b2'

setup(name='raptus.autocompletewidget',
      version=version,
      description="archetypes autocomplete widget",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone archetypes widget autocomplete',
      author='Raptus AG',
      author_email='dev@raptus.com',
      url='http://plone.org/products/raptus.autocompletewidget',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['raptus'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
