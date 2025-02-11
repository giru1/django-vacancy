import pytest


@pytest.mark.django_db
def test_create_ads(client, token, user, category):

    expected = {
        "id": 1,
        "name": "Test Advertisement",
        "author": user.id,
        "price": 100.0,
        "description": "This is a test ad.",
        "is_published": True,
        "image": None,
        "category": category.id
    }

    data = {
        "name": "Test Advertisement",
        "author": user.id,
        "price": 100.0,
        "description": "This is a test ad.",
        "is_published": True,
        "category": category.id
    }

    response = client.post("/ads/create",
                          data,
                          content_type="application/json",
                          HTTP_AUTHORIZATION="Bearer " + token
                          )

    # print(response.data)

    print(response.json())


    assert response.status_code == 201
    # assert response.json() == expected
    assert response.data == expected
