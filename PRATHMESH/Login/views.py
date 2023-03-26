from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from User.models import User
from User.serlializers import UserSerializer
from rest_framework import serializers
from rest_framework import status
import datetime


@api_view(['POST'])
def check_login(request):

    name = request.data['name']

    userData = User.objects.filter(name=name)
    print(name)
    if userData:
        user = UserSerializer(userData, many=True)
        request.session['name'] = request.data['name']
        return Response(user.data)
    else:
        return Response("Invalid User Name")
