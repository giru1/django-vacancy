import pytest

@pytest.mark.django_db
def test_selection_create(client, token, user, ad):
    response = client.post(
        "/selection/create/",
        {
            "name": "new test",
            "owner": user.id,
            "items": [ad.id]
        },
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {token}")

    assert response.status_code == 201
    assert response.data == {'id': 1, 'name': 'new test', 'owner': user.id, 'items': [ad.id]}