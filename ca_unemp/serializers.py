from rest_framework import serializers
from .models import Unemployment

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unemployment
        fields = '__all__'
