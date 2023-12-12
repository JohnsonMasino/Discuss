from django.urls import path
from . import views
from .views import RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    path('', views.Home, name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('signup/', views.SignUp, name='signup'),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('register', RegisterView.as_view(), name='register'),
]