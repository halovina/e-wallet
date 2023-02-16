from django.urls import path
from home import views

urlpatterns = [
    path('dashboard', views.DashboardView.as_view(), name='page_dashboard'),
]