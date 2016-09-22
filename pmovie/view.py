# -*- coding: utf-8 -*-

from django.http import HttpResponse, JsonResponse
from django import template

""" 首頁 """
def index(request):
    return HttpResponse('這是首頁')

""" 使用者首頁 """
def usersite(request):
    return HttpResponse('這是首頁')

""" 管理者首頁 """
def adminsite(request):
    return HttpResponse('這是首頁')
