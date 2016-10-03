# PythonTools
该项目为本人用python写的小工具，易于日常操作，由于是自用，所以与本人本地环境设置可能有很大关系，如果你也有这方面的需求，请仔细阅读源文件之后再使用，谢谢！

本人大致环境:
- win10企业版
- python 3.5.2

下面是工具的具体介绍：

- [GPRS_of_blog_pictures](#GPRS_of_blog_pictures.py)
- [update_all_py_packages](#update_all_py_packages.py)

## GPRS_of_blog_pictures.py
由于本人的blog使用github + Hexo,为了节省github的空间,所以将图片放在[https://i.imgur.com](https://i.imgur.com),该网站可以上传任意容量，任意大小的图片文件，更主要的原因是我的blog使用的是`MarkDownPad2`编辑的，该软件默认上传图片也是这个地方，而这个网站规定，如果图片在6个月没有访问流量，则会删除图片，对于学生党而言，暂没有能力负担起图片主机或空间的价格，只能写个脚本定时执行跑下流量，防止blog中的图片被意外删除

## update_all_py_packages.py
对于强迫症而言，保持软件甚至包的最新状态是一种日常，然而`pip`并没有一键更新所以python第三方包的方法，免得升级某些包后某些功能不兼容，这也是为什么很多生产环境下的东西都很老，都是为了避免不必要的麻烦，但是，不更新可能意味着安全隐患，所以更新到最新还是有必要的，所以就写了个脚本一键更新python第三方包
