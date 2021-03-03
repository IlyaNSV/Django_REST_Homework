from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import DefaultUser
from .serializers import DefaultUserModelSerializer


class DefaultUserModelViewSet(ModelViewSet):
    queryset = DefaultUser.objects.all()
    serializer_class = DefaultUserModelSerializer
