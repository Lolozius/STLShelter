from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name='page/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='page/index.html'),
        name='logout'
    ),
]
