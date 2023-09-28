from django.db import models
from accounts.models import CustomeUser

class Skills(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    



class Comments(models.Model):
    info = models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users')
    skills = models.ManyToManyField(Skills)
    descriptions = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.info.username
    

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
