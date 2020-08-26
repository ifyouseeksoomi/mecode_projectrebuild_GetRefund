from django.urls    import path
from .views         import CartItemView, RecommendationView, QuantityView

urlpatterns = [
    path('/cart', CartItemView.as_view()),
    path('/cart/recommendation', RecommendationView.as_view()),
    path('/cart/quantitytotal', QuantityView.as_view())
]

