#coding=UTF-8
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #允许使用_或者-来分隔内容
    path('<slug:blog_title>', views.blog_detail, name="blog_detail"),
    path('<int:a>/<int:b>', views.add, name="add"),

]