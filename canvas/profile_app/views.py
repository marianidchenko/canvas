from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views
from canvas.profile_app.forms import AddPaymentForm, EditPaymentForm, DeletePaymentForm, AddAddressForm, \
    EditAddressForm, DeleteAddressForm
from canvas.profile_app.helpers import get_payment_methods
from canvas.profile_app.models import PaymentMethod, Address


class ProfileDetailsView(LoginRequiredMixin, generic_views.TemplateView):
    template_name = 'profile/profile_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome to Canvas'
        context['user'] = self.request.user
        payment_methods = get_payment_methods(self.request.user.pk)
        context['payment_methods'] = payment_methods
        return context


class AddPaymentMethodView(LoginRequiredMixin, generic_views.CreateView):
    model = PaymentMethod
    form_class = AddPaymentForm
    template_name = 'profile/payment_add.html'
    success_url = reverse_lazy('profile details')

    # Auto-add the profile relation
    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super(AddPaymentMethodView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('profile details')
        else:
            return super(AddPaymentMethodView, self).post(request, *args, **kwargs)


class ManagePaymentMethodsView(LoginRequiredMixin, generic_views.TemplateView):
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
    success_url = reverse_lazy('manage payments')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('manage payments')
        else:
            return super(EditPaymentView, self).post(request, *args, **kwargs)


class DeletePaymentView(LoginRequiredMixin, generic_views.DeleteView):
    model = PaymentMethod
    form_class = DeletePaymentForm
    template_name = 'profile/payment_delete.html'
    success_url = reverse_lazy('manage payments')

    # Create a delete and cancel button
    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('manage payments')
        else:
            return super(DeletePaymentView, self).post(request, *args, **kwargs)


class AddAddressView(LoginRequiredMixin, generic_views.CreateView):
    model = Address
    form_class = AddAddressForm
    template_name = 'profile/address_add.html'
    success_url = reverse_lazy('profile details')

    # Auto-add the profile relation
    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        if len(Address.objects.filter(profile=self.request.user.profile)) == 0:
            form.instance.primary = True
        return super(AddAddressView, self).form_valid(form)


class ManageAddressesView(LoginRequiredMixin, generic_views.TemplateView):
    model = Address
    template_name = 'profile/manage_addresses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        context['addresses'] = Address.objects.filter(profile=self.request.user.profile)
        return context


class EditAddressView(LoginRequiredMixin, generic_views.UpdateView):
    model = Address
    form_class = EditAddressForm
    template_name = 'profile/address_edit.html'
    success_url = reverse_lazy('profile details')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('manage addresses')
        else:
            return super(EditAddressView, self).post(request, *args, **kwargs)


class DeleteAddressView(LoginRequiredMixin, generic_views.DeleteView):
    model = Address
    form_class = DeleteAddressForm
    template_name = 'profile/address_delete.html'
    success_url = reverse_lazy('manage addresses')

    # Create a delete and cancel button
    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('manage addresses')
        else:
            return super(DeleteAddressView, self).post(request, *args, **kwargs)
