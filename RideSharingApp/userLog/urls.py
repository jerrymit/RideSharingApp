from django.urls import path

from . import views

app_name = 'userLog'
urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
]