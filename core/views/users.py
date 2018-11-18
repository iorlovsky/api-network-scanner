from rest_framework import views, generics
from rest_framework.response import Response

from core import serializers, models


class SigninView(views.APIView):

    def post(self, request, *args, **kwargs):
        return Response({'test': 'ok'})


class SignupView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
