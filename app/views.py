import serializers.serializer
from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from app.serializers import TaskCommentSerializer, TaskSerializer
from app.models import Task, TaskComment


class TaskViewSet(viewsets.ModelViewSet):
    """Task view set."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: serializers.serializer.Serializer) -> None:
        serializer.save(assigned_to=self.request.user)


class TaskCommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing task comments.
    """

    serializer_class = TaskCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> QuerySet:
        return TaskComment.objects.filter(task__assigned_to=self.request.user)

    def perform_create(self, serializer: serializers.serializer.Serializer):
        serializer.save(user=self.request.user)
