#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
AUTHOR = u'Michell Stuttgart'
SITENAME = u'Código Avulso'
SITEURL = 'http://codigoavulso.com.br'
SITE_LOGO = u'images/logo.png'
AUTHOR_PIC_URL = u'https://lh3.googleusercontent.com/-2DmtcIOqPIc/VyPVyYGo09I/AAAAAAAAF58/VBWeR-ejVhECPk4YR6hiHuQJz_RzM_3mgCCo/s601/IMG-20141231-WA0004%2B1.jpg'
AUTHOR_LOCATION = u'Brasil'
AUTHOR_BIO = u'Sou graduado em Engenharia da Computação pela Universidade Federal de Itajubá (UNIFEI) e entusiasta da filosofia do software livre, contribuidor de diversos projetos Open Source (incluindo projetos próprios) e feliz usuário linux.'
SITE_DESCRIPTION = 'Meu blog sobre tecnologia, livros, linux e outras nerdices.'
TAG_LINE = '# sudo apt-get install faith hope love'
AUTHOR_EMAIL = 'michellstut@gmail.com'
LINKEDIN_URL = 'https://www.linkedin.com/in/michellstut'

# Development
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = u'pt'
SITE_LANG = 'pt_BR'
SITE_LANG_ALTERNATE = 'en_GB'
DEFAULT_PAGINATION = 10
THEME = 'casper-pelican-theme'

FEED_RSS = 'feed'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GITHUB_URL = 'https://github.com/mstuttgart'
DISQUS_SITENAME = 'codigoavulso'
# USE_OPEN_GRAPH = 'True'
RELATED_POSTS_MAX = 10
GOOGLE_ANALYTICS = 'UA-75274475-1'

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', '404')
# [Casper2Pelican] Header images
DEFAULT_HEADER_IMAGE = u'images/back7.jpg'
ARCHIVE_HEADER_IMAGE = u'images/back7.jpg'
ABOUT_HEADER_IMAGE = u'images/mountains_sky_landscape_rocks.jpg'
COPYRIGHT = 'Copyright &copy; 2016'
DELETE_OUTPUT_DIRECTORY = True

# Blogroll
SOCIAL =  (
    ('Github', 'https://github.com/mstuttgart'),
    ('Linkedin', 'https://www.linkedin.com/in/michellstut'),
    )

PLUGIN_PATHS = ["pelican-plugins",]
PLUGINS = ['neighbors','minification','sitemap']

SITEMAP = {
    'format': 'xml',
        'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
STATIC_PATHS = [
    'images',
    'extra/CNAME',
    'extra/favicon.ico',
    'static/browserconfig.xml',
    'static/large.png',
    'static/square.png',
    'static/tiny.png',
    'static/wide.png',
    'static/socialmedia.txt',
]
EXTRA_PATH_METADATA = {
    'static/browserconfig.xml': {
        'path': 'browserconfig.xml'
    },
    'static/large.png': {
        'path': 'large.png'
    },
    'static/square.png': {
        'path': 'square.png'
    },
    'static/tiny.png': {
        'path': 'tiny.png'
    },
    'static/wide.png': {
        'path':'wide.png'
    },
    'static/socialmedia.txt': {
        'path':'socialmedia.txt'
    },
    'extra/CNAME': {
      'path': 'CNAME'
    },
    'extra/favicon.ico': {
      'path': 'favicon.ico'
    }
}
