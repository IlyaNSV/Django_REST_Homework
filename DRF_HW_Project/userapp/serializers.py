from rest_framework.serializers import HyperlinkedModelSerializer
from .models import DefaultUser


class DefaultUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = DefaultUser
        fields = ('url','mail', 'user_name', 'first_name', 'last_name')
