from django.urls import path
from canvas.profile_app.views import AddPaymentMethodView, ProfileDetailsView, EditPaymentView, \
    ManagePaymentMethodsView, DeletePaymentView

urlpatterns = (
    path('', ProfileDetailsView.as_view(), name='profile details'),
    path('add_payment/', AddPaymentMethodView.as_view(), name='add payment'),
    path('manage_payments/', ManagePaymentMethodsView.as_view(), name='manage payments'),
    path('edit_payment/<int:pk>/', EditPaymentView.as_view(), name='edit payment'),
    path('delete_payment/<int:pk>/', DeletePaymentView.as_view(), name='delete payment')
)