from rest_framework import routers
from api_core.viewsets_api.school_viewset import SchoolViewSet

router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)