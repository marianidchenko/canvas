from canvas.profile_app.models import PaymentMethod


def get_payment_methods(pk):
    payment_methods = PaymentMethod.objects.filter(profile_id=pk)
    return payment_methods
