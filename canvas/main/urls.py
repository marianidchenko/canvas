from django.urls import path

from canvas.main.views import IndexView, CreateProductView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('product/add/', CreateProductView.as_view(), name='add product')
)