from django.urls import path

from canvas.main.views import IndexView, CreateProductView, AllProductsView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('browse/', AllProductsView.as_view(), name='browse'),
    path('product/add/', CreateProductView.as_view(), name='add product'),
)
