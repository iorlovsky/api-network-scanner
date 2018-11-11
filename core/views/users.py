from rest_framework import views
from rest_framework.response import Response

from core.models import User


class SigninView(views.APIView):

    def post(self, request, *args, **kwargs):
        return Response({'test': 'ok'})

