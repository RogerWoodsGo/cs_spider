#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from spider_list.models import Kr36

# Create your views here.
def index(request):
    return render(request, 'index.html')

def desc(request):
    info_all = Kr36.objects.all()
    msg_list = []
    for x in info_all:
        item = {}
        item['hash_title'] =  x.hash_title
        item['create_time'] = x.created_at
        item['description_text'] = x.description_text
        msg_list.append(x.hash_title)
    return render(request, 'desc.html', {'msg_list': msg_list})
