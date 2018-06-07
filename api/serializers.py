from rest_framework import serializers, generics
from .models import Time, PrimeiraFase


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'

class PrimeiraFaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimeiraFase
        fields = '__all__'

