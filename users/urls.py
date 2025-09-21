from django.contrib.auth import views as view_auth
from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('', views.register, name='register'),
    path('logout/', views.logouts, name='logouts'),
    path('login/', view_auth.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('updateProfile/<int:id>', views.updateProfile, name='updateProfile')
]