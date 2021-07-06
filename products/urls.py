from django.urls import path
from . import views

urlpatterns = [
    path('', views.studio_products, name='products')
]