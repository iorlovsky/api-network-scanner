from rest_framework import serializers
from rest_framework.compat import authenticate


class SigninSerializer(serializers.Serializer):

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'),
                            email=email, password=password)

        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass