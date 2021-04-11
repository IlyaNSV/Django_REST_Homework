from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import DefaultUser


class DefaultUserModelSerializerVer1(ModelSerializer):
    class Meta:
        model = DefaultUser
        fields = ('mail', 'user_name', 'first_name', 'last_name')


class DefaultUserModelSerializerVer2(ModelSerializer):
    class Meta:
        model = DefaultUser
        fields = ('mail', 'user_name', 'first_name', 'last_name', 'is_staff', 'is_superuser')
