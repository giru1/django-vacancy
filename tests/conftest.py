from pytest_factoryboy import register

from tests.factories import UserFactory, CategoryFactory, AdsFactory

pytest_plugins = "tests.fixtures"

register(UserFactory)
register(CategoryFactory)
register(AdsFactory)
