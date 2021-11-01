from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import PersonViewSet

router = routers.DefaultRouter()
router.register(r"femalemereen", PersonViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
