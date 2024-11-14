import pytest
from rest_framework import status
from django.urls import reverse
from app.models import Task


@pytest.mark.django_db
def test_create_task(auth_client, create_user):
    user = create_user
    url = reverse("tasks-list")
    data = {"title": "New Task", "description": "Test Task", "assigned_to": user.id}
    response = auth_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["title"] == "New Task"


@pytest.mark.django_db
def test_update_task(auth_client, create_user):
    task = Task.objects.create(
        title="Initial Task", description="Task description", assigned_to=create_user
    )
    url = reverse("tasks-detail", args=[task.id])
    data = {"title": "Updated Task"}
    response = auth_client.patch(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == "Updated Task"


@pytest.mark.django_db
def test_delete_task(auth_client, create_user):
    task = Task.objects.create(
        title="Task to Delete", description="Delete this task", assigned_to=create_user
    )
    url = reverse("tasks-detail", args=[task.id])
    response = auth_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Task.objects.filter(id=task.id).exists()
