from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, TODO_note


class ProjectModelSerializer(HyperlinkedModelSerializer):
    members = serializers.HyperlinkedRelatedField(view_name='DefaultUser-detail',
                                                  lookup_field='uuid', many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('__all__')


class TODONoteModelSerializer(HyperlinkedModelSerializer):
    project = serializers.StringRelatedField()
    creator_user = serializers.HyperlinkedRelatedField(view_name='DefaultUser-detail',
                                                       lookup_field='uuid', read_only=True)

    class Meta:
        model = TODO_note
        fields = ('__all__')
