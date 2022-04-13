from creditcards import types
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from canvas.main.models import Product
from canvas.profile_app.forms import AddPaymentForm, EditPaymentForm, DeletePaymentForm, AddAddressForm, \
    EditAddressForm, DeleteAddressForm, EditProfileForm, EditBannerForm
from canvas.profile_app.helpers import get_profile_by_username, get_products_by_profile_username
from canvas.profile_app.models import PaymentMethod, Address, Profile


class ProfileDetailsView(generic_views.ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 3
    template_name = 'profile/profile_details.html'

    def get_queryset(self):
        profile = get_profile_by_username(self.kwargs['username'])
        return self.model.objects.filter(profile=profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = get_profile_by_username(self.kwargs['username'])
        return context


class EditProfileView(LoginRequiredMixin, generic_views.UpdateView):
    model = Profile
    template_name = 'profile/profile_edit.html'
    form_class = EditProfileForm

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'username': self.request.user.profile.username})


class EditBannerView(generic_views.UpdateView, LoginRequiredMixin):
    model = Profile
    template_name = 'profile/profile_edit.html'
    form_class = EditBannerForm

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'username': self.request.user.profile.username})


class AddPaymentMethodView(LoginRequiredMixin, generic_views.CreateView):
    model = PaymentMethod
    form_class = AddPaymentForm
    template_name = 'profile/payment_add.html'

    def get_success_url(self):
        return reverse_lazy('manage payments', kwargs={'username': self.request.user.profile.username})

    # Auto-add the profile relation
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


class AddAddressView(LoginRequiredMixin, generic_views.CreateView):
    model = Address
    form_class = AddAddressForm
    template_name = 'profile/address_add.html'

    def get_success_url(self):
        return reverse_lazy('manage addresses', kwargs={'username': self.request.user.profile.username})

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

    def get_success_url(self):
        return reverse_lazy('manage addresses', kwargs={'username': self.request.user.profile.username})


class DeleteAddressView(LoginRequiredMixin, generic_views.DeleteView):
    model = Address
    form_class = DeleteAddressForm
    template_name = 'profile/address_delete.html'

    def get_success_url(self):
        return reverse_lazy('manage addresses', kwargs={'username': self.request.user.profile.username})

    # Create a delete and cancel button
    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('manage addresses', username=self.request.user.profile.username)
        else:
            return super(DeleteAddressView, self).post(request, *args, **kwargs)
