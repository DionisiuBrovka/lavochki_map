from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, verbose_name="Пользователь")
    photo = models.CharField(verbose_name="Аватар", max_length=250, blank=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=13, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class PhotoLav(models.Model):
    image_path = models.ImageField(
        verbose_name="Фото", 
        null=False,
        upload_to='media'
    )

    alt = models.CharField(
        verbose_name="Описание",
        null=True,
        blank=True,
        max_length=250
    )

    is_valid = models.BooleanField(
        verbose_name="Проверено", 
        null=False,
        default=False
    )


class Lavochki(models.Model):
    user = models.ForeignKey(
        Profile, 
        on_delete = models.CASCADE, 
        verbose_name="Пользователь",
        null=False
    )

    x = models.FloatField(
        verbose_name="Долгота",
        null=False
    )

    y = models.FloatField(
        verbose_name="Широта",
        null=False
    )

    description = models.TextField(
        verbose_name="Описание", 
        null=False
    )

    photo = models.ForeignKey(
        PhotoLav, on_delete = models.CASCADE, 
        verbose_name="Главное фото", 
        null=True,
        blank=True
    )

    is_padik =  models.BooleanField(
        verbose_name="Возле подъезда", 
        null=True,
        blank=True,
        default=False
    ) 

    is_ten =  models.BooleanField(
        verbose_name="В тени", 
        null=True,
        blank=True,
        default=False, 
    ) 

    activiti =  models.IntegerField(
        verbose_name="Активность возле лавочки", 
        null=False,
        default=1
    ) 

    rating = models.FloatField(
        verbose_name="Рейтинг", 
        null=True,
        blank=True,
        default=5.0
    )

    date_added = models.DateTimeField(
        verbose_name="Дата добавление", 
        null=False,
        auto_now=True
    )

    is_valid = models.BooleanField(
        null=False,
        verbose_name="Проверено"
    )

class Marks(models.Model):
    user = models.ForeignKey(
        Profile, 
        on_delete = models.CASCADE, 
        verbose_name="Пользователь",
        null=False
    )

    lavochka = models.ForeignKey(
        Lavochki, 
        on_delete = models.CASCADE, 
        verbose_name="Лавочка",
        null=False
    )

    rating = models.IntegerField(
        verbose_name="Оценка",
        null=False
    )

    date_added = models.DateTimeField(
        verbose_name="Дата добавления",
        null=False
    )

