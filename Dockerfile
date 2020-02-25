# 基础镜像
FROM python:3.5

# 维护者信息
MAINTAINER zhuima <zhuima314@gmail.com>

# app 所在目录
WORKDIR /usr/local/web
ADD . /usr/local/web/

# 安装 app 所需依赖
RUN cd /usr/local/web/ && python -m pip install --no-cache-dir -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

EXPOSE 8080
CMD python manage.py runserver  0.0.0.0:8080
