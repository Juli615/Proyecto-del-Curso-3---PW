from .models import Estudiante
from rest_framework import viewsets
from rest_framework.response import Response
from .serial import EstudianteSerializer

# Create your views here.
class EstudianteViewSet(viewsets.ModelViewSet):
    """
    API-REST endpoint para el modelo carro, admite GET,
    POST, PUT, PATCH, DELETE
    """

    queryset = Estudiante.objects.all().order_by('-fecha_matricula')
    serializer_class = EstudianteSerializer
