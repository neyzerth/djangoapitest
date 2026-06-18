from adminmike.models import Career
from api_core.serializer_api.career_serializer import CareerSerializer
from rest_framework import viewsets

class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
