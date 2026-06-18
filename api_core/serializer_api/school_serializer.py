from adminmike.models import School, Course, Student
from rest_framework import serializers

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'