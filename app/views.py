# coding: utf8
# Create your views here.

import datetime
import json

from django.contrib import messages

# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from app.forms import CommitForm
from app.models import UrlGroup, UrlInfor


def index(request):
    """
    前端展示文件入口
    """
    today = datetime.date.today()
    weekday = get_week_day(datetime.datetime.now())
    return render(request, "index.html", {"today": today, "weekday": weekday})


def get_week_day(date):
    """
    获取当天是星期几，用来实现页面展示
    """
    week_day_dict = {
        0: "星期一",
        1: "星期二",
        2: "星期三",
        3: "星期四",
        4: "星期五",
        5: "星期六",
        6: "星期天",
    }
    day = date.weekday()
    return week_day_dict[day]


def serialization_data(request):
    """
    构造数据格式
        list
            dict
                list
                    dict

    从组里取出所有组，然后再根据一对多的关系，通过组获取url的具体信息，属于反向获取数据
    http://830909.blog.51cto.com/8311014/1765596
    http://www.cnpythoner.com/post/135.html
    [{"gid": "production", "list": [{"desc": "\u7ebf\u4e0aelk\u65e5\u5fd7\u68c0\u7d22\u7cfb\u7edf", "href": "http://192.168.0.210", "title": "\u7ebf\u4e0aelk\u7cfb\u7edf"}, {"desc": "\u7ebf\u4e0a\u90ae\u7bb1\u5730\u5740\uff0c\u516c\u53f8\u5185\u90e8\u90ae\u7bb1\u767b\u9646\u94fe\u63a5", "href": "http://192.168.0.215", "title": "\u90ae\u7bb1\u5730\u5740"}], "title": "\u751f\u4ea7\u73af\u5883"}, {"gid": "staging", "list": [{"desc": "zabbix\u76d1\u63a7\u7cfb\u7edf\uff0c\u53ef\u4ee5\u7cfb\u7edf\u7cfb\u7edf\u548c\u5e94\u7528\u5c42\u7684\u76d1\u63a7\u4fe1\u606f", "href": "http://192.168.0.211", "title": "\u7ebf\u4e0azabbix\u7cfb\u7edf"}], "title": "\u9884\u53d1\u73af\u5883"}, {"gid": "testing", "list": [{"desc": "\u8fd0\u7ef4\u5185\u90e8nginx\u7ba1\u7406\u5e73\u53f0", "href": "http://192.168.0.215", "title": "\u7ebf\u4e0anginx\u7ba1\u7406\u5e73\u53f0"}, {"desc": "sdf", "href": "http://192.168.0.212", "title": "\u7ebf\u4e0arundeck"}], "title": "\u6d4b\u8bd5\u73af\u5883"}, {"gid": "loading", "list": [{"desc": "\u538b\u6d4b\u73af\u5883\u4ee3\u7801\u53d1\u5e03\u4e4bjenkins\u4e13\u7528", "href": "http://192.168.0.212", "title": "jenkins"}], "title": "\u538b\u6d4b\u73af\u5883"}, {"gid": "QA", "list": [{"desc": "qa\u4e13\u7528SmokeTest\u9875\u9762", "href": "http://192.168.0.215", "title": "smoketest"}], "title": "QA\u4e13\u573a"}, {"gid": "new_work", "list": [{"desc": "\u4e2a\u4eba\u5f00\u53d1\u673a\u5668\u7533\u8bf7\uff0c\u7528\u4e8e\u4e2a\u4eba\u5199\u4ee3\u7801\u7528\u9014", "href": "http://192.168.0.214", "title": "\u4e2a\u4eba\u5f00\u53d1\u673a\u7533\u8bf7"}, {"desc": "\u7528\u4e8e\u767b\u9646\u7ebf\u4e0b\u3001\u7ebf\u4e0a\u5821\u5792\u673a", "href": "http://192.168.0.215", "title": "\u5821\u5792\u673a\u8d26\u53f7\u7533\u8bf7"}], "title": "\u65b0\u5458\u5de5\u4e0a\u624b"}]
    """

    _group_lists = UrlGroup.objects.all().order_by("timestamp")
    _datas = []
    for group in _group_lists.all():
        if group.group_set.count() > 0:
            _group_template = {
                "title": u"{0}".format(group.group_name),
                "gid": u"{0}".format(group.gid),
                "list": [],
            }
            _group = UrlGroup.objects.get(gid=group.gid)
            for k in _group.group_set.all():
                if k.url_status:
                    _url_template = {
                        "title": u"{0}".format(k.url_name),
                        "href": "{0}".format(k.url_path),
                        "desc": u"{0}".format(k.url_desc),
                    }
                    _group_template["list"].extend([_url_template])
            _datas.extend([_group_template])
    result = json.dumps(_datas)
    return HttpResponse(result)


def commit(request):
    today = datetime.date.today()
    weekday = get_week_day(datetime.datetime.now())
    if request.method == "POST":
        form = CommitForm(request.POST)
        if form.is_valid():
            urlinfor = form.save(commit=False)
            urlinfor.save()
            print(urlinfor)
            messages.success(request, "提交成功! 审核期1个工作日。")
            return HttpResponseRedirect(reverse("commit"))
    else:
        form = CommitForm()
    return render(
        request, "commit.html", {"form": form, "today": today, "weekday": weekday}
    )
