---
layout: post
title: ffmpeg常用教程
slug: ffmpeg
date: 2020-2-16 13:10
status: publish
author: Arley
categories: 
  - 技术
tags: 
  - ffmpeg
---

## 一、安装

**ffmpeg官网：[https://ffmpeg.zeranoe.com/builds/](https://ffmpeg.zeranoe.com/builds/)** 

该网站中的FFMPEG分为3个版本：Static，Shared，Dev。
前两个版本可以直接在命令行中使用，他们的区别在于<br>
Static里面只有3个应用程序：

* ffmpeg.exe
* ffplay.exe
* ffprobe.exe

Shared里面除了3个应用程序：ffmpeg.exe，ffplay.exe，ffprobe.exe之外，还有一些Dll，比如说avcodec-54.dll之类的。
Shared里面的exe体积很小，他们在运行的时候，到相应的Dll中调用功能。

Dev版本是用于开发的，里面包含了库文件xxx.lib以及头文件xxx.h，这个版本不包含exe文件。

这里我们使用static版本，下载zip压缩文件，解压到指定目录，利用Windows自带命令提示符CMD，CD到解压的路径，

例如：D:\ffmpeg201200216\bin，这样bin下面的ffmpeg.exe就可以在命令行中使用了，可以用ffmpeg -version测试一下：

放一个mp4视频，然后把声音提取到output.acc，用命令测试一下：

    ffmpeg -i movie.mp4 -acodec copy -vn output.aac

## 二、常用命令
主要参数：

* -i 设定输入流 
* -f 设定输出格式 
* -ss 开始时间 

视频参数：

* -b 设定视频流量(码率)，默认为200Kbit/s 
* -r 设定帧速率，默认为25 
* -s 设定画面的宽与高 
* -aspect 设定画面的比例 
* -vn 不处理视频 
* -vcodec 设定视频编解码器，未设定时则使用与输入流相同的编解码器
 
音频参数：

* -ar 设定采样率 
* -ac 设定声音的Channel数 
* -acodec 设定声音编解码器，未设定时则使用与输入流相同的编解码器 
* -an 不处理音频

### 1. 视频格式转换

比如一个avi文件，想转为mp4。

    ffmpeg -i input.avi output.mp4

### 2. 提取音频
比如一个相声.MP4文件,只想听声音，提取音频为.ACC格式：

    ffmpeg -i 相声.mp4 -acodec aac -vn output.aac

(-vn 不处理视频 )

### 3. 提取视频
比如一个相声.MP4文件,只想看视频影像不听声音：

    ffmpeg -i 相声.mp4 -vcodec copy -an output.mp4

（-an 不处理音频）

### 4. 视频剪切
截取视频从时间为00:00:15开始，截取5秒钟的视频：

    ffmpeg -ss 00:00:15 -t 00:00:05 -i input.mp4 -vcodec copy -acodec copy output.mp4

-ss表示开始切割的时间，-t表示要切多少。

> ffmpeg 在切割视频的时候无法做到时间绝对准确，因为视频编码中关键帧（I帧）和跟随它的B帧、P帧是无法分割开的，否则就需要进行重新帧内编码，会让视频体积增大。所以，如果切割的位置刚好在两个关键帧中间，那么 ffmpeg 会向前/向后切割，所以最后切割出的 chunk 长度总是会大于等于应有的长度。

### 5.码率控制
**码率： bitrate = file size / duration**

比如一个文件20.8M，时长1分钟，那么，码率就是：

biterate = 20.8M bit/60s = 20.8*1024*1024*8 bit/60s= 2831Kbps

ffmpg控制码率有3种选择:

* -minrate
* -b:v
* -maxrate

-b:v 主要是控制平均码率。 比如一个视频源的码率太高了，有10Mbps，文件太大，想把文件弄小一点，但是又不破坏分辨率:

    ffmpeg -i input.mp4 -b:v 2000k -bufsize 2000k output.mp4

-minrate -maxrate 设置码率波动阈值

    ffmpeg -i input.mp4 -b:v 2000k -bufsize 2000k -maxrate 2500k output.mp4

### 6. 视频编码格式转换
相声.mp4的编码是MPEG4，转换H264编码：

    ffmpeg -i input.mp4 -vcodec h264 output.mp4

相反

    ffmpeg -i input.mp4 -vcodec mpeg4 output.mp4

### 7.为视频添加logo
水印logo.png贴到一个视频上，那可以用如下命令：


    ffmpeg -i input.mp4 -i logo.png -filter_complex overlay output.mp4


### 8. 旋转视频
在手机上录的视频，在电脑放，是颠倒的，需要旋转90度。

    ffmpeg -i 相声.mp4 -vf transpose=1 rotate8.mp4

## 三、其他命令
官方文档：[https://www.ffmpeg.org/ffmpeg.html](https://www.ffmpeg.org/ffmpeg.html "ffmpeg官方文档")
