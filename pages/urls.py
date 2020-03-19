from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('Add_user', views.Add_user, name='Add_user'),
    path('Dash_board', views.Dash_board, name='Dash_board'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('map', views.map, name='map'),
    path('add_attendace', views.add_attendace, name='add_attendace'),
    path('add_checkout', views.add_checkout, name='add_checkout'),
]