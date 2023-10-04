from django.shortcuts import render,get_object_or_404
from .models import *
from root.models import Category,Properties_company

# Create your views here.
def service(request,cat=None):
    category = Category.objects.all()
    property = Properties_company.objects.filter(status=True)
    if cat:
        service= Services.objects.filter(category__name=cat)
    else:
        service= Services.objects.filter(status=True)
    context={
        'service':service,
        'category': category,
        'property': property,
    }
    return render(request,'service/services.html',context=context)


def service_detail(request,id):
    try:
        service = Services.objects.get(id=id)
        context={
            'service': service,
        }
        
        return render(request,'service/service-details.html',context=context)
    except:
        return render(request,'service/404.html')