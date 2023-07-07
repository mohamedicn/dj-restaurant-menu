from django.db import models

# Create your models here.

class Food(models.Model):
    name_food = models.CharField(max_length= 35) 
    contant_food = models.TextField()
    Prise_food = models.DecimalField(max_digits=5,decimal_places=2)
    image_food = models.ImageField(upload_to='photos/%y/%m/%d')
    active_food = models.BooleanField(default=True)
    


