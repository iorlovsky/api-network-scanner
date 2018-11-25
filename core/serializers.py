from rest_framework import serializers
import uuid
from core import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('email', )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        return user


class NetstatSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    protocol = serializers.SerializerMethodField()
    recv_q = serializers.SerializerMethodField()
    send_q = serializers.SerializerMethodField()
    local_addr = serializers.SerializerMethodField()
    foreign_addr = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()

    def get_id(self, data):
        return uuid.uuid4()

    def get_protocol(self, data):
        return data[0]

    def get_recv_q(self, data):
        return data[1]

    def get_send_q(self, data):
        return data[2]

    def get_local_addr(self, data):
        return data[3]

    def get_foreign_addr(self, data):
        return data[4]

    def get_state(self, data):
        return data[5]

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
