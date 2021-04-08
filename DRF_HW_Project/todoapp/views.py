from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .filters import ProjectFilter, ToDoNoteProjectFilter
from .models import Project, ToDoNote
from .serializers import ProjectModelSerializer, TODONoteModelSerializer, TODONoteModelSerializerBase
from .paginations import ProjectListPagination, ToDoNoteListPagination

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectListPagination
    filterset_class = ProjectFilter
    permission_classes = [permissions.IsAuthenticated]


class TODONoteModelViewSet(ModelViewSet):
    queryset = ToDoNote.objects.all()
    serializer_class = TODONoteModelSerializer
    pagination_class = ToDoNoteListPagination
    filterset_class = ToDoNoteProjectFilter
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TODONoteModelSerializer
        return TODONoteModelSerializerBase

    def destroy(self, request, *args, **kwargs):
        note = ToDoNote.objects.get(id=kwargs['pk'])
        note.actual_sign = note.CLOSED
        note.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
