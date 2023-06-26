from django.urls import path, include
from .views import (
    RegisterAPIView,
    LoginAPIView,
    UserAPIView,
    LogoutView,
    ProfileInfoAPIView,
    ProfilePasswordAPIView,
    UsersAPIView,
)

urlpatterns = [
    path("register", RegisterAPIView.as_view()),
    path("login", LoginAPIView.as_view()),
    path("user/<str:scope>", UserAPIView.as_view()),
    path("logout", LogoutView.as_view()),
    path("users/info", ProfileInfoAPIView.as_view()),
    path("users/password", ProfilePasswordAPIView.as_view()),
    path("users", UsersAPIView.as_view()),
    path("users/<str:pk>", UsersAPIView.as_view()),
]
