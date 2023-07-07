from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.db.models.signals import post_save
from foodmenu.models import Restaurantmenu

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    productfavorites=models.ManyToManyField(Restaurantmenu)
    phone=models.CharField(max_length=20,verbose_name=_("phone")) 
    NotesIf_any=models.CharField(max_length=500,verbose_name="Notes")
    
    slug=models.SlugField(blank=True, null=True) 
    join_date=models.DateTimeField(verbose_name=_("Created At"), default=datetime.now)
    
    def save(self ,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return '%s' %(self.user)

    def get_absolute_url(self):
        return reverse("accounts:Profile_detail", kwargs={"slug": self.slug})

    def create_profile(sender ,*args, **kwargs):
        if kwargs['created']:
            user_profile=Profile.objects.create(user=kwargs['instance'])    
    post_save.connect(create_profile , sender=User)

class Static_Address(models.Model):
    std_address =models.CharField(max_length=150)
    cost =models.CharField(max_length=50)
    distance =models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    
    def __str__(self):
        return self.std_address

    
class Address(models.Model):
    user=models.ForeignKey(Profile,verbose_name=_("user"), on_delete=models.CASCADE)
    sta_address=models.ForeignKey(Static_Address,verbose_name=_("Static Address"), on_delete=models.CASCADE)
    address =models.CharField(max_length=150,verbose_name=_("detail for Static Address"))
    
    def __str__(self):
        return 'User : ' + str(self.user) + ' ==> ' + ' address : ' + str(self.sta_address)

