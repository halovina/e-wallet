from django.urls import path
from users import views

urlpatterns = [
    path('register', views.RegisterUser.as_view(), name='register_new_user')
]