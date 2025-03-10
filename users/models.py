from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=350)
    lat = models.DecimalField(decimal_places=4, max_digits=6, null=True)
    lng = models.DecimalField(decimal_places=4, max_digits=6, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class User(AbstractUser):
    ROLES = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Админ"),
    ]


    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    role = models.CharField(max_length=50, choices=ROLES, default='member')
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    age = models.PositiveIntegerField(null=True)
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'