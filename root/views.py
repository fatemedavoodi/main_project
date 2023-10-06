from django.shortcuts import render,redirect
from .models import *
from service.models import Services
from accounts.models import CustomeUser
from .forms import *
from django.contrib import messages

def home(request):
   
    category = Category.objects.all()
    property = Properties_company.objects.filter(status=True)
    team_member = Team_members.objects.filter(status=True)
    skills = Skills.objects.all()
    service_count = Services.objects.filter(status=True).count() 
    user_count = CustomeUser.objects.filter(is_active=True).count()
    property_count = Properties_company.objects.filter(status=True).count()
    three_service = Services.objects.filter(status=True)[:3]
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
        'three_service':three_service
    }
    return render(request,'root/index.html',context=context)

def about(request):
    category = Category.objects.all()
    service_count = Services.objects.filter(status=True).count() 
    user_count = CustomeUser.objects.filter(is_active=True).count()
    property_count = Properties_company.objects.filter(status=True).count()
    team_member = Team_members.objects.filter(status=True)
    context={
        'category': category,
        'service_count': service_count,
        'user_count': user_count,
        'property_count': property_count,
        'team_member':team_member,
    }
    return render(request,'root/about.html',context=context)

def contact(request):
    if request.method == 'GET':
        category = Category.objects.all()
        context={
            'category':category,
        }
        return render(request,"root/contact.html",context=context)
    elif request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'we recieved your message')
            return redirect('root:contact')
        else:
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('root:contact')

def pricing(request):
    category = Category.objects.all()
    context={
        'category': category,
    }
    return render(request,'root/pricing.html',context=context)

def request(request):
    if request.method == 'GET':
        category = Category.objects.all()
        context={
            'category':category,
        }
        return render(request,"root/contact.html",context=context)
    elif request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'we recieved your message')
            return redirect('root:contact')
        else:
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('root:contact')
