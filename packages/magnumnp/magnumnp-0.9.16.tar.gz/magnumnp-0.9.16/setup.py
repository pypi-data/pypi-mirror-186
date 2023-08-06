#!/usr/bin/env python

from distutils.core import setup

setup(name='magnumnp',
      version='v0.9.16',
      description='magnum.np finite-difference package for the solution of micromagnetic problems',
      author='Florian Bruckner',
      author_email='florian.bruckner@univie.ac.at',
      url='http://micromagnetics.org/magnum.np/',
      packages=['magnumnp', 'magnumnp.common', 'magnumnp.field_terms', 'magnumnp.loggers', 'magnumnp.solvers', 'magnumnp.utils'],
      install_requires = [
            'torch',
            'numpy',
            'scipy',
            'setproctitle',
            'pyvista',
            'xitorch'
            ]
     )
