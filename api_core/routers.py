from rest_framework import routers
from api_core.viewsets_api.school_viewset import SchoolViewSet
from api_core.viewsets_api.teacher_viewset import TeacherViewSet
from api_core.viewsets_api.student_viewset import StudentViewSet

router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)