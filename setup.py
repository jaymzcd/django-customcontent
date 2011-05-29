#!/usr/bin/env python

from setuptools import setup

setup(name='django-customcontent',
      version='0.2',
      description='A django app to allow users to add css/js/html chunks to a page based on the request.path',
      author='Jaymz Campbell',
      author_email='jaymz@jaymz.eu',
      url='https://github.com/jaymzcd/django-customcontent',
      packages=['customcontent',],
     )
