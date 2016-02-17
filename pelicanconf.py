#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'forin-xyz'
SITENAME = '耕有田，读有书'
SITEURL = 'http://forin-xyz.github.io'

GITHUB_URL = 'http://github.com/forin-xyz/'

# 元数据
# DEFAULT_METADATA = {
#    "Author": 'forin.xyz'

# }

# 主题
THEME = 'mytheme'
THEME_STATIC_DIR = 'output/theme'


# 生成的page名
SLUGIFY_SOURCE = 'basename'

#
AUTHORS_SAVE_AS = ""

# 路径
PATH = 'content'

# 文章种类
USE_FOLDER_AS_CATEGORY = True

# 日期格式
DEFAULT_DATE_FORMAT = '%Y年%m月%d日 星期%a'

# 静态文件
STATIC_PATHS = ['blog', 'downloads', 'images', 'pdfs']
# 文章路径
ARTICLE_PATHS = ['计算机科学', '数学', 'computer']

DUOSHUO_SITENAME = "耕有田，读有书"


ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

# 静态文件
# STATIC_PATHS = ['images', 'pdfs']

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

# 别人博客的链接
LINKS = (('我的导航', 'http://forin-xyz.github.io/tutorial.html'),
         )


# 社交账号
SOCIAL = (('微博', 'http://weibo.com/u/1756830393'),

          ('github', 'http://github.com/forin-xyz'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
