# 使用官方Python镜像作为基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /usr/src/app

# 把当前目录下的所有文件（除了.dockerignore排除的路径），都拷贝进入容器内的/usr/src/app目录
ADD . /usr/src/app

# 使用pip安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 指定容器启动程序及参数，这里我们使用gunicorn作为Django的WSGI HTTP Server
CMD ["gunicorn", "myproject.wsgi:application", "-w 2", "-b :8000"]
