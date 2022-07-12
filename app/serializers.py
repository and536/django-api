from dataclasses import fields
from app.models import Paciente, Exame
from rest_framework import serializers


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'name', 'age', 'address', 'created_at']

class ExameSerializer(serializers.ModelSerializer):
    # patient = PacienteSerializer().instance
    class Meta:
        model = Exame
        fields = ['id', 'name_professional', 'date_exam', 'weight', 'height', 'patient', 'created_at']