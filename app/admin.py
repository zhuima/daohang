# coding: utf8

from django.contrib import admin
from .models import UrlGroup, UrlInfor
from django.utils.html import format_html

# Register your models here.


class UrlGroupModelAdmin(admin.ModelAdmin):
    # 显示在管理页面的字段
    list_display = ("group_name", "gid", "timestamp")
    # 可以修改内容的链接
    list_display_links = ("gid",)
    # 可以查询的字段，显示搜索框
    search_fields = ("group_name",)
    # 可直接编辑的字段（但是不能同时可连接可编发来）
    list_editable = ("group_name",)
    # 定制过滤器
    list_filter = ("group_name",)

    list_per_page = 10

    class Meta:
        model = UrlGroup



class UrlInforModelAdmin(admin.ModelAdmin):

    # 显示在管理页面的字段
    list_display = (
        "url_name",
        "url_path",
        "url_desc",
        "url_group",
        "url_status",
        "timestamp",
    )
    # 可以修改内容的链接
    list_display_links = ("url_desc",)
    # 可以查询的字段，显示搜索框
    search_fields = ("url_name",)
    # 可直接编辑的字段（但是不能同时可连接可编发来）
    list_editable = ("url_status",)
    # 定制过滤器
    list_filter = ("url_name",)

    list_per_page = 10

    class Meta:
        model = UrlInfor

 

admin.site.register(UrlGroup, UrlGroupModelAdmin)
admin.site.register(UrlInfor, UrlInforModelAdmin)
