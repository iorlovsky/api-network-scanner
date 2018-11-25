import subprocess

from core.serializers import NetstatSerializer


class NetworkService:

    def netstat(self):
        process = subprocess.run(['netstat'], stdout=subprocess.PIPE)
        output = process.stdout
        output_as_arr = output.decode("utf-8").split('\n')[2:10]
        prepared_output = [NetstatSerializer(row.split()).data for row in output_as_arr]
        return prepared_output
