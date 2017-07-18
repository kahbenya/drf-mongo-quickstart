from django_mongoengine.mongo_auth.models import User
from rest_framework_mongoengine import viewsets
from quickstart.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
