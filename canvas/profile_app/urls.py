from django.urls import path

from canvas.profile_app.views import *

urlpatterns = (
    path('<str:username>/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('edit/banner/<int:pk>', EditBannerView.as_view(), name='edit banner'),

    path('manage_payments/<str:username>/', ManagePaymentMethodsView.as_view(), name='manage payments'),
    path('payment/add/', AddPaymentMethodView.as_view(), name='add payment'),
    path('payment/edit/<int:pk>/', EditPaymentView.as_view(), name='edit payment'),
    path('payment/delete/<int:pk>/', DeletePaymentView.as_view(), name='delete payment'),

    path('manage_addresses/<str:username>/', ManageAddressesView.as_view(), name='manage addresses'),
    path('address/add/', AddAddressView.as_view(), name='add address'),
    path('address/edit/<int:pk>/', EditAddressView.as_view(), name='edit address'),
    path('address/delete/<int:pk>/', DeleteAddressView.as_view(), name='delete address'),
)
