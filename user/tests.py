import jwt, json, bcrypt

from django.test import TestCase, Client

from .models        import User
from product.models import Product
from order.models   import Order
from my_settings    import SECRET_KEY, ALGORITHM

class SignUpTest(TestCase):
    def test_signup_success(self):
        client = Client()

        user = {
            'first_name' : 'amy',
            'last_name'  : 'Lee',
            'birthday'   : '2000.01.01',
            'email'      : 'amy@example.com',
            'password'   : '1234qwer'
        }

        response = client.post('/user/signup', json.dumps(user), content_type='application/json')
        user = User.objects.filter(email='amy@example.com').exists()

        self.assertIs(user, True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'SIGNUP_SUCCESS!'})

    def test_signup_fail_by_password(self):
        client = Client()

        user = {
            'first_name' : 'amy',
            'last_name'  : 'Lee',
            'birthday'   : '2000.01.01',
            'email'      : 'amy@example.com',
            'password'   : '1234a'
        }

        response = client.post('/user/signup', json.dumps(user), content_type='application/json')
        user = User.objects.filter(email='amyexample.com').exists()

        self.assertIs(user, False)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message': 'INVALID_PASSWORD'})

    def test_signup_fail_by_duplicated_email(self):
        client = Client()

        User.objects.create(
            email      = 'amy@example.com',
            first_name = 'amy',
            last_name  = 'Lee',
            birthday   = '2000-01-01',
            password   = '1234qwer'
        )

        user = {
            'first_name' : 'amy',
            'last_name'  : 'Lee', 
            'birthday'   : '2000.01.01',
            'email'      : 'amy@example.com',
            'password'   : '1234qwer'
        }

        response = client.post('/user/signup', json.dumps(user), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message': 'USER_ALREADY_EXISTS'})

class SignInTest(TestCase):
    def setUp(self):
        User.objects.create(
            email      = 'amy@example.com',
            first_name = 'amy',
            last_name  = 'Lee',
            birthday   = '2000-01-01',
            password   = bcrypt.hashpw('1234qwer'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_signin_success(self):
        client = Client()

        data = {
            'email'    : 'amy@example.com',
            'password' : '1234qwer'
        }

        response = client.post('/user/signin', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_signin_fail_by_wrong_password(self):
        client = Client()

        data = {
            'email' : 'amy@example.com',
            'password' : '1111qwer'
        }

        response = client.post('/user/signin', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message':'UNAUTHORIZED'})

    def test_signin_fail_by_key_error(self):
        client = Client()
        
        data = {
            'cmail' : 'amy@example.com',
            'password' : '1234qwer'
        }

        response = client.post('/user/signin', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message':'KEY_ERROR'})

    def test_signin_fail_by_wrong_email(self):
        client = Client()

        data = {
            'email' : 'emma@example.com',
            'password' : '1234qwer'
        }

        response = client.post('/user/signin', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message': 'UNAUTHORIZED'})
