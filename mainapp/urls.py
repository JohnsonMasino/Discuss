from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('', views.Home, name='home'),
    path('login/', views.Login, name='login'),
    path('signup/', views.SignUp, name='signup'),
    path('register/', RegisterView.as_view(), name='register'),
]