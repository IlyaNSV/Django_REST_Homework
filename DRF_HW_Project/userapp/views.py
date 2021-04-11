from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import DefaultUser
from .serializers import DefaultUserModelSerializerVer1, DefaultUserModelSerializerVer2
from rest_framework import mixins, viewsets, permissions


class DefaultUserCustomModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                                    viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = DefaultUser.objects.all()
    serializer_class = DefaultUserModelSerializerVer1

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return DefaultUserModelSerializerVer2
        return DefaultUserModelSerializerVer1

