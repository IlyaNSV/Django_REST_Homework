from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import DefaultUser


class DefaultUserModelSerializer(ModelSerializer):
    class Meta:
        model = DefaultUser
        fields = ('mail', 'user_name', 'first_name', 'last_name')
