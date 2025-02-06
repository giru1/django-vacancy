from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=10, unique=True, validators=[MinValueValidator(5)], null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


def validate_price(value):
    if value < 0:
        raise ValidationError('Цена не может быть отрицательной')

def validate_is_published(value):
    if value:
        raise ValidationError('Объявление не может быть опубликовано')


class Ads(models.Model):
    name = models.CharField(max_length=150, null=False, validators=[MinValueValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField(null=True, validators=[MinValueValidator(0)])
    description = models.CharField(max_length=1000, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='ads/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'