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
        fields = (
            'id',
            'username',
            'password',
            'avatar',
            'maximum_capacity',
            'used_capacity',
            'expiration_date'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id','name', 'type', 'link', 'size', 'created_date', 'owner')
        read_only_fields = ('id',)

class FileShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileShare
        fields = ('file', 'user', 'shared_date')