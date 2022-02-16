from unicodedata import name
from django import views
from django.urls import path
from . import views

# -----------------------------


urlpatterns = [
    path('', views.main, name='index'),
    path('cart/', views.cart, name='cart'),
    path('update_item/', views.updateItem, name="update_item"),
]
