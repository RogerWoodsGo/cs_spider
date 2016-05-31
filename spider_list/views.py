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
    info_dict = []
    for x in info_all: 
        info_dict.append(x.hash_title)
    return render(request, 'desc.html', {'info_dict': info_dict})
