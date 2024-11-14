import pytest
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model


@pytest.fixture
def user_data():
    return {
        "username": "testuser",
        "password": "password123",
        "email": "testuser@example.com",
    }


@pytest.fixture
def create_user(user_data):
    user = get_user_model().objects.create_user(**user_data)
    return user


@pytest.mark.django_db
def test_user_login(client, create_user):
    url = reverse("token_obtain_pair")
    data = {"username": "testuser", "password": "password123"}
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["access"]
