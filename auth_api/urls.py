from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, profile, login

router = DefaultRouter()
router.register(r"user", CustomUserViewSet)

urlpatterns = [
    path("user/profile/", profile, name="profile"),
    path("user/login/", login, name="login"),
    path("", include(router.urls)),
]
