from django.urls import path

from canvas.main.views import IndexView, CreateProductView, AllProductsView, CartView, add_to_cart_view, \
    ProductDetailView, CheckoutView, PurchasedView, ManageProductsView, EditProductView, RestockProductView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('browse/', AllProductsView.as_view(), name='browse'),
    path('details/<int:pk>', ProductDetailView.as_view(), name='details'),
    path('product/add/', CreateProductView.as_view(), name='add product'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('purchased/', PurchasedView.as_view(), name='purchased'),
    path('add_to_cart/<int:pk>/', add_to_cart_view, name='add to cart'),
    path('manage_products/', ManageProductsView.as_view(), name='manage products'),
    path('product/edit/<int:pk>', EditProductView.as_view(), name='edit product'),
    path('product/restock/<int:pk>', RestockProductView.as_view(), name='restock product'),
)
