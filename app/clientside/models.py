from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    photo = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=13, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class PhotoLav(models.Model):
    image_path = models.ImageField(upload_to='media')
    alt = models.CharField(max_length=200)
    is_valid = models.BooleanField(default=False)

class Lavochki(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    description = models.TextField(blank=True)
    photos_id = models.ForeignKey(PhotoLav, on_delete = models.CASCADE, blank=True, default=1)
    user_id = models.ForeignKey(Profile, on_delete = models.CASCADE)
    is_valid = models.BooleanField()
    rating = models.FloatField(blank=True, default=5.0)
    date_added = models.DateTimeField(auto_now=True)
    is_padik =  models.BooleanField(blank=True, default=False) 
    is_ten =  models.BooleanField(blank=True, default=False, null=True) 
    is_activiti =  models.IntegerField(blank=True, default=1) 

class Marks(models.Model):
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    rating = models.IntegerField()
    lavochka = models.ForeignKey(Lavochki, on_delete = models.CASCADE)
    date_added = models.DateTimeField()

