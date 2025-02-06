import re
from datetime import date

from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User, Location


class UserListSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

def validate_email(value):
    if re.search(r'@rambler\.ru$', value.lower()):
        raise ValidationError('Registration with rambler.ru email is not allowed.')
    return value

def validate_birth_date(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 9:
        raise ValidationError('Users younger than 9 years old cannot register.')
    return value

class UserCreateSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    locations = serializers.SlugRelatedField(
        many=True,
        queryset=Location.objects.all(),  # Укажите queryset для получения местоположений
        slug_field="id"
    )
    birth_date = serializers.DateField(
        validators=[
            validate_birth_date
        ])
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all()), validate_email])

    class Meta:
        model = User
        fields = '__all__'
        # exclude = ['locations']

    def create(self, validated_data):
        locations_data = validated_data.pop('locations', [])
        user = User.objects.create(**validated_data)

        # Сохраняем местоположения
        user.locations.set(locations_data)
        user.set_password(validated_data["password"])  # Убедитесь, что пароль устанавливается правильно
        user.save()

        return user



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
