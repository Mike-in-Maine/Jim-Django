from django.shortcuts import render, HttpResponse
from main.models import Item
import pandas as pd

# Create your views here.
def homepage(request):
    return render(request, template_name='main/home.html')

def itemspage(request):
    items = Item.objects.all()
    #items = [{'name':'Phone','price':'500'}, {'name':'Laptop','price':'1000'}]
    #dfs = pd.DataFrame(items)
    #print(dfs)
    return render(request, template_name='main/items.html', context={'items': items})