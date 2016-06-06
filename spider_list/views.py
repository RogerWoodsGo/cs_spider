#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from spider_list.models import Kr36
from spider_list.models import Cyb 
import json

# Create your views here.
#def index(request):
#    return render(request, 'index.html')

objectsMap = {"36kr":Kr36, "cyb":Cyb}
itemMap = {"bigdata":[u"大数据"], "cloud_compute":[u"云计算"], "smart_hardware":[u"智能硬件"], "medical":[u"医疗", u"互联网医疗"], "region_link":[u"区块链"], "insurance":[u"保险", u"互联网保险"], "inter_transport":[u"物流", u"跨境物流"], "investment":[u"投资", u"融资", u"注册资本", u"出资"]}
def index(request):
    #info_all = list(info_all_1) 
    info_all = []
    print type(info_all)
    #print type(info), "****"
    for k, v in objectsMap.items():
         info_all.extend(list(v.objects.all()))
    msg_list = []
    for x in info_all:
        item = {}
        item['hash_title'] =  x.hash_title
        item['create_time'] = x.created_at
        item['description_text'] = x.description_text
        item['news_url'] = x.news_url
        msg_list.append(item)
    return render(request, 'index.html', {'msg_list': msg_list})


def get_item(request):
    website = request.GET['website']
    item_list = request.GET['item'].split(',')
    msg_list = []
    info_all = []
    try:
        if website == "all":
            for k, v in objectsMap.items():
                info_all.extend(list(v.objects.all()))
                #info_all.append(x.objects.all())
        else:
            info_all = objectsMap[website].objects.all() 
    except:
        print "except happen"
        return HttpResponse(json.dumps(msg_list), content_type='application/json') 
    for x in info_all:
        sql_item = {}
        desc = x.description_text
        all_in = 1
        if item_list[0] == u"":
            all_in = 1
        else:
            for req_item in item_list:  
                item_in = 0
                for item in itemMap[req_item]:
                    if (item in desc) or (item in x.hash_title):
                        item_in = 1
                        break
                if item_in == 0:
                    all_in = 0
                    break
        if all_in:
            sql_item['description_text'] = x.description_text
            sql_item['hash_title'] = x.hash_title
            sql_item['create_time'] = str(x.created_at)
            sql_item['news_url'] = x.news_url
            #print x.news_url
            msg_list.append(sql_item)
    return HttpResponse(json.dumps(msg_list), content_type='application/json') 
    #return HttpResponse(resp) 
