from rest_framework import serializers
# from .models import Jobs


class JobsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    company = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    location = serializers.CharField(max_length=None)
    hours = serializers.IntegerField()
    # start_date = serializers.DateField()
    # end_date = serializers.DateField()
    contract_type = serializers.CharField(max_length=200)
    manager = serializers.CharField(max_length=200)
    moanage_email = serializers.EmailField()
    salary = serializers.IntegerField()
    notes = serializers.CharField(max_length=None)
