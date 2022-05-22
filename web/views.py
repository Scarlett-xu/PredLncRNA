from datetime import datetime, timedelta
from django.http import JsonResponse
from pyecharts import options as opts
from pyecharts.charts import Bar
import json
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from lncRNAwebtool.settings import BASE_DIR
import datetime
import os
import markdown
import uuid
from web.models import *
from django.core.paginator import Paginator
import json
# Create your views here.
# index是主页


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


def home(request):
    value = {}
    # 默认为正序排列
    reverse = request.GET.get('reverse', '0')
    value['reverse'] = reverse
    # 数据库里paper
    # 分页
    # papers = Paper.objects.all()
    # 一页八个

    if reverse == '0':
        papers = Paper.objects.all().order_by('-date')
        paginator = Paginator(papers, 9)
        # page是参数 第几页 默认为1
        num_p = request.GET.get('page', 1)
        page = paginator.page(int(num_p))
        value['page'] = page
    else:
        papers = Paper.objects.all().order_by('date')
        paginator = Paginator(papers, 9)
        # page是参数 第几页 默认为1
        num_p = request.GET.get('page', 1)
        page = paginator.page(int(num_p))
        value['page'] = page
        value['papers'] = papers
    # 词频tags
    tags = []
    filename = os.path.join(BASE_DIR, 'web', 'static', 'json', 'tags')
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    for line in lines:
        t = Tags()
        t.tag = line.rstrip().split(' ')[0]
        t.id = 'tag'+(line.rstrip().split(' ')[1])
        tags.append(t)
    value['tags'] = tags
    # latest_paper模块的paper
    latest_paper = latestPaper.objects.all()
    # 取出偶数个
    if len(latest_paper) % 2 != 0:
        latest_paper = latest_paper[:-1]
    latest_papers = []

    for i in range(0, len(latest_paper), 2):
        latest_papers.append(latest_paper[i:i+2])

    value['latest_papers'] = latest_papers
    d = datetime.datetime.now()
    today = '%d-%d-%d' % (d.year, d.month, d.day)
    value['update_time'] = today
    return render(request, 'multiends/home.html', value)
    # return render(request, "multiends/home.html")


def run(request):
    value = {}
    uids = request.COOKIES.get('uids', None)
    struids = ""
    if uids:
        for ut in uids.split(','):
            ut = ut + '\n'
            struids += ut
    else:
        struids = '\n'
    value['history_uid'] = struids

    return render(request, "multiends/run.html", value)


