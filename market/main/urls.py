from django.urls import path, include
from main import views
urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('items/', views.itemspage, name='items'),
    path('orders/', views.orderspage, name='orders'),
]