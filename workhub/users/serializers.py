from rest_framework import serializers
from jobs.serializers import JobsSerializer
from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'jobs')
        id = serializers.ReadOnlyField()
        username = serializers.CharField(max_length=200)
        email = serializers.CharField(max_length=200)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
