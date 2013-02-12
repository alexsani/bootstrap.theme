from setuptools import setup, find_packages
import os

version = '1.0.0'

setup(name='bootstrap.theme',
      version=version,
      description="Diazo Plone theme based on Twitter Bootstrap",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Alex Sani',
      author_email='alexsani.re@gmail.com',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['bootstrap'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          'plone.app.themingplugins',
          'plone.app.jquery >= 1.7.1.1',
          'plone.app.jquerytools >= 1.5.1',
      ],
      extras_require={
        'test': ['plone.app.testing',]
      },

      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
