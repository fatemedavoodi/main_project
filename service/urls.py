from django.urls import path
from .views import *

app_name = 'service'

urlpatterns = [
    path("",service,name='service'),
    path("service_detail/<int:id>",service_detail,name='service_detail'),
    path('category/<str:cat>',service,name='service_cat'),
    
   
]
