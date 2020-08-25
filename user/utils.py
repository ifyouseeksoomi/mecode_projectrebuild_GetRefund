import jwt, json

from django.http import JsonResponse
from my_settings import SECRET_KEY, ALGORITHM
from .models     import User

def login_check(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload      = jwt.decode(access_token, SECRET_KEY['secret'], ALGORITHM['algorithm'])
            user         = User.objects.get(id=payload['user_id'])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse ({'message': 'UNAUTHORIZED_TOKEN'}, status=401)
        except User.DoesNotExist:
            return JsonResponse ({'message': 'UNAUTHORIZED_USER'}, status=401)
        except KeyError:
            return JsonResponse ({'message': 'KEY_ERROR'}, status=400)
        return func(self, request, *args, **kwargs)
    return wrapper
