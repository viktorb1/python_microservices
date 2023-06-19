from django.urls import path, include
from .views import (
    RegisterAPIView,
    LoginAPIView,
    UserAPIView,
    LogoutView,
    ProfileInfoAPIView,
    ProfilePasswordAPIView,
)

urlpatterns = [
    path("register", RegisterAPIView.as_view()),
    path("login", LoginAPIView.as_view()),
    path("user", UserAPIView.as_view()),
    path("logout", LogoutView.as_view()),
    path("users/info", ProfileInfoAPIView.as_view()),
    path("users/password", ProfilePasswordAPIView.as_view()),
]
