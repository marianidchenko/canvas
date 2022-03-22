from django.urls import path

from canvas.auth_app.views import UserRegistrationView, UserLoginView, UserLogoutView, JustLoggedOutView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('logged_out/', JustLoggedOutView.as_view(), name='logged out')
)