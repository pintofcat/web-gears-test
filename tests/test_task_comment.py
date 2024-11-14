import pytest
from rest_framework import status
from django.urls import reverse
from app.models import TaskComment


@pytest.mark.django_db
def test_create_task_comment(auth_client, create_task, create_user):
    url = reverse("task_comments-list")
    data = {"text": "This is a comment", "task": create_task.id}
    response = auth_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["text"] == "This is a comment"


@pytest.mark.django_db
def test_list_task_comments(auth_client, create_task, create_user):
    TaskComment.objects.create(
        text="This is a comment", task=create_task, user=create_user
    )

    url = reverse("task_comments-list")
    response = auth_client.get(url, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0
