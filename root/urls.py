from django.urls import path
from .views import *

app_name = 'root'

urlpatterns = [
    path('',home,name='home'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('pricing',pricing,name='pricing'),
    path('request',request,name='request'),
    path('search/',home,name='home_search'),
]
