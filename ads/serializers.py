from django.core.validators import MinValueValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ads.models import Ads, Category


class AdsSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=150, min_length=10, required=True)
    description = serializers.CharField(required=False)
    price = serializers.FloatField(validators=[MinValueValidator(0)])
    is_published = serializers.BooleanField(default=False)

    class Meta:
        model = Ads
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    slug = serializers.CharField(
        max_length=10,
        min_length=5,
        validators=[UniqueValidator(queryset=Category.objects.all())]
    )