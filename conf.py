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
site_build_date = "2019-12-18T16:51+08:00"
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
        "url": "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzIzMTU3NTYwMw==&scene=123&uin=NjA3Mzg1ODgx&key=ac35f96b417667e5b347cd2555d13036d5b8597d41321c23cd9710ec3fbd890057239f9d75fe1f22abe4bd7502178132a915189f3bdb955302e95b4134c3881b2a6827946b4143a1bbd2081d7c310ff0&devicetype=Windows+7&version=62080074&lang=zh_CN&a8scene=1&pass_ticket=r%2FJVeu95vpQpCjOB7F6EJYN02iiWmEEMHBBPzuSoye384c1E0iviUJf%2FqadRTHIZ",
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
<link rel="shortcut icon" href="${static_prefix}favicon.ico">
'''

footer_addon = ''

body_addon = ''
