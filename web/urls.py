from django.urls import path, include
from web.views import home, run, details, about, help, regist_url, upload, background, readmore


urlpatterns = [
    path("", home, name="home"),
    # path("home/", home, name="home"),
    path("run/", run, name="run"),
    path("details/", details, name="details"),
    path("help/", help, name="help"),
    path("about/", about, name="about"),
    path('upload/', upload, name='upload'),
    path('background/', background, name='background'),
    path('readmore/', readmore, name='readmore'),
    # path('chart/', chart, name='chart'),
    # path('selectool/', selectool, name='selectool'),
    # path('mkdown/', mkdown, name='mkdown'),
    # path("mdeditor/", include('mdeditor.urls'))
    # path('paper_list/', paper_list, name='paper_list'),
    # path('downloadf/', downloadf, name='downloadf'),
    # path('regist_url/', regist_url),
]
