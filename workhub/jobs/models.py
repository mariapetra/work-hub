from django.contrib.auth import get_user_model
from django.db import models


class Jobs(models.Model):
    company = models.CharField(max_length=200)
    description = models.TextField()
    location = models.TextField()
    hours = models.IntegerField()
    contract_type = models.TextField()
    manager = models.CharField(max_length=200)
    manager_email = models.EmailField()
    salary = models.IntegerField()
    notes = models.TextField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_jobs'
    )
