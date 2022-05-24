from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class PhotoLav(models.Model):
    alt = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200)

class Lavochki(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    descroption = models.TextField()
    photos_id = models.ForeignKey(PhotoLav, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    is_valid = models.BooleanField()
    raiting = models.FloatField()
    date_added = models.DateTimeField()

class Marks(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    raiting = models.IntegerField()
    Lavochki_id = models.ForeignKey(Lavochki, on_delete = models.CASCADE)
    date_added = models.DateTimeField()

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