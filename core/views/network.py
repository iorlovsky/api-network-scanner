from rest_framework import views
from rest_framework.response import Response
from core.services import NetworkService

networkService = NetworkService()


class Netstat(views.APIView):

    def get(self, request):
        netstat = networkService.get_netstat()
        return Response(netstat)


class Ifstat(views.APIView):

    def get(self, request):
        ifstat = networkService.get_ifstat()
        return Response(ifstat)


class NetworkCommonInfo(views.APIView):

    def get(self, request):
        network_common_info = networkService.get_common_info()
        return Response(network_common_info)


class PacketsInfo(views.APIView):

    def get(self, request):
        packets_info = networkService.get_packets_info()
        return Response(packets_info)