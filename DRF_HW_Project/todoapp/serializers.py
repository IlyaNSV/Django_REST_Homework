from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, ToDoNote


class ProjectModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = ('__all__')


class TODONoteModelSerializer(HyperlinkedModelSerializer):
    project = serializers.StringRelatedField()

    class Meta:
        model = ToDoNote
        fields = ('__all__')
