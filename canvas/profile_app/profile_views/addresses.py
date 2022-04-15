from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from canvas.profile_app.forms import AddAddressForm, EditAddressForm, DeleteAddressForm
from canvas.profile_app.models import Address


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

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('manage addresses', username=self.request.user.profile.username)
        else:
            return super(DeleteAddressView, self).post(request, *args, **kwargs)