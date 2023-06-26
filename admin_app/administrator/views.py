from core.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins

from core.models import User, Product, Link, Order
from .serializers import ProductSerializer, LinkSerializer, OrderSerializer
from django.core.cache import cache
from common.services import UserService


# Create your views here.
class AmbassadorAPIView(APIView):
    def get(self, request):
        users = UserService.get("users")
        return Response(filter(lambda a: a["is_ambassador"] == 1, users))


class ProductGenericAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
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
    def get(self, request, pk=None):
        links = Link.objects.filter(user=pk)
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)


class OrderAPIView(APIView):
    def get(self, request):
        orders = Order.objects.filter(complete=True)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
