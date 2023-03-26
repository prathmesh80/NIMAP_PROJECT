from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project
from .serlializers import ProjectSerializer
from rest_framework import serializers
from rest_framework import status


@api_view(['GET'])
def view_projects(request):
    if request.session.has_key('name'):
        if request.query_params:
            projects = Project.objects.filter(**request.query_params.dict())
        else:
            projects = Project.objects.all()

        print(projects)

        # If there is something in projects else raise error

        if projects:
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        raise serializers.ValidationError('Please Login First')
