from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Project, ToDoNote


class ProjectModelSerializer(ModelSerializer):
    members = HyperlinkedRelatedField(many=True, view_name='defaultuser-detail', read_only=True)

    class Meta:
        model = Project
        fields = ('__all__')


class TODONoteModelSerializer(HyperlinkedModelSerializer):
    project = HyperlinkedIdentityField(view_name='project-detail')
    creator_user = HyperlinkedIdentityField(view_name='defaultuser-detail')
    # project = serializers.StringRelatedField()

    class Meta:
        model = ToDoNote
        fields = ('__all__')
