from django.urls import path
from .views import ProductListView, FilterListView, ProductDetailView, PairWithView, BelowInfoView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/filter', FilterListView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/<int:product_id>/pairing', PairWithView.as_view()),
    path('/<int:product_id>/belowinfo', BelowInfoView.as_view())

]
