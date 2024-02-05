from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
app_name = 'app_users'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='app_users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout_view'),
]