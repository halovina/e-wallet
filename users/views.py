from django.shortcuts import render
from django.views.generic import TemplateView
from users.utils import validate_format_password, checkUserLogin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponseRedirect

# Create your views here.
class RegisterUser(TemplateView):
    template_name = 'user/register.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def post(self, *args, **kwargs):
        context = self.get_context_data()
        fullname = self.request.POST.get('fullname')
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        retypePassword = self.request.POST.get('retype-password')
        
        if password != retypePassword:
            messages.error(self.request, "Password dan Retype-password harus sama")
            return super(TemplateView, self).render_to_response(context)
            
        checkPw, msgPw = validate_format_password(password)
        if checkPw == False:
            messages.error(self.request, msgPw)
            return super(TemplateView, self).render_to_response(context)
            
        createNewUser(email, password, fullname)
        messages.success(self.request, "Register user sukses")
        return super(TemplateView, self).render_to_response(context)
    
def createNewUser(email, password, fullname):
    User.objects.create_user(
        username=email,
        email=email,
        password=password,
        first_name=fullname
    )
    

class LoginUser(TemplateView):
    template_name = 'user/login.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def post(self, *args, **kwargs):
        context = self.get_context_data()
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        is_authenticate, user = checkUserLogin(email, password)
        if is_authenticate:
            login(self.request, user)
            return HttpResponseRedirect('/home/dashboard')
        messages.error(self.request,"Periksa email dan password Anda")
        return super(TemplateView, self).render_to_response(context)
    
    
def userLogout(request):
    try:
        request.session.clear()
    except Exception as e:
        pass
    return HttpResponseRedirect('/accounts/login/')