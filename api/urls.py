from django.db.models import base
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import FemaleMereenSet, PersonSet

router = routers.DefaultRouter()
router.register(r"femalemereen", FemaleMereenSet, basename="femalemereen")
router.register(r"persons", PersonSet, basename="persons")

urlpatterns = [
    path("", include(router.urls)),
]
