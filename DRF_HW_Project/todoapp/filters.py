from django_filters import rest_framework as filters
from .models import Project, ToDoNote


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class ToDoNoteProjectFilter(filters.FilterSet):
    created = filters.DateFromToRangeFilter()

    class Meta:
        model = ToDoNote
        fields = ['project', 'created']


