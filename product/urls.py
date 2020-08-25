from django.urls import path
from .views import ProductsView, ProductDetailView, PairWithView, BelowInfoView

urlpatterns = [
    path('', ProductsView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/<int:product_id>/pairing', PairWithView.as_view()),
    path('/<int:product_id>/belowinfo', BelowInfoView.as_view())

]
