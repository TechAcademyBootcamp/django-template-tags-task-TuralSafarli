from django.shortcuts import render
import requests

# Create your views here.

def newslist(request):
    news_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=dd5f84390b6e4218bf66116db5b25578'

    r = requests.get(news_url)

    Nlist = r.json()['articles']
    
    context = {
        'newslist': Nlist[:5]
    }
    return render(request,'news_list.html',context)