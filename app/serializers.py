from rest_framework import serializers

from app.models import Task, TaskComment


class TaskSerializer(serializers.ModelSerializer):
	"""Task serializer."""

	class Meta:
		model = Task
		fields = "__all__"
		read_only_fields = ['user', 'created_at', 'updated_at']


class TaskCommentSerializer(serializers.ModelSerializer):
	"""Task comment serializer."""
	user = serializers.ReadOnlyField(source='user.username')

	class Meta:
		model = TaskComment
		fields = "__all__"
		read_only_fields = ['user', 'created_at']