from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from .models import Client
from Project.models import Project
from .serlializers import ClientSerializer
from .serlializers import ClientSerializerById
from Project.serlializers import ProjectSerializer
from rest_framework import serializers
from rest_framework import status
import datetime


@api_view(['POST'])
def add_client(request):
    data = {'id': Client.objects.count() + 1}

    time = datetime.datetime.now()
    data['client_name'] = request.data['client_name']
    data['created_at'] = str(time.strftime("%Y/%m/%d, %H:%M:%S"))

    if request.session.has_key('name'):
        data['created_by'] = request.session['name']
    else:
        raise serializers.ValidationError('Please login first')

    client = ClientSerializer(data=data)

    # validating for already existing data

    if Client.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if client.is_valid():
        client.save()
        return Response(client.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_clients(request):
    # Checking for the parameters from the URL

    if request.session.has_key('name'):
        if request.query_params:
            clients = Client.objects.filter(**request.query_params.dict())
        else:
            clients = Client.objects.all()

        # If there is something in items else raise error

        if clients:
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        raise serializers.ValidationError('Please login First')


@api_view(['GET'])
def view_clientById(request, id):
    if request.session.has_key('name'):

        clients = Client.objects.filter(id=id)
        clientName = Client.objects.get(id=id).getClientName()
        projectList = Project.objects.filter(client_name=clientName)

        if projectList:
            serializer = ProjectSerializer(projectList, many=True)
            return Response(serializer.data)
        elif clients:
            serializer = ClientSerializerById(clients, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        raise serializers.ValidationError('Please login First')


@api_view(['POST'])
def add_projects(request, id):
    if request.session.has_key('name'):

        data = {'id': Project.objects.count() + 1}

        time = datetime.datetime.now()
        data['project_name'] = request.data['project_name']
        data['client_name'] = Client.objects.get(id=id).getClientName()
        data['created_at'] = str(time.strftime("%Y/%m/%d, %H:%M:%S"))
        data['created_by'] = request.session["name"]

        user_info = str(request.data['users'])

        print(user_info)

        data['users'] = user_info

        project = ProjectSerializer(data=data)

        print(project)

        if Project.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already exists')

        if project.is_valid():
            project.save()
            return Response(project.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        raise serializers.ValidationError('Please Login First')


@api_view(['POST'])
def update(request, id=None):
    if request.session.has_key('name'):

        data = {'id': id}

        time = datetime.datetime.now()

        item = Client.objects.get(id=id)

        data['client_name'] = request.data['client_name']
        data["created_by"] = Client.objects.get(id=id).getCreatedBy()
        data["created_at"] = Client.objects.get(id=id).getCreatedAt()
        data['updated_at'] = str(time.strftime("%Y/%m/%d, %H:%M:%S"))

        client = ClientSerializer(instance=item, data=data)

        # validating for already existing data

        if client.is_valid():
            client.save()
            return Response(client.data)
        else:
            print(client.errors)
            return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        raise serializers.ValidationError('Please login First')


@api_view(['DELETE'])
def delete(request, id=None):
    if request.session.has_key('name'):

        clients = Client.objects.filter(id=id)
        clientName = Client.objects.get(id=id).getClientName()
        projectList = Project.objects.filter(client_name=clientName)

        if clients:
            clients.delete()
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

        if projectList:
            projectList.delete()
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        raise serializers.ValidationError('Please login First')
