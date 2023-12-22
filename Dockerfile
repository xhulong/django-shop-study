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

# 从 GitHub 下载 wait-for-it.sh 脚本并赋予执行权限
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /code/
RUN chmod +x /code/wait-for-it.sh

# 复制项目文件到工作目录
COPY . /code/

# 收集静态文件
RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

# 启动 Django 应用之前，先运行 wait-for-it.sh 脚本等待 MySQL 服务完全启动
CMD /code/wait-for-it.sh db:3306 -- python manage.py runserver 0.0.0.0:8000
