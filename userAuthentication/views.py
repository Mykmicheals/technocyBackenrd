
from django.contrib.auth.models import User
from .serializers import RegisterSerializer,MyTokenObtainPairSerializer,UpdateUserSerializer
from rest_framework import generics

from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UpdateProfileView(generics.UpdateAPIView):

    queryset = User.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer
