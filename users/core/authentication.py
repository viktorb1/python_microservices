import jwt, datetime
from app import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from core.models import User, UserToken
from django.utils import timezone


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("jwt")
        is_ambassador = "api/ambassador" in request.path

        if not token:
            return None

        payload = JWTAuthentication.get_payload(token)

        user = User.objects.get(pk=payload["user_id"])

        if (is_ambassador and payload["scope"] != "ambassador") or (
            not is_ambassador and payload["scope"] != "admin"
        ):
            raise exceptions.AuthenticationFailed("Invalid Scope!")

        if user is None:
            raise exceptions.AuthenticationFailed("User not found!")

        if not UserToken.objects.filter(
            user_id=user.id, token=token, expired_at__gt=timezone.now()
        ).exists():
            raise exceptions.AuthenticationFailed("unauthenticated")

        return (user, None)

    @staticmethod
    def get_payload(token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("unauthenticated")

        return payload

    @staticmethod
    def generate_jwt(id, scope):
        payload = {
            "user_id": id,
            "scope": scope,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
        }

        return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
