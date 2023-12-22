# 使用官方 Python 镜像作为基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /code

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 安装依赖
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 复制项目文件到工作目录
COPY . /code/
