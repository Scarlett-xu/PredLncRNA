from pydoc import describe
from django.db import models
from mdeditor.fields import MDTextField
# Create your models here.

# Django规定，如果要使用模型，必须要创建一个app
# 与数据库操作相关，存入或读取数据时用到这个
# 建立person类


class Paper(models.Model):
    pid = models.CharField(max_length=10, default='pid')
    name = models.CharField(max_length=300, default='paper')
    link = models.CharField(max_length=300, default='link')
    describtion = models.CharField(max_length=300, default='describtion')
    publishdate = models.CharField(max_length=30, default='date')
    imgsrc = models.CharField(max_length=300, default='imgsrc')
    date = models.IntegerField(default='1')
    citations = models.IntegerField(default='0')

    # link = models.IntegerField()
# 自动生成一个主键
# 构建字段nanme和temperature

    # def __str__(self):
    #     # 定义函数读取字段数据
    #     # 在Python2中使用 def __unicode__(self)
    #     return self.name
# 这里新建了一个person类，继承了django的models.Model类


class Tags:
    def __init__(self):
        self.tag = ''
        self.id = ''


class Databases(models.Model):
    dbname = models.CharField(max_length=50, default='database')
    description = models.CharField(max_length=300, default='description')
    institute = models.CharField(max_length=200, default='institute')
    version = models.CharField(max_length=100, default='version')
    numoflncrna = models.CharField(max_length=50, default='numoflncrna')
    spieces = models.CharField(max_length=50, default='spieces')

# class latestPaper(models.Model):
#     paper_name = models.CharField(max_length=300, default='paper_name')
#     img_link = models.CharField(max_length=300, default='paper_name')


class ExampleModel(models.Model):
    name = models.CharField(max_length=10, default='name')
    content = MDTextField()


class latestPaper(models.Model):
    pid = models.CharField(max_length=15, default='paperid')
    title = models.CharField(max_length=200, default='title')
    paperurl = models.CharField(max_length=300, default='paper')
    journal_name = models.CharField(max_length=300, default='journal_name')
    year = models.CharField(max_length=10, default='year')
    imgsrc = models.CharField(max_length=300, default='imgsrc')

# class inputdata(models.Model):
#     tid = models.CharField(max_length=15, default='taskid')
#     title = models.CharField(max_length=200, default='title')
#     paperurl = models.CharField(max_length=300, default='paper')
#     journal_name = models.CharField(max_length=300, default='journal_name')
#     year = models.CharField(max_length=10, default='year')
#     imgsrc = models.CharField(max_length=300, default='imgsrc')
