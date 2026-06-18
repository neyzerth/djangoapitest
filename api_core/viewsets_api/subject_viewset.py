from adminmike.models import Subject
from api_core.serializer_api.subject_serializer import SubjectSerializer
from rest_framework import viewsets

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
