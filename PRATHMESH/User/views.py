from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serlializers import UserSerializer
from rest_framework import serializers
from rest_framework import status
import datetime


@api_view(['GET'])
def view_users(request):
    if request.query_params:
        users = User.objects.filter(**request.query_params.dict())
    else:
        users = User.objects.all()
    print(users)

    if users:
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_users(request):
    data = {'id': User.objects.count() + 1}
    time = datetime.datetime.now()
    data['name'] = request.data['name']
    data['password'] = request.data['password']

    user = UserSerializer(data=data)

    print(user)

    # Validating for already existing data
    if User.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if user.is_valid():
        user.save()
        return Response(user.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)