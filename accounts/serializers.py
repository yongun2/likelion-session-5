

from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        