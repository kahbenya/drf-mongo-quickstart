from django_mongoengine.mongo_auth.models import User
from rest_framework_mongoengine import serializers


class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', )



