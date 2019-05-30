# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("欢迎光临我的博客!!")

def blog_detail(request, blog_title):
    return HttpResponse(f"标题是{blog_title}")

def add(request, a, b):
    return HttpResponse(f"{a}+{b}={a+b}")