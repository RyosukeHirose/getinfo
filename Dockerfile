FROM python:3.7

# 作業ディレクトリを設定  
WORKDIR /usr/src/app  

ADD requirements.txt /usr/src/app  

# Pipenvをインストール  
RUN apt-get update \
&& pip install --upgrade pip \
&& pip install -r requirements.txt \
&& pip install django-debug-toolbar \
&& pip install djangorestframework \
&& apt-get install -y python-dev default-libmysqlclient-dev \
&& apt-get install -y python3-dev \
&& pip install mysqlclient



# CMD [""]

# コンテナ内で
# django-admin startproject getinfo .
# python manage.py startapp scraping
# settingにアプリ名と'rest_framework'を追加
# python manage.py makemigrations  
# python manage.py migrate  
# python manage.py runserver 0:8000  で起動
