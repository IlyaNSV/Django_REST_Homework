from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Project, TODO_note
from .serializers import ProjectModelSerializer, TODONoteModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TODONoteModelViewSet(ModelViewSet):
    queryset = TODO_note.objects.all()
    serializer_class = TODONoteModelSerializer
