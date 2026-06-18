from adminmike.models import School
from api_core.serializer_api.school_serializer import SchoolSerializer
from rest_framework import viewsets

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer