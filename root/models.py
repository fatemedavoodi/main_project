from django.db import models
from accounts.models import CustomeUser




class Skills(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Properties_company(models.Model):
    title = models.CharField(max_length=200)
    content1 = models.TextField()
    content2 = models.TextField()
    image = models.ImageField(upload_to='property',default='property.jpg')
    status = models.BooleanField(default=False)
    updates_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    

class Team_members(models.Model):
    info = models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='team_members')
    skills = models.ManyToManyField(Skills)
    descriptions = models.TextField()
    twitter= models.CharField(max_length=200,default='#')
    facebook= models.CharField(max_length=200,default='#')
    instagram= models.CharField(max_length=200,default='#')
    linkdin= models.CharField(max_length=200,default='#')
    status = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info.username





class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Request(models.Model):
    city_departure = models.CharField(max_length=100)
    delivery_city = models.CharField(max_length=100)
    total_weight = models.IntegerField()
    dimensions = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
