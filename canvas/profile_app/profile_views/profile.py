from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as generic_views

from canvas.common_tools.helpers import get_profile_by_username
from canvas.main.models import Product
from canvas.profile_app.forms import EditProfileForm, EditBannerForm
from canvas.profile_app.models import Profile


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