from rest_framework import views
from rest_framework.response import Response
from core.services import NetworkService


class Scanners(views.APIView):
    networkService = NetworkService()

    def get(self, request):
        netstat = self.networkService.netstat()
        return Response({'netstat': netstat})