from django.db import models

from app.mixins import SoftDeleteMixin


class Task(SoftDeleteMixin):
    """Task model."""

    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(
        "auth.User", on_delete=models.SET_NULL, null=True, related_name="tasks"
    )
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attachment = models.FileField(upload_to="attachments/", null=True, blank=True)

    def __str__(self):
        return self.title


class TaskComment(SoftDeleteMixin):
    """Task comment model."""

    text = models.TextField()
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="task_comment"
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
