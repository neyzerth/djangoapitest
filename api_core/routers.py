from rest_framework import routers
from api_core.viewsets_api.school_viewset import SchoolViewSet
from api_core.viewsets_api.teacher_viewset import TeacherViewSet
from api_core.viewsets_api.student_viewset import StudentViewSet
from api_core.viewsets_api.subject_viewset import SubjectViewSet
from api_core.viewsets_api.career_viewset import CareerViewSet

router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'careers', CareerViewSet)