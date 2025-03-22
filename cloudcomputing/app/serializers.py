from rest_framework import serializers

from app.models import *


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'avatar')
        extra_kwargs = {'password': {'write_only': True}}

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
