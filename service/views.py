from django.shortcuts import render
from .models import *

# Create your views here.
def service(request):
    return render(request,'service/services.html')


def service_detail(request,id):
    return render(request,'service/services_details.html')