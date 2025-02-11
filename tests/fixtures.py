import pytest


@pytest.fixture
@pytest.mark.django_db
def token(client, django_user_model):
    username = "hr123"
    password  = "password"

    django_user_model.objects.create_user(
        username=username,
        password=password,
        role="admin",
    )
    response = client.post(
        "/users/token",
        {
            "username": username,
            "password": password
        },
        format="json",
    )

    return response.data["access"]
