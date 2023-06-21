from django.urls import path, include
from .views import LinkAPIView, OrderAPIView, OrderConfirmAPIView, TestingView

urlpatterns = [
    path("links/<str:code>", LinkAPIView.as_view()),
    path("orders", OrderAPIView.as_view()),
    path("orders/confirm", OrderConfirmAPIView.as_view()),
    path("testing/", TestingView.as_view()),
]
