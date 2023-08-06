import requests

from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.encoding import smart_text


from rest_framework import exceptions
from rest_framework import status
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework_jwt.settings import api_settings


URL_USER_DATA = '{}{}?access_token='.format(
    settings.OAUTH_EXOPASS_DOMAIN,
    settings.OAUTH_EXOPASS_USER_URL,
)


def _sanitize_token(token):
    return token


def get_user_uuid_from_token(token):
    exo_uuid = None

    try:
        sanitized_token = _sanitize_token(token)
        response = requests.get(URL_USER_DATA + sanitized_token)    # NOSONAR
        assert (response.status_code == status.HTTP_200_OK)
        response_json = response.json()

        exo_uuid = response_json.get('exo_uuid')
        if not exo_uuid:
            user = get_user_model().objects.retrieve_remote_user_by_exo_pass_uuid(
                response_json.get('id')
            )
            exo_uuid = user.uuid

    except AssertionError:
        pass

    return exo_uuid


def get_jwt(request, raise_exceptions=False):

    auth = get_authorization_header(request).split()
    auth_header_prefix = api_settings.JWT_AUTH_HEADER_PREFIX.lower()

    if not auth:
        if api_settings.JWT_AUTH_COOKIE:
            return request.COOKIES.get(api_settings.JWT_AUTH_COOKIE)
        return None

    if smart_text(auth[0].lower()) != auth_header_prefix:
        return None

    if len(auth) == 1 and raise_exceptions:
            raise exceptions.AuthenticationFailed(
                'Invalid Authorization header. No credentials provided.'
            )
    elif len(auth) > 2 and raise_exceptions:
            raise exceptions.AuthenticationFailed(
                'Invalid Authorization header. Credentials string should not contain spaces.'
            )

    return auth[1].decode('utf-8')


class OAuth2JSONWebTokenAuthentication(BaseAuthentication):
    """
    Token based authentication using the JSON Web Token standard.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string specified in the setting
    `JWT_AUTH_HEADER_PREFIX`. For example:
        Authorization: JWT eyJhbGciOiAiSFMyNTYiLCAidHlwIj

    """

    def authenticate(self, request):
        """
        Returns a two-tuple of `User` and token if a valid signature has been
        supplied using JWT-based authentication.  Otherwise returns `None`.
        """

        jwt_value = self.get_jwt_value(request)
        if jwt_value is None:
            return None

        try:
            user_uuid = get_user_uuid_from_token(jwt_value)
            assert (user_uuid is not None)
            user = get_user_model().objects.get(uuid=user_uuid)

        except get_user_model().DoesNotExist:
            user = get_user_model().objects.retrieve_remote_user_by_exo_pass_uuid(user_uuid)

        except AssertionError:
            raise exceptions.AuthenticationFailed()

        return (user, None)

    def get_jwt_value(self, request):
        return get_jwt(request, raise_exceptions=True)


class OAuth2Backend:
    """
        Allows to login via email address and password. username
        is interpreted as email address.
    """
    supports_object_permissions = False
    supports_anonymous_user = True
    supports_inactive_user = True

    def authenticate(self, request, *args, **kwargs):    # NOSONAR
        user = None
        try:
            token = get_jwt(request)
            if token is None:
                return user

            user_uuid = get_user_uuid_from_token(token)
            assert (user_uuid is not None)

            user = get_user_model().objects.get(
                uuid=user_uuid,
                is_active=True
            )

        except get_user_model().DoesNotExist:
            pass

        except AssertionError:
            pass

        return user

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(uuid=user_id)
        except get_user_model().DoesNotExist:
            return None
