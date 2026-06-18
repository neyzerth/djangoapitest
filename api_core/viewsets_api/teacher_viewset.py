from adminmike.models import Teacher
from api_core.serializer_api.teacher_serializer import TeacherSerializer
from rest_framework import viewsets

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
