from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='users'),
    path('add_register', views.add_register, name='add_register'),
    path('login_user', views.login_user, name='login_user'),
    path('change_password', views.change_password, name='change_password'),
    path('user_dashboard', views.user_dashboard, name='user_dashboard'),
]
