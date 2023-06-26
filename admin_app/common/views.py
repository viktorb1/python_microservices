import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import exceptions

from .services import UserService


# Create your views here.
class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        data["is_ambassador"] = "api/ambassador" in request.path
        res = UserService.post("register", data=data)
        return Response(res.json(), status=res.status_code)


class LoginAPIView(APIView):
    def post(self, request):
        data = request.data
        data["scope"] = "ambassador" if "api/ambassador" in request.path else "admin"
        print(data)

        res = UserService.post("login", data=data)
        print(res)

        if res.status_code != 200:
            return Response(json.loads(res._content), status=res.status_code)

        jwt = res.json().get("jwt", "")
        response = Response()
        response.set_cookie(key="jwt", value=jwt, httponly=True)
        response.data = {"message": "success"}
        return response


class UserAPIView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        # if "api/ambassador" in request.path:
        #     data["revenue"] = user.revenue

        # instead of calling UserService directly, we can use our middleware
        # res = UserService.get("user", headers=request.headers)
        return Response(request.user_ms.json(), status=request.user_ms.status_code)


class LogoutView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        res = UserService.post("logout", headers=request.headers)
        response = Response()
        response.delete_cookie(key="jwt")
        response.data = {"message": "success"}
        return response


class ProfileInfoAPIView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def put(self, request):
        print("THE TYPE IS", type(request.headers))
        res = UserService.put("users/info", data=request.data, headers=request.headers)
        return Response(res.json(), status=res.status_code)


class ProfilePasswordAPIView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def put(self, request):
        res = UserService.put(
            "users/password", data=request.data, headers=request.headers
        )
        return Response(res.json(), status=res.status_code)
