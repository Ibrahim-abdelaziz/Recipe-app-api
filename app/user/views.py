from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import CreateUserSerializer, AuthtokenSerializer
from rest_framework import generics, permissions, authentication

class CreateUserView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthtokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = CreateUserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, request):
        return self.request.user
