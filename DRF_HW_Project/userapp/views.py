from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import DefaultUser
from .serializers import DefaultUserModelSerializer
from rest_framework import mixins, viewsets


class DefaultUserCustomModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                                    viewsets.GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = DefaultUser.objects.all()
    serializer_class = DefaultUserModelSerializer

