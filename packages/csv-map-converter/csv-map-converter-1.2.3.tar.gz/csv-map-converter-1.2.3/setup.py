#!/usr/bin/env python   
try:                    
    from setuptools import setup, find_packages
except:                 
    from distutils.core import setup, find_packages

setup(name='csv-map-converter',
      version='1.2.3',
      description='It is csv converter to be able to get multi-values.',
      author='Sparrow Jang',
      author_email='sparrow.jang@gmail.com',
      url='https://github.com/eHanlin/csv-map-converter',
      packages=find_packages(),
      test_suite = 'tests',
     )

