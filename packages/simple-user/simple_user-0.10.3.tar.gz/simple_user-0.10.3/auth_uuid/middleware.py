from django.contrib.auth.middleware import AuthenticationMiddleware as DjangoAuthMiddleware
from django.contrib.auth.middleware import get_user
from django.contrib.auth import get_user_model
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.request import Request

from .token_authentication import OAuth2JSONWebTokenAuthentication


class AuthenticationMiddleware(DjangoAuthMiddleware):
    def process_request(self, request):
        request.user = get_user_model(
            ).objects.retrieve_remote_user_by_cookie(
                request.COOKIES)


def get_user_jwt(request):
    user = get_user(request)
    if user.is_authenticated:
        return user
    try:
        user_jwt = OAuth2JSONWebTokenAuthentication().authenticate(Request(request))
        if user_jwt is not None:
            return user_jwt[0]
    except Exception:
        pass
    return user


class OAuth2AuthenticationMiddleware(MiddlewareMixin):

    def process_request(self, request):
        assert hasattr(request, 'session'), (
            'The Django authentication middleware requires session middleware '
            'to be installed. Edit your MIDDLEWARE_CLASSES setting to insert '
            "'django.contrib.sessions.middleware.SessionMiddleware'."
        )
        if request.user.is_anonymous:
            request.user = SimpleLazyObject(lambda: get_user_jwt(request))


def get_user_jwt_(request):
    user = get_user(request)
    if user.is_authenticated:
        return user
    try:
        user_jwt = JSONWebTokenAuthentication().authenticate(Request(request))
        if user_jwt is not None:
            return user_jwt[0]
    except Exception:
        pass
    return user


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        assert hasattr(request, 'session'), (
            'The Django authentication middleware requires session middleware '
            'to be installed. Edit your MIDDLEWARE_CLASSES setting to insert '
            "'django.contrib.sessions.middleware.SessionMiddleware'."
        )
        if request.user.is_anonymous:
            request.user = SimpleLazyObject(lambda: get_user_jwt_(request))
