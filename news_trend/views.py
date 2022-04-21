import requests,json
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from newsdataapi import NewsDataApiClient


# Create your views here.
# def home(request):
#     try:
#         api_key   = 'pub_66264246cb6e2e62d30563de8e7d62e183ec'
#         news_obj  = requests.get(f'https://newsdata.io/api/1/news?apikey={api_key}&country=in&category=business,sports,health,food,top')
#         news_data = json.loads(news_obj.content)
#     except Exception as e:
#         print(e)
#         news_data = []
#     return render(request, 'home/home.html',{'news_data': news_data['results']})


def home(request):
    try:
        api_key   = 'baa7bb6a65144a35867128e1eb31dac0'
        news_obj  = requests.get(f'https://newsapi.org/v2/everything?apiKey={api_key}&q=bitcoin')
        news_data = json.loads(news_obj.content)
        page      = request.GET.get('page', 1)
        paginator = Paginator(news_data['articles'], 6)
        try:
            news_data = paginator.page(page)
        except PageNotAnInteger:
            news_data = paginator.page(1)
        except EmptyPage:
            news_data = paginator.page(paginator.num_pages)
    except Exception as e:
        print(e)
        news_data = []
    return render(request, 'home/home.html',{'news_data': news_data})