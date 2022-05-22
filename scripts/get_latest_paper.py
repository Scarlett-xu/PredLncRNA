import requests
import csv
import time
import re
import pymysql


def get_data():
    pid = []  # paper id
    journal = []  # 期刊名
    year = []  # 年份
    title = []  # titles
    imghrefs = []  # 图片地址
    url = 'https://pubmed.ncbi.nlm.nih.gov/?term=lncRNA%20predict'
    for i in range(3):
        print("抓取第"+str(i+1)+"页")
        if i != 0:
            url = url+'&page='+str(i)
        # 获取title
        reg_title = re.compile('data-article-id="\d{8}">\s*(.*?)\s*</a>')
        title += reg_title.findall(strhtml.text)

        # 获取期刊名和年份
        reg_journal = re.compile('short-journal-citation">(.*?)</span>')
        journalyear = reg_journal.findall(strhtml.text)
        for i in journalyear:
            journal.append(i.split('.')[0])
            year.append(i.split('.')[1])

        # 获取id
        reg_id = re.compile(
            '<meta name="log_displayeduids" content="(.*?)" />')
        idlist = reg_id.findall(strhtml.text)[0]
        pid += idlist.split(',')

        # 获取图片地址
        for i in idlist.split(','):
            urli = 'https://pubmed.ncbi.nlm.nih.gov/' + i
            links.append(urli)
            detailhtml = requests.get(urli)
            imglink = re.compile('<a class="figure-link"\s*href="(.*?)"')
            imghref = imglink.findall(detailhtml.text)
            imghrefs.append(imghref)

    return pid, title, journal, year, imghrefs


# 筛选出有图片的论文
def filter_papers(pid, title, journal, year, imghrefs, n):
    newidx = []
    for i in range(n*10):
        if len(imghrefs[i]) != 0:
            newidx.append(i)
    pid = [pid[i] for i in newidx]
    journal = [journal[i] for i in newidx]
    year = [year[i] for i in newidx]
    title = [title[i] for i in newidx]
    imghrefs = [imghrefs[i][0] for i in newidx]
    return pid, title, journal, year, imghrefs


pid, title, journal, year, imghrefs = get_data()
pid, title, journal, year, imghrefs = filter_papers(
    pid, title, journal, year, imghrefs, 3)
db = pymysql.connect(host='139.196.159.204',
                     port=3306,
                     user='root',
                     password='mysql',
                     database='predlncRNA',
                     use_unicode=True)
cs1 = db.cursor()
for i in range(len(pid)):
    #     print(type(imghrefs[i]))
    query = "insert into web_latestpaper(pid,title,paperurl,journal_name,year,imgsrc) values( '%s','%s','%s','%s','%s','%s' )" % (
        pid[i], title[i], 'link', journal[i], year[i], imghrefs[i])
    print(query)
    cs1.execute(query)
db.commit()
db.close()
