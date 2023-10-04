from django.shortcuts import render
from .models import *
from service.models import Services
from accounts.models import CustomeUser

def home(request):
   
    category = Category.objects.all()
    property = Properties_company.objects.filter(status=True)
    team_member = Team_members.objects.filter(status=True)
    skills = Skills.objects.all()
    service_count = Services.objects.filter(status=True).count() 
    user_count = CustomeUser.objects.filter(is_active=True).count()
    property_count = Properties_company.objects.filter(status=True).count()
    if request.GET.get('search'):
        service = Services.objects.filter(content1__contains=request.GET.get('search'))
    else:
        service = Services.objects.filter(status=True)
    context ={
        'category': category,
        'service': service,
        'service_count': service_count,
        'user_count': user_count,
        'property_count': property_count,
        'property': property,
        'team_member': team_member,
        'skills':skills,
    }
    return render(request,'root/index.html',context=context)

def about(request):
    category = Category.objects.all()
    service_count = Services.objects.filter(status=True).count() 
    user_count = CustomeUser.objects.filter(is_active=True).count()
    property_count = Properties_company.objects.filter(status=True).count()
    
    context={
        'category': category,
        'service_count': service_count,
        'user_count': user_count,
        'property_count': property_count,
    }
    return render(request,'root/about.html',context=context)

def contact(request):
    category = Category.objects.all()
    context={
        'category': category,
    }
    return render(request,'root/contact.html',context=context)

def pricing(request):
    category = Category.objects.all()
    context={
        'category': category,
    }
    return render(request,'root/pricing.html',context=context)

def request(request):
    category = Category.objects.all()
    context={
        'category': category,
    }
    return render(request,'root/get-a-quote.html',context=context)