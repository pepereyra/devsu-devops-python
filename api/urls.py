from django.urls import path
from rest_framework import routers

from .health import liveness, readiness
from .views import UserViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet, "users")

urlpatterns = [
    path("health/live/", liveness),
    path("health/ready/", readiness),
] + router.urls