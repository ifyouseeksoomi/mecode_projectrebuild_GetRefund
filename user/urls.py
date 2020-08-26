from django.urls import path
from .views import SignUpView, SignInView, MyPageView, MyOrderView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/my-page', MyPageView.as_view()),
    path('/my-order', MyOrderView.as_view()),
    #path('/kakao-signup', KakaoLoginView.as_view())
]

