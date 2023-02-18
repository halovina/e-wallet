from django.urls import path
from account import views

urlpatterns = [
    path('account-type', views.AccountType.as_view(), name='account_type_index'),
    path('account-type/create', views.AccountTypeCreate.as_view(), name='account_type_create'),
    path('account-type/edit/<int:account_id>', views.AccountTypeEdit.as_view(), name='account_type_edit'),
    path('account-type/delete/<int:account_id>', views.accountTypeDelete, name='account_type_delete'),
]