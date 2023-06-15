from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.db.models.signals import post_save
from foodmenu.models import Restaurantmenu

class Profile(models.Model):
    user=models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    productfavorites=models.ManyToManyField(Restaurantmenu)
    phone=models.CharField(max_length=20,verbose_name=_("phone")) 
    adress=models.CharField(max_length=100)
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
