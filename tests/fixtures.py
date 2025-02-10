import pytest


@pytest.fixture
@pytest.mark.django_db
def token(client, user):
    username = "hr123"
    password  = "password"

    user.objects.create_user(
        username=username,
        password=password,
        email="<EMAIL>",
    )
    response = client.post(
        "/auth/login/",
        {"username": username, "password": password},
        format="json",
    )

    return response.data["token"]
