from django.db import models
from rest_framework import serializers


class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    project_name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    created_at = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    users = models.CharField(max_length=5000)

    def __str__(self):
        return str(self.id) + " " + " " + self.project_name
