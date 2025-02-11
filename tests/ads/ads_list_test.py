import pytest

from ads.models import Ads
from ads.serializers import AdsSerializer
from tests.factories import AdsFactory


@pytest.mark.django_db
def test_ads_list(client, token):
    items = AdsFactory.create_batch(5)

    expected = {
        "count": 5,
        "next": None,
        "previous": None,
        "results": AdsSerializer(items, many=True).data
    }

    response = client.get("/ads/", content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {token}")

    assert response.status_code == 200
    assert response.data == expected

