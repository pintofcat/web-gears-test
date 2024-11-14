import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient

from app.models import Task


@pytest.fixture
def user_data():
    return {
        'username': 'testuser',
        'password': 'password123',
        'email': 'testuser@example.com',
    }

@pytest.fixture
def create_user(user_data):
    user = get_user_model().objects.create_user(**user_data)
    return user


@pytest.fixture
def auth_client(create_user):
    """Create an authenticated client with JWT token."""
    user = create_user
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    client = APIClient()

    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    return client


@pytest.fixture
def create_task(create_user):
    task = Task.objects.create(title='Task for Comment', description='Task description', assigned_to=create_user)
    return task
