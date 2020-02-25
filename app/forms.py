# coding: utf8

from django import forms
from django.conf import settings

from app.models import UrlInfor
from django.utils.http import is_safe_url


class CommitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommitForm, self).__init__(*args, **kwargs)
        self.fields["url_name"].help_text = "链接名称，例如：wiki."
        self.fields["url_path"].help_text = "链接，例如：https://zh.wikipedia.org/zh/Wiki."
        self.fields["url_desc"].help_text = "链接描述:，例如：这是wiki链接，你可以通过这个链接了解相关技术。"

    class Meta:
        model = UrlInfor
        fields = ["url_name", "url_path", "url_group", "url_desc"]

    def clean_url_name(self):
        url_name = self.cleaned_data.get("url_name")
        exists = UrlInfor.objects.filter(url_name=url_name).exists()
        if exists:
            raise forms.ValidationError(message="%s 已经存在了" % url_name)
        else:
            return url_name

    def clean_url_path(self):
        url_path = self.cleaned_data.get("url_path")
        exists = is_safe_url(url=url_path, allowed_hosts=settings.ALLOWED_HOSTS)
        if exists:
            raise forms.ValidationError(message="%s url不合法" % url_path)
        else:
            return url_path
