from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from canvas.profile_app.forms import AddPaymentForm, EditPaymentForm, DeletePaymentForm
from canvas.profile_app.models import PaymentMethod


class AddPaymentMethodView(LoginRequiredMixin, generic_views.CreateView):
    model = PaymentMethod
    form_class = AddPaymentForm
    template_name = 'profile/payment_add.html'

    def get_success_url(self):
        return reverse_lazy('manage payments', kwargs={'username': self.request.user.profile.username})

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super(AddPaymentMethodView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('manage payments', kwargs={'username': self.request.user.profile.username})
        else:
            return super(AddPaymentMethodView, self).post(request, *args, **kwargs)


class ManagePaymentMethodsView(LoginRequiredMixin, generic_views.ListView):
    model = PaymentMethod
    template_name = 'profile/manage_payment_methods.html'

    def get_queryset(self):
        return PaymentMethod.objects.filter(profile=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        context['payment_methods'] = PaymentMethod.objects.filter(profile=self.request.user.profile)
        return context


class EditPaymentView(LoginRequiredMixin, generic_views.UpdateView):
    model = PaymentMethod
    form_class = EditPaymentForm
    template_name = 'profile/payment_edit.html'

    def get_success_url(self):

        return reverse_lazy('manage payments', kwargs={'username': self.request.user.profile.username})

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('manage payments',  username=self.request.user.profile.username)
        else:
            return super(EditPaymentView, self).post(request, *args, **kwargs)


class DeletePaymentView(LoginRequiredMixin, generic_views.DeleteView):
    model = PaymentMethod
    form_class = DeletePaymentForm
    template_name = 'profile/payment_delete.html'

    def get_success_url(self):
        return reverse_lazy('manage payments', kwargs={'username': self.request.user.profile.username})

    # Create a delete and cancel button
    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('manage payments', username=self.request.user.profile.username)
        else:
            return super(DeletePaymentView, self).post(request, *args, **kwargs)