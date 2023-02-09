from rest_framework import serializers
from .models import Jobs


class JobsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    company = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    location = serializers.CharField(max_length=None)
    hours = serializers.IntegerField()
    contract_type = serializers.CharField(max_length=200)
    manager = serializers.CharField(max_length=200)
    manager_email = serializers.EmailField()
    salary = serializers.IntegerField()
    notes = serializers.CharField(max_length=None)
    owner = serializers.ReadOnlyField(source='owner.id')

    def create(self, validated_data):
        return Jobs.objects.create(**validated_data)


class JobsDetailSerializer(JobsSerializer):

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get(
            'date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
