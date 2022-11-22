from rest_framework import serializers

from Users.models import UsersModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = '__all__'
