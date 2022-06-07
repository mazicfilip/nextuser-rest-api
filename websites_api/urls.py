from django.urls import path, include
from rest_framework import routers

from websites_api.views import WebsiteViewSet

router = routers.DefaultRouter()

router.register('websites', WebsiteViewSet)

urlpatterns = [
    path('', include(router.urls))
]
