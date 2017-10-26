from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(allow_null=False, input_formats=['%Y-%m-%d', '%m/%d/%Y', '%Y-%m-%dT%H:%M:%S.%fZ'])

    class Meta:
        model = User
        fields = ('id', 'username', 'birthday', 'rand_num')
