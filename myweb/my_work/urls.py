from django.conf.urls import url,include
from my_work import views
from django.contrib import admin

urlpatterns = [
    url(r'start', views.my_work_home),
]
