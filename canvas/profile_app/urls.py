from django.urls import path
from canvas.profile_app.views import AddPaymentMethodView, ProfileDetailsView, EditPaymentView, \
    ManagePaymentMethodsView, DeletePaymentView, AddAddressView, ManageAddressesView, EditAddressView, DeleteAddressView

urlpatterns = (
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),

    path('manage_payments/', ManagePaymentMethodsView.as_view(), name='manage payments'),
    path('payment/add/', AddPaymentMethodView.as_view(), name='add payment'),
    path('payment/edit/<int:pk>/', EditPaymentView.as_view(), name='edit payment'),
    path('payment/delete/<int:pk>/', DeletePaymentView.as_view(), name='delete payment'),

    path('address/add/', AddAddressView.as_view(), name='add address'),
    path('manage_addresses/', ManageAddressesView.as_view(), name='manage addresses'),
    path('address/edit/<int:pk>/', EditAddressView.as_view(), name='edit address'),
    path('address/delete/<int:pk>/', DeleteAddressView.as_view(), name='delete address'),

)