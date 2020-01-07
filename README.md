# Blog-With-GitHub-Boilerplate

> 💡 注意：这不是所谓使用 Maverick 的「标准方法」，只不过是利用 Maverick 与 GitHub Actions 写博客一个流程而已。不要觉得非得这样不可。Maverick 的用法见 [README.md](https://github.com/AlanDecode/Maverick)。

这是博客文章[《完全用 GitHub 写博客》](https://blog.imalan.cn/archives/blog-with-github/)所提出方法的示例仓库。你可以将这个仓库 fork 到自己的账户下（点击右上角的 Fork 按钮），然后按照本文档余下的内容操作一遍，就知道该如何使用了。

> Fork 之后暂时不要修改仓库名称，保持 Blog-With-GitHub-Boilerplate

## 第一步：为仓库开启 Pages 服务

![](https://github.com/AlanDecode/Blog-With-GitHub-Boilerplate/raw/source/assets/image-20191218153736217.png)

进入 Fork 的仓库，点击右上角这个 Settings 按钮，找到 GitHub Pages 相关设置：

![](https://github.com/AlanDecode/Blog-With-GitHub-Boilerplate/raw/source/assets/image-20191218153908353.png)

设置发布来源为 gh-pages branch，稍等片刻你就可以通过类似 `https://<用户名>.github.io/Blog-With-GitHub-Boilerplate` 这样的链接访问你的网站了。

## 第二步：为仓库添加一个 token

为了让 GitHub Actions 可以自动更新你的网站，需要添加一个 Token。点击[这个网址](https://github.com/settings/tokens)，点击右上角的 Generate new token，起个名字并勾选 repo 复选框：

![](https://github.com/AlanDecode/Blog-With-GitHub-Boilerplate/raw/source/assets/image-20191218154358592.png)

点击页脚的 Generate Token，新的 token 会显示出来，把它复制下来，保存好。关了这个页面你就永远也看不到它了。

![](https://github.com/AlanDecode/Blog-With-GitHub-Boilerplate/raw/source/assets/image-20191218154525529.png)

回到仓库中，进入 Setting，坐标找到 Secrets 选项卡，新建一个名叫 PERSONAL_TOKEN 的 secret：

![](https://github.com/AlanDecode/Blog-With-GitHub-Boilerplate/raw/source/assets/image-20191218154724925.png)

**💡 从这里开始我们会对仓库的文件做一些修改，如果你电脑上有安装 Git，可以把仓库 clone 到本地，完成修改后提交并 push 回去；如果没有安装，可以直接在浏览器中编辑文件。**

## 第三步：尝试修改一下网站设置

>新 fork 的仓库可能需要手动打开 Actions。点击仓库顶部的 Actions 按钮：
>
>![](https://github.com/AlanDecode/Blog-With-GitHub-Boilerplate/raw/source/assets/image-20191219104540016.png)
>
>如果出现了以下提示，点击 "I understand my workflows, go ahead and run them".
>
>![](https://github.com/AlanDecode/Blog-With-GitHub-Boilerplate/raw/source/assets/enable-action.png)

回到仓库首页，点击 conf.py 文件，然后点击编辑按钮：

![](https://github.com/AlanDecode/Blog-With-GitHub-Boilerplate/raw/source/assets/image-20191218155128999.png)

1. 为你的网站起个名字，填写到 `site_name` 这里
2. 修改 `author`，`email`，`description` 等选项为你的内容
3. 其它选项也可以随意修改（暂时不要修改 `site_prefix` 选项）

点击页脚的 Commit changes，稍等片刻再访问 `https://<用户名>.github.io/Blog-With-GitHub-Boilerplate` 看是不是已经更新了。如果没有，请点击仓库标题下方的 Actions 按钮，在里面查看自动构建状态。

### 第四步：尝试发布新的内容

点击进入仓库的 src 文件夹，并点击 Create new file

![](https://github.com/AlanDecode/Blog-With-GitHub-Boilerplate/raw/source/assets/image-20191218155835654.png)

填写文件名以及内容。文件名可以起 `我的第一篇文章.md`，内容可以参考这样的：

```
---
layout: post
title: 我的第一篇文章
slug: my-first-awesome-post
date: 2019-12-17 20:34
status: publish
author: <填写你的名字>
categories: 
  - 默认分类
tags: 
  - 博客
  - GitHub
excerpt: Hello World!
---

这是我的第一篇文章。文章使用 GitHub 管理，并通过 GitHub Actions 自动构建与发布！
```

点击页脚的 Commit new file，稍等片刻再访问 `https://<用户名>.github.io/Blog-With-GitHub-Boilerplate`，可见新文章已经发布了！

## 第五步：使用 jsDelivr 作为博客的 CDN 服务

回到仓库首页，点击 conf.py 文件，然后点击编辑按钮。修改 `enable_jsdelivr` 如下：

```
enable_jsdelivr = {
    "enabled": True,
    "repo": "<你的用户名>/Blog-With-GitHub-Boilerplate@gh-pages"
}
```

点击 Commit changes。然后修改你刚才添加的文章，在里面插入一张仓库中的图片：

```
这是我的第一篇文章。文章使用 GitHub 管理，并通过 GitHub Actions 自动构建与发布！

![幽灵公主剧照](./images/Mononoke_Hime.jpg)
```

发布后稍等片刻再访问你的网站，此时网站的图片都通过 jsDelivr 传输的。不信的话在图片上右键选择「在新标签页中打开图片」，看链接是否以 `cdn.jsdelivr.net` 开头。

要插入你自己的图片，请把图片上传到 `src/images` 文件夹里，然后在文章中使用 Markdown 语法引用即可。

## 第六步：进行更多的自定义与创作

经过以上的步骤你已经学会了自定义网站、添加文章与修改文章。接下来就该你自由发挥了。仓库中 conf.py 里面的内容都可以自定义修改，特别要注意格式，比如引号要使用英文引号之类的。针对网站的设置项请参考 [Maverick/README.md](https://github.com/AlanDecode/Maverick/blob/master/README.md)。

仓库自带的 about.md 与 Typography 都可改可删，全看你。

仓库`src/static` 文件夹中有一个 logo.png，这是示例 logo。你可以在这个文件夹中上传新的 logo 图片，最好是方形的图片，然后在 conf.py 中修改 `site_logo` 为 `"${static_prefix}新的logo.png"` 即可。

现在可以把仓库名称改成你想要的名字了。改了之后，记得将 conf.py 中的 `site_prefix` 设置为 `"/<新的仓库名>/"`，并且对应修改 `enable_jsdelivr ` 选项的内容。

如果要将仓库名修改为 `<用户名>.github.io` 的形式，请看 [About-User-Pages](https://github.com/AlanDecode/Blog-With-GitHub-Boilerplate/blob/source/About-User-Pages.md)。

## 第七步：在本地进行创作

你可以把仓库 clone 到电脑上，修改后再将修改 push 回去。如果你的电脑上有安装 `make`，则这个过程可以方便一些：

升级 Maverick：

```bash
make mvrk
```

升级主题：

```bash
make theme
```

修改站点：

```bash
make msg="Add some change" site
```

> **关于如何在电脑上使用 Git**
>
> 如果你之前没有使用过 GitHub，那么需要进行一定的设置。如果你的电脑是 macOS 或者 Linux，git 可能是默认安装在电脑上的；如果是 Windows，则需要到[这里](https://git-scm.com/downloads)下载合适的 Git 安装到电脑上。记得安装时选中将  git 添加到 PATH。
>
> 文件管理器中右键，点击 Git Bash Here，在弹出的窗口中输入：
>
> ```
> git config --global user.name "你的GitHub用户名"
> git config --global user.email "你的GitHub邮箱"
> git config --global credential.helper store
> ```
>
> 之后到仓库右上角的 Clone or download 那里，复制仓库链接（建议使用 HTTPS）：
>
> ![](https://github.com/AlanDecode/Blog-With-GitHub-Boilerplate/raw/source/assets/image-20191218201359204.png)
>
> 在命令行中输入：
>
> ```
> git clone <仓库链接>
> ```
>
> 若需要输入用户名密码则输入就行。这样仓库就克隆到了本地。在仓库中进行修改后，这样提交文件：
>
> ```
> # cd 到仓库文件夹后
> 
> git add .
> git commit -m "添加修改"
> git push
> ```
>
> 这样本地的修改就推送到了 GitHub。

## 第八步：绑定自定义域名

如果你有自己的域名，请在域名解析商那里将域名 CNAME 设置为 `<用户名>.github.io`，然后回到仓库，在 `src/static` 文件夹中添加一个名叫 CNAME 的文件，内容填写你自己的域名。然后在 conf.py 中修改 `site_prefix` 为 `"/"`。稍等片刻，你的网站就能通过你的域名访问了。

---

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

