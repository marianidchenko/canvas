from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy
from django.views import generic as generic_views
from django.contrib.auth import views as auth_views
from canvas.auth_app.forms import UserRegistrationForm


UserModel = get_user_model()


class UserRegistrationView(generic_views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


class UserLogoutView(auth_views.LogoutView):
    pass


class JustLoggedOutView(generic_views.TemplateView):
    template_name = 'index.html'
