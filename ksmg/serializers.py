from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Ksmg, KsmgEE

class KsmgEESerializer(serializers.ModelSerializer):
    class Meta:
        model = KsmgEE
        fields = ('__all__')

class KsmgSerializer(serializers.ModelSerializer):
    request_user = serializers.ReadOnlyField(source='request_user.username')
    request_user_id = serializers.ReadOnlyField(source='request_user.id')
    next_user = serializers.ReadOnlyField(source='next_user.username')
    ksmgee = KsmgEESerializer(many=True, read_only=True)
    class Meta:
        model = Ksmg
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','ksmg_next_user','ksmg')
