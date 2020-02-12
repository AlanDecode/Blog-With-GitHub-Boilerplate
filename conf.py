# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/arley.cn/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "Arley517693777/arley.cn@gh-pages"
}

# 站点设置
site_name = "Arley's Blog"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "Arley"
email = "arley@arley.cn"
author_homepage = "https://www.arley.cn"
description = "Living without an aim is like sailing without a compass。<br>生活没有目标，犹如航海没有罗盘。"
key_words = ['Maverick', 'arley', 'Galileo', 'blog']
language = 'zh-CN'

nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "读书",
        "url": "${site_prefix}read/",
        "target": "_self"
    },
    {
        "name": "电影",
        "url": "${site_prefix}movies/",
        "target": "_self"
    },
    {
        "name": "音乐",
        "url": "${site_prefix}musics/",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/Leon517693777?s=05",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/Arley517693777",
        "icon": "gi gi-github"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
