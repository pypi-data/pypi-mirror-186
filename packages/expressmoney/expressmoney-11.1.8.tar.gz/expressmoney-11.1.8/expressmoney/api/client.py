__all__ = ('ApiTasks', 'ApiRequest')

from typing import Union

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from expressmoney import requests

User = get_user_model()


class ApiTasks(requests.Tasks):
    """Google Cloud Tasks Client for Django user"""

    def __init__(self,
                 service: str = 'default',
                 path: str = '/',
                 user: Union[None, int, User] = None,
                 location: str = 'europe-west1',
                 queue: str = 'attempts-1',
                 in_seconds: int = None):
        user = None if user is None else user if isinstance(user, User) else User.objects.get(pk=user)
        access_token = RefreshToken.for_user(user).access_token if user is not None else None
        super().__init__(service=service,
                         path=path,
                         access_token=access_token,
                         location=location,
                         queue=queue,
                         in_seconds=in_seconds
                         )


class ApiRequest(requests.Request):
    """HTTP Client for Django user"""

    def __init__(self,
                 service: str = None,
                 path: str = '/',
                 query_params: Union[None, dict] = None,
                 user: Union[None, int, User] = None,
                 timeout: tuple = (30, 30),
                 ):
        user = None if user is None else user if isinstance(user, User) else User.objects.get(pk=user)
        access_token = RefreshToken.for_user(user).access_token if user is not None else None
        super().__init__(service=service,
                         path=path,
                         query_params=query_params,
                         access_token=access_token,
                         timeout=timeout
                         )

    @staticmethod
    def _get_iap_client_id():
        return settings.IAP_CLIENT_ID
