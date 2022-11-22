from rest_framework import serializers

from Task.models import TaskModel
from Users.models import UsersModel


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'
