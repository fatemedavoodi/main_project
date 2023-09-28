from django.shortcuts import render

# Create your views here.
def service(request):
    return render(request,'service/services.html')


def service_detail(request):
    return render(request,'service/service-details.html')