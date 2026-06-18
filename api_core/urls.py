from django.urls import path, include
from .routers import *

urlpatterns = [
    path('api-v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]