from django.db import models
from django.utils.text import slugify 
from django import forms
# Create your models here.


class Description(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length = 1000 , null =True,blank=True)
    active=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title


class OurTeam(models.Model):
    name = models.CharField(max_length = 100 , blank=True)
    work = models.CharField(max_length = 100 , blank=True)
    image = models.ImageField( upload_to='photos/ImageOurTeam/%y/%m/%d')
    
    
class Gallery(models.Model):
    image = models.ImageField( upload_to='photos/ImageGallery/%y/%m/%d')


    
    