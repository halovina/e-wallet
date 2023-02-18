from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import AccountType as AccountTypeModel
from django.utils.text import slugify
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


class AccountType(TemplateView):
    template_name = 'account/index.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['acc'] = AccountTypeModel.objects.all().order_by('-id')
        return context
    
    
class AccountTypeCreate(TemplateView):
    template_name = 'account/form.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['h_title'] = 'Tambah Data'
        return context
    
    def post(self, *args, **kwargs):
        try:
            accountTypeName = self.request.POST.get('account_type_name')
            AccountTypeModel(
                type_name = accountTypeName,
                slug = slugify(accountTypeName)
            ).save()
            messages.success(self.request, "Data berhasil ditambahkan")
        except Exception as e:
            messages.error(self.request, str(e))
        return HttpResponseRedirect('/acc/account-type')
    
    
class AccountTypeEdit(TemplateView):
    template_name = 'account/form.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_context_data(self, account_id, **kwargs):
        context = super().get_context_data(**kwargs)
        context['h_title'] = 'Edit Data'
        context['acc'] = AccountTypeModel.objects.get(id=account_id)
        return context
    
    def post(self, *args, **kwargs):
        try:
            account_id = self.request.POST.get('account_id')
            accountTypeName = self.request.POST.get('account_type_name')
            acc = AccountTypeModel.objects.get(id=account_id)
            acc.type_name = accountTypeName
            acc.save()
            messages.success(self.request, "Data berhasil diubah")
        except Exception as e:
            messages.error(self.request, str(e))
        return HttpResponseRedirect('/acc/account-type')
    

@login_required    
def accountTypeDelete(request, account_id):
    try:
        AccountTypeModel.objects.filter(id=account_id).delete()
        messages.success(request, "Data berhasil di hapus")
    except Exception as e:
        messages.error(request, str(e))
    return HttpResponseRedirect('/acc/account-type') 
    
    
    