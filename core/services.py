import socket
import subprocess
import time

from api_network_scanner.settings import PATH_TO_SOCKET
from core.serializers import NetstatSerializer, IfstatSerializer, NetworkCommonInfoSerizalizer


class NetworkService:

    def get_netstat(self):
        process = subprocess.run(['netstat'], stdout=subprocess.PIPE)
        output = process.stdout
        output_as_arr = self.bytes_to_arr(output)[2:10]
        prepared_output = [NetstatSerializer(row.split()).data for row in output_as_arr]
        return prepared_output

    def get_ifstat(self):
        process = subprocess.Popen(['ifstat'], stdout=subprocess.PIPE)
        time.sleep(10)
        process.kill()
        output = process.communicate()[0]
        output_as_arr = self.bytes_to_arr(output)
        prepared_output = {
            'interface': output_as_arr[0].strip(),
            'speed': [IfstatSerializer(row.split()).data for row in output_as_arr[2:-1]]
        }
        return prepared_output

    def get_common_info(self):
        process = subprocess.run(['ifconfig'], stdout=subprocess.PIPE)
        output = process.stdout
        output_as_arr = self.bytes_to_arr(output)[:2]
        common_info = NetworkCommonInfoSerizalizer(output_as_arr[1].split()[1:]).data
        common_info['interface'] = output_as_arr[0].split()[0]
        return common_info

    def get_packets_info(self):
        process = subprocess.run(['sudo', PATH_TO_SOCKET], stdout=subprocess.PIPE)
        output = process.stdout
        output_as_arr = self.bytes_to_arr(output)
        return {'raw': output_as_arr[0]}

    def bytes_to_arr(self, bytes_value):
        return bytes_value.decode("utf-8").split('\n')

    def get_interface(self):
        process = subprocess.run(['route', '|', 'grep', '^default'], stdout=subprocess.PIPE)
        output = process.stdout
        return self.bytes_to_arr(output)[0]
