from django.conf.urls import url
from . import views
# . : 현재 폴더

urlpatterns = [
    url(r'^$', views.index),
]
# ^$: 빈경로