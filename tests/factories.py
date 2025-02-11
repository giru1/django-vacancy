import factory.django

from ads.models import Category, Ads
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = factory.Faker('password')
    age = 34


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('name')


class AdsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ads

    name = factory.Faker("name")
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)

    price = 100
