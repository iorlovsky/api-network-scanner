import subprocess
import time

from core.serializers import NetstatSerializer, IfstatSerializer


class NetworkService:

    def netstat(self):
        process = subprocess.run(['netstat'], stdout=subprocess.PIPE)
        output = process.stdout
        output_as_arr = self.bytes_to_arr(output)[2:10]
        prepared_output = [NetstatSerializer(row.split()).data for row in output_as_arr]
        return prepared_output

    def ifstat(self):
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

    def bytes_to_arr(self, bytes_value):
        return bytes_value.decode("utf-8").split('\n')