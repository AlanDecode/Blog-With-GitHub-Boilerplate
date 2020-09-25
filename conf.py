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
    "repo": "sjwayrhz/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "道生一，一生二，二生三，三生万物"
site_logo = "${static_prefix}logo.png"
site_build_date = "2015-01-10T00:00+08:00"
author = "Taoist Monk"
email = "taoistmonk@163.com"
author_homepage = "https://www.sjhz.tk"
description = "戒律 性命双修"
key_words = ['Taoist Monk', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "sjwayrhz",
        "url": "https://github.com/sjwayrhz",
        "brief": "作者的github空间"
    },
    {
        "name": "爱生云鹤",
        "url": "http://blog.sina.com.cn/u/1242294255",
        "brief": "爱生云鹤的微博"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
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
        "name": "Facebook",
        "url": "https://www.facebook.com/profile.php?id=100030415567861",
        "icon": "gi gi-facebook"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/sjwayrhz",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "http://blog.sina.com.cn/u/1242294255",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
