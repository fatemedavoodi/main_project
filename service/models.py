from django.db import models
from root.models import Category

class Services(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    content1 = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()
    item1 = models.TextField()
    item2 = models.TextField()
    item3 = models.TextField()
    image = models.ImageField(upload_to='service',default='service.jpg')
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('created_date',)

    def snip(self):
        return self.content1[:20]+'...'
    
    def capt(self):
        return self.title.capitalize()