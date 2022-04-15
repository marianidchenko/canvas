from django.urls import path

from canvas.main.views import *

urlpatterns = (
    path('', IndexView.as_view(), name='index'),

    path('browse/', AllProductsView.as_view(), name='browse'),
    path('browse/<str:username>/', ProfileProductViews.as_view(), name='profile products'),
    path('search/', SearchProductsView.as_view(), name='search'),

    path('details/<int:pk>', ProductDetailView.as_view(), name='details'),

    path('manage_products/', ManageProductsView.as_view(), name='manage products'),
    path('product/add/', CreateProductView.as_view(), name='add product'),
    path('product/edit/<int:pk>/', EditProductView.as_view(), name='edit product'),
    path('product/restock/<int:pk>/', RestockProductView.as_view(), name='restock product'),
    path('product/delete/<int:pk>/', DeleteProductView.as_view(), name='delete product'),

    path('add_to_cart/<int:pk>/', add_to_cart_view, name='add to cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/remove/<int:pk>/', RemoveCartItemView.as_view(), name='remove cartitem'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('purchased/', PurchasedView.as_view(), name='purchased'),
)