def about(request):
    single_article = ExampleModel.objects.get(name='about')
    html = markdown.markdown(single_article.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    return render(request, "multiends/about.html", {"html": html})


def details(request):
    return render(request, "multiends/details.html")


def help(request):
    # single_article = ExampleModel.objects.get(name='help')
    # html = markdown.markdown(single_article.content, extensions=[
    #     'markdown.extensions.extra',
    #     'markdown.extensions.codehilite',
    #     'markdown.extensions.toc',
    # ])

    value = {}
    # if request.method == 'POST':
    #     if 'bntcnci' in request.POST:
    #         c =

    return render(request, "multiends/help.html")


def background(request):
    # single_article = ExampleModel.objects.get(name='help')
    # single_article = ExampleModel.objects.all()
    # single_article.increase_visted()
    # single_article.content = markdown.markdown(single_article.content,
    #                                            extensions=[
    #                                                'markdown.extensions.extra',
    #                                                'markdown.extensions.codehilite',
    #                                                'markdown.extensions.toc',
    #                                            ])
    return render(request, "multiends/background.html")


# def mkdown(request):

#     return render(request, "multiends/mkdown.html")
def readmore(request):
    value = {}
    latest_paper = latestPaper.objects.all()
    value['latest_paper'] = latest_paper
    return render(request, "multiends/readmore.html", value)


# def chart(request):
#     return render(request, "multiends/chart.html")


def regist_url(request):
    data = json.loads(request.body)
    username = data["username"]
    password = data["password"]
    print("用户名："+username)
    print("密码："+password)
    return HttpResponse(request.body)


def upload(request):
    value = {}

    if request.method == 'POST':
        # predict按钮
        if 'btnpredict' in request.POST:
            uid = str(uuid.uuid1())
            val = request.POST.get("flexRadioDefault")
            path = os.path.join(BASE_DIR, "inputfiles")
            models = request.POST.get("select_models")
            spieces = request.POST.get("select_spieces")
            if val == "upload":
                # 上传文件
                data = request.FILES.get("inputfile")
                if not os.path.exists(path):
                    os.mkdir(path)
                with open(os.path.join(path, uid), "wb") as f:
                    f.write((models + '\n').encode())
                    # 如果不存在物种，就记录空格
                    try:
                        f.write((spieces+'\n').encode())
                    except:
                        f.write(('\n').encode())
                    for c in data.chunks():
                        f.write(c)
            elif val == "paste":
                text = request.POST.get('textarea_data')
                with open(os.path.join(path, uid), "wb") as f:
                    f.write((models + '\n').encode())
                    f.write((spieces+'\n').encode())
                    f.write(text.encode())

            else:
                return render(request, "multiends/run.html")
            value['uid'] = uid

            value['uploadmassage'] = "预测文件上传成功！"

            # 上传当前的uid
            uids = request.COOKIES.get('uids', None)
            struids = uid + '\n'
            if uids:
                for ut in uids.split(','):
                    ut = ut + '\n'
                    struids += ut
            else:
                struids = '\n'
            value['history_uid'] = struids
            # value = {'uid': uid, 'uploadmassage': "预测文件上传成功！"}
            script_path = os.path.join(BASE_DIR, "scripts")
            os.system("bash "+script_path+"/predict.sh " +
                      uid + " > predict.log")
            response = render(request, "multiends/run.html", context=value)

            # 保存历史uid
            uids = request.COOKIES.get('uids', None)
            if uids:
                list_uid = uids.split(',')
                list_uid.insert(0, uid)
                if len(list_uid) >= 5:
                    list_uid.pop()
                    print("pop the listuid")
                uids = ','.join(list_uid)
            else:
                uids = uid
            print(uids)
            response.set_cookie('uids', uids)
            return response
        # 下载按钮
        elif 'download' in request.POST:
            uids = request.COOKIES.get('uids', None)
            struids = ""
            if uids:
                for ut in uids.split(','):
                    ut = ut + '\n'
                    struids += ut
            else:
                struids = '\n'
            value['history_uid'] = struids
            # 显示内容
            val = request.POST.get("getid")

            base_respath = os.path.join(
                BASE_DIR, "predict_results", val)
            # 判断id是否存在
            if val != "" and val in os.listdir(os.path.join(
                    BASE_DIR, "predict_results")):
                filename = base_respath
                file = open(filename, 'rb')
                response = FileResponse(file)
                response['Content-Type'] = 'application/octet-stream'
                response['Content-Disposition'] = 'attachment;filename='+val
                return response
            else:
                # id不存在，返回不存在的信息。
                notexistfilename = os.path.join(base_respath, "notexist")
                file = open(notexistfilename, 'r')
                lines = file.readlines()
                text = "".join(lines)
                value['outputframe'] = text
                return render(request, "multiends/run.html", context=value)

        # 显示结果按钮：
        elif 'show_result' in request.POST:
            uids = request.COOKIES.get('uids', None)
            struids = ""
            if uids:
                for ut in uids.split(','):
                    ut = ut + '\n'
                    struids += ut
            else:
                struids = '\n'
            value['history_uid'] = struids

            val = request.POST.get("getid")
            base_respath = os.path.join(
                BASE_DIR, "predict_results", val)
            # 判断id是否存在
            if val != "" and val in os.listdir(os.path.join(
                    BASE_DIR, "predict_results")):
                filename = base_respath
                file = open(filename, 'r')
                lines = file.readlines()
                text = "".join(lines)
                value['outputframe'] = text
                value['taskid'] = val
                return render(request, "multiends/run.html", context=value)

            else:
                # id不存在，返回不存在的信息。
                notexistfilename = os.path.join(
                    BASE_DIR, "predict_results", "notexist")
                file = open(notexistfilename, 'r')
                lines = file.readlines()
                text = "".join(lines)
                value['outputframe'] = text
                # value = {'outputframe': text}
                return render(request, "multiends/run.html", context=value)

        elif 'show_log' in request.POST:
            uids = request.COOKIES.get('uids', None)
            struids = ""
            if uids:
                for ut in uids.split(','):
                    ut = ut + '\n'
                    struids += ut
            else:
                struids = '\n'
            value['history_uid'] = struids

            val = request.POST.get("getid")
            base_respath = os.path.join(
                BASE_DIR, "predict_log", val)
            # 判断id是否存在
            if val != "" and val in os.listdir(os.path.join(
                    BASE_DIR, "predict_log")):
                filename = base_respath
                file = open(filename, 'r')
                lines = file.readlines()
                text = "".join(lines)
                value['outputframe'] = text
                value['taskid'] = val
                return render(request, "multiends/run.html", context=value)

            else:
                # id不存在，返回不存在的信息。
                notexistfilename = os.path.join(
                    BASE_DIR, "predict_results", "notexist")
                file = open(notexistfilename, 'r')
                lines = file.readlines()
                text = "".join(lines)
                value['outputframe'] = text
                # value = {'outputframe': text}
                return render(request, "multiends/run.html", context=value)
        elif 'resetbtn' in request.POST:
            uids = request.COOKIES.get('uids', None)
            struids = ""
            if uids:
                for ut in uids.split(','):
                    ut = ut + '\n'
                    struids += ut
            else:
                struids = '\n'
            value['history_uid'] = struids
            return render(request, "multiends/run.html", value)
