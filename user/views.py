import json,slee bcrypt, jwt, requests, datetime

from django.views           import View
from django.http            import (
    HttpResponse,
    JsonResponse
)
from django.core.validators import validate_email
from django.core.exceptions import (
    ValidationError,
    ObjectDoesNotExist
)
from .utils                 import login_check
from my_settings            import SECRET_KEY, ALGORITHM

from .models                import User


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            validate_email(data['email'])

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': 'USER_ALREADY_EXISTS'}, status=400)
            if len(data['password']) < 8:
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=400)

            User.objects.create(
                first_name = data['first_name'],
                last_name  = data['last_name'],
                birthday   = datetime.datetime.strptime(data['birthday'], '%Y.%m.%d').date(),
                email      = data['email'],
                password   = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8') 
                )
            return JsonResponse ({'message' : 'SIGNUP_SUCCESS!'}, status=200)
        except KeyError:
            return JsonResponse ({'message' : 'INVALID_KEY'}, status=400)
        except ValidationError:
            return JsonResponse ({'message' : 'VALIDATION_ERROR'}, status=400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email=data['email']).exists():
                user = User.objects.get(email=data['email'])
                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    access_token = jwt.encode({'user_id':user.id}, SECRET_KEY['secret'], ALGORITHM['algorithm']).decode('utf-8')
                    return JsonResponse({'access_token': access_token}, status=200)
                return JsonResponse({'message': 'UNAUTHORIZED'}, status=401)
            return JsonResponse({'message': 'UNAUTHORIZED'}, status=401)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except ValidationError:
            return JsonResponse({'message': 'INVALID_EMAIL'}, status=401)

class MyPageView(View):
    @login_check
    def get(self, request):
        return JsonResponse ({'first_name': request.user.first_name})

