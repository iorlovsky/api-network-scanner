from rest_framework import views
from rest_framework.response import Response
from core.services import NetworkService

networkService = NetworkService()


class Netstat(views.APIView):

    def get(self, request):
        netstat = networkService.netstat()
        return Response(netstat)


class Ifstat(views.APIView):

    def get(self, request):
        ifstat = networkService.ifstat()
        return Response(ifstat)
