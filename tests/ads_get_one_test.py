import pytest

from ads.models import Ads

@pytest.mark.django_db
def test_ads_list(client):
    ads = Ads.objects.create(
        ame="Test Ad",
        author_id=1,  # Assuming there's a user with ID 1
        price=100,
        description="This is a test ad.",
        is_published=True
    )
    # ads_list = Ads.objects.all()

    expected = {
        "count": 1,
        "results": [{
            "name":
            "Test Ad",
            "author": 1,
            "price": 100,
            "description": "This is a test ad.",
            "is_published": True,
            "image": None,
            "category": 1
        }]
    }

    response = client.get("/ads/")
    response_one = client.get("/ads/1/")
    assert response.status_code == 200
    assert response.json() == expected
    assert response.data == expected
