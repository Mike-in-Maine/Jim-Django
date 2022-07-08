from django.shortcuts import render, HttpResponse
from main.models import Item, Orders
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

def orderspage(request):
    orders = Orders.objects.all()
    return render(request, template_name='main/book_orders.html',context={'orders': orders})