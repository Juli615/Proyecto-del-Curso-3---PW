from rest_framework import serializers

from .models import Estudiante

class EstudianteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['nombre','apellido','email','fecha_matricula','promedio']
