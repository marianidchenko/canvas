from django.urls import path
from canvas.profile_app.views import AddPaymentMethodView, ProfileDetailsView, EditPaymentView, \
    ManagePaymentMethodsView, DeletePaymentView, AddAddressView, ManageAddressesView, EditAddressView, DeleteAddressView

urlpatterns = (
    path('', ProfileDetailsView.as_view(), name='profile details'),

    path('manage_payments/', ManagePaymentMethodsView.as_view(), name='manage payments'),
    path('add_payment/', AddPaymentMethodView.as_view(), name='add payment'),
    path('edit_payment/<int:pk>/', EditPaymentView.as_view(), name='edit payment'),
    path('delete_payment/<int:pk>/', DeletePaymentView.as_view(), name='delete payment'),

    path('add_address/', AddAddressView.as_view(), name='add address'),
    path('manage_addresses/', ManageAddressesView.as_view(), name='manage addresses'),
    path('edit_address/<int:pk>/', EditAddressView.as_view(), name='edit address'),
    path('delete_address/<int:pk>/', DeleteAddressView.as_view(), name='delete address'),

)