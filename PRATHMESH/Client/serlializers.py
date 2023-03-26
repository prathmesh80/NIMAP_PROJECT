from django.db.models import fields
from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'client_name', 'created_at', 'created_by')


class ClientSerializerById(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'client_name', 'created_at', 'created_by','updated_at')