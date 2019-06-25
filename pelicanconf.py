#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Renato Oliveira'
SITENAME = 'Hi!'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'pelican-hyde'
PROFILE_IMAGE = 'crying_cat.png'

BIO = '''
My name is Renato and I write about Salesforce.
'''
# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/renatofox/'),
          ('cloud', 'https://trailhead.salesforce.com/credentials/certification-detail-print?searchString=Z5F3tOBg9aG28if2yQ0tYW/DXl6bRAZFUCqNiOiXrXh0s6X2gF8u2nOZr94S/UrD'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True