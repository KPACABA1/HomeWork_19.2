from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Адрес электронной почты')

    avatar = models.ImageField(upload_to="users/", verbose_name="Аватар пользователя", null=True, blank=True)
    phone_number = models.PositiveIntegerField()
