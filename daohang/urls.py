"""daohang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views as app_views

admin.site.site_title = "daohang"
admin.site.site_header = "运维内部导航平台"


urlpatterns = [
    url(r"^signin/", admin.site.urls, name="login"),
    url(r"^$", app_views.index, name="index"),
    url(r"^datas/$", app_views.serialization_data, name="datas"),
    url(r"^commit/$", app_views.commit, name="commit")
    # url(r'^commit/$', app_views.CommitView.as_view(), name='commit')
]
