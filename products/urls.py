from django.urls import path

from .views import ProductDetailView


urlpatterns = [
    path('/product/<int:product_id>', ProductDetailView.as_view())
]