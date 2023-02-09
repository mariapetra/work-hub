from django.db import models


class Jobs(models.Model):
    company = models.CharField(max_length=200)
    description = models.TextField()
    location = models.TextField()
    hours = models.IntegerField()
    # start_date = models.DateField()
    # end_date = models.DateField()
    contract_type = models.TextField()
    manager = models.CharField(max_length=200)
    manager_email = models.EmailField()
    salary = models.IntegerField()
    notes = models.TextField()
