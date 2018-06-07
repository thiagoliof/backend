from rest_framework import serializers, generics
from .models import Time, PrimeiraFase


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'

class PrimeiraFaseSerializer(serializers.ModelSerializer):
    mandante = TimeSerializer()
    visitante = TimeSerializer()
    
    class Meta:
        model = PrimeiraFase
        fields = ('id', 'grupo', 'data', 'mandante', 'visitante', 'gol_mandante', 'gol_visitante')

