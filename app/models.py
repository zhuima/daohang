# coding: utf8

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UrlGroup(models.Model):
    """
    定义导航项目的组
    """
    group_name = models.CharField(u'分类名称', max_length=100, unique=True)
    gid = models.CharField(u'标签名称', max_length=100)
    timestamp = models.DateTimeField(u'创建时间')

    class Meta:
        verbose_name = u'导航分组'
        verbose_name_plural = u'导航分组'

    def __unicode__(self):
        return self.group_name


class UrlInfor(models.Model):
    """
    定义导航项目的具体信息
    """
    url_name = models.CharField(u'链接名称', max_length=100)
    url_path = models.CharField(u'链接', max_length=200)
    url_desc = models.TextField(u'链接描述', max_length=200)
    url_group = models.ForeignKey(UrlGroup, verbose_name=u'分类名称', related_name='group_set')
    timestamp = models.DateTimeField(u'创建时间')


    class Meta:
        verbose_name = u'导航详情'
        verbose_name_plural = u'导航详情'
        ordering = ['url_name']


    def __unicode__(self):
        return self.url_name
