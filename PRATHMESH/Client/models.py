from django.db import models


class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    client_name = models.CharField(max_length=255)
    created_at = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    updated_at = models.CharField(max_length=255)

    def getClientName(self):
        return self.client_name

    def getCreatedBy(self):
        return self.created_by

    def getCreatedAt(self):
        return self.created_at
