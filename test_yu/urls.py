#-*-coding: utf-8
"""test_yu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# urlpatterns: 서버로 요청이 들어오면 누가 어떻게 처리할지 담당자를 지정

from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('elections.urls')),
    url(r'^admin/', admin.site.urls),
]

# url(주소, 누가 처리할지)
# include: 앱에 대해서 접속을 처리할때 반드시 적어줘야하는 문법, import 해줘야 함.