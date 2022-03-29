from django.urls import path

from canvas.main.views import IndexView, CreateProductView, AllProductsView, CartView, add_to_cart_view

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('browse/', AllProductsView.as_view(), name='browse'),
    path('product/add/', CreateProductView.as_view(), name='add product'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add_to_cart/<int:pk>/', add_to_cart_view, name='add to cart')
)
