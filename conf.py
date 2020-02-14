# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
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
    "repo": "Arley517693777/arley.github.io@gh-pages"
}

# 站点设置
site_name = "Arley's Blog"
site_logo = "${static_prefix}Arley.png"
site_build_date = "2019-09-09T09:59+08:00"
author = "Arley"
email = "arley@arley.cn"
author_homepage = "https://www.arley.cn"
description = "Living without an aim is like sailing without a compass。<br>生活没有目标，犹如航海没有罗盘。"
key_words = ['Maverick', 'arley', 'Galileo', 'blog']
language = 'zh-CN'
background_img = "${static_prefix}bg.png"
external_links = [
    {
        "name": "Arley公众号",
        "url": "http://mp.weixin.qq.com/mp/homepage?__biz=MzIzMTU3NTYwMw==&hid=3&sn=d96053e0ee2ce78dfd76f091f0a145f1&scene=18#wechat_redirect",
        "brief": "分享实用干货！"
    }
]
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

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="shortcut icon" href="${static_prefix}favicon.ico">
'''

footer_addon = ''

body_addon = ''
