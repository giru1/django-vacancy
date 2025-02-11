import pytest

from ads.serializers import AdsSerializer


@pytest.mark.django_db
def test_get_one_ads(client, ad, token):
    response = client.get(
        f"/ad/{ad.id}",
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {token}")
    assert response.status_code == 200
    assert response.data == AdsSerializer(ad).data
