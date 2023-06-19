from core.models import User
from rest_framework.views import APIView
from common.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import generics, mixins

from common.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import User, Product, Link, Order
from .serializers import ProductSerializer, LinkSerializer, OrderSerializer
from django.core.cache import cache


# Create your views here.
class AmbassadorAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        ambassadors = User.objects.filter(is_ambassador=True)
        serializer = UserSerializer(ambassadors, many=True)
        return Response(serializer.data)


class ProductGenericAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)

        return self.list(request)

    def post(self, request):
        response = self.create(request)
        for key in cache.keys("*"):
            if "products_frontend" in key:
                cache.delete(key)
        cache.delete("products_backend")
        return response

    def put(self, request, pk=None):
        response = self.partial_update(request, pk)
        for key in cache.keys("*"):
            if "products_frontend" in key:
                cache.delete(key)
        cache.delete("products_backend")
        return response

    def delete(self, request, pk=None):
        response = self.destroy(request, pk)
        for key in cache.keys("*"):
            if "products_frontend" in key:
                cache.delete(key)
        cache.delete("products_backend")
        return response


class LinkAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        links = Link.objects.filter(user=pk)
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)


class OrderAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(complete=True)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
