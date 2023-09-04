from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator
import uuid
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.utils.text import slugify



# Create your models here.
class Food(models.Model):
    name_food = models.CharField(max_length= 35) 
    contant_food = models.TextField()
    Prise_food = models.DecimalField(max_digits=5,decimal_places=2)
    image_food = models.ImageField(upload_to='photos/%y/%m/%d')
    active_food = models.BooleanField(default=True)


class BookATable(models.Model):
    ChooseTableSize = models.IntegerField(default=2)
    ChooseADay = models.DateField(default=timezone.now)
    ChooseATime = models.TimeField(default=timezone.now) 
    ChooseAddressTable = models.IntegerField(default= 1,null=True)
    NotesIfAny = models.TextField(max_length=200,blank=True, null=True)
    IsTableActive = models.BooleanField(default=False)                                              
    
    
class Restaurantmenu(models.Model):
    Name = models.CharField(max_length=40)
    Price = models.DecimalField(max_digits=5,decimal_places=2)
    Image = models.ImageField(upload_to='photos/RestaurantMenu/%y/%m/%d')
    Category = models.CharField(max_length=40)
    slug = models.SlugField(blank=True ,null=True)
    def save(self,*args,**kwargs):
        self.slug= slugify(self.Name)
        super(Restaurantmenu,self).save(*args,**kwargs)
    #Assess =models.ImageField(upload_to='photos/RestaurantMenu/Assess/%y/%m/%d')
    
    def __str__(self):
        return self.Name
    
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_date= models.DateTimeField(verbose_name=_("Created At"), default=datetime.now)
    # detils = models.ManyToManyField(Restaurantmenu )
    is_finished = models.BooleanField()
    def __str__(self):
        return 'User : ' + str(self.user) + ' ==>' + 'is_finished : ' + str(self.is_finished)



class OrderDetails(models.Model):
    product = models.ForeignKey(Restaurantmenu,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    cost=models.DecimalField(max_digits=5,decimal_places=0,verbose_name=_("Cost"))
    quantity=models.IntegerField()
    class Meta:
        verbose_name = _("OrderDetail")
        verbose_name_plural = _("OrderDetails")
    def __str__(self):
        return 'User: ' +  self.order.user.username + 'Product: '+ self.product.Name + 'Order id: ' + str(self.order.id)
    # def get_absolute_url(self):
    #     return reverse("OrderDetails_detail", kwargs={"pk": self.pk})







#  This class use to check address is CharField or UrlField  
class CharOrURLField(models.CharField):
    validators = [URLValidator()]

    def get_prep_value(self, value):
        if self.is_valid_url(value):
            return value.lower()
        return value

    def is_valid_url(self, value):
        try:
            URLValidator()(value)
            return True
        except:
            return False

# class FoodDelivery(models.Model):
#     Name = models.CharField(max_length=40)
#     Phone = models.CharField(max_length=50)
#     NotesIfAny = models.TextField(max_length=100)
#     Address = CharOrURLField(max_length=255) # Char or URL field 




