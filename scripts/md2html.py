# -*- coding: utf-8

import markdown
import os
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


def md2html(mdstr):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite',
            'markdown.extensions.tables', 'markdown.extensions.toc']

    html = '''
    <html lang="zh-cn">
    <head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type" />
    <link href="default.css" rel="stylesheet">
    <link href="github.css" rel="stylesheet">
    </head>
    <body>
    %s
    </body>
    </html>
    '''

    ret = markdown.markdown(mdstr, extensions=exts)
    return html % ret


if __name__ == '__main__':

    # if len(sys.argv) < 3:
    #     print('usage: md2html source_filename target_file')
    #     sys.exit()

    # infile = open(sys.argv[1], 'r')
    # md = infile.read()
    # infile.close()

    # if os.path.exists(sys.argv[2]):
    #     os.remove(sys.argv[2])

    # outfile = open(sys.argv[2], 'a')
    md = '## 1. 关于网站 - 本网站是lcnRNA预测网站，主要介绍lncRNA预测工具以及提供预测平台 - 网站主要是用django + mysql + nginx 搭建，使用容器化部署方式在阿里云服务器上搭建。 - 如有问题，可使用邮箱联系本网站开发人员：xinranxu@hzau.edu.cn ## 2. 功能介绍 - 网站的预测依赖于高算力服务器，提供快速的预测和结果的比对； - 网站提供数据库、模型和特征的分析介绍，以及该领域相关信息的提供； - 网站提供该领域最新论文，每周根据pubmed自动更新相关最新论文。 ## 3. 网站支持 - 网站基于Django框架，通过Docker容器化部署方式在阿里云服务器上搭建； - 前端使用Boostrap4 + jQuery支持响应式， - 前后端分离，后端数据库使用Mysql - 使用crontab定时任务更新网站内容 - 使用nginx反向代理映射域名 - 使用阿里云OSS对象存储图片，多进程下载图片，提高图片的更新与加载效率 ## 4. 关于作者 博主为华中农业大学计算机科学与技术专业2018级学生。 该网站为综述论文：A systematic review of computational methods for predicting long noncoding RNAs的拓展应用。该论文总结了21种不同的lncRNA预测模型，基于机器学习、深度学习、集成学习模型，并提供对应数据库、特征、模型的介绍，并在统一环境下进行预测，对比模型的性能。'
    print(md2html(md))
    # outfile.close()

    # print('convert %s to %s success!' % (sys.argv[1], sys.argv[2]))
