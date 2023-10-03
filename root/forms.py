from django import forms
from .models import ContactUs,Request

class ContactUsForm(forms.ModelForm):
    
    class Meta:
        model = ContactUs
        fields = ['name','email','subject','message']

class RequestForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = ['city_departure','delivery_city','total_weight','dimensions','name','email','phone','message']