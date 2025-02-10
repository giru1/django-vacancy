import pytest

from ads.models import Ads

@pytest.mark.django_db
def test_ads_list(client, token):
    expected = {
        "id": "1",
        "name": "Test Ad",
        "author": 1,
        "price": 100,
        "description": "This is a test ad.",
        "is_published": True,
        "image": None,
        "category": 1
    }

    data = {
        "name": "Test Ad",
        "author": 1,
        "price": 100,
        "description": "This is a test ad.",
        "is_published": True,
        "image": None,
        "category": 1
    }


    response = client.get("/ads/create/",
                          data=data,
                          content_type="application/json",
                          HTTP_AUTHORIZATION="Bearer " + token
                          )



    assert response.status_code == 201
    # assert response.json() == expected
    assert response.data == expected
