from django.shortcuts import render
from django.views.generic import TemplateView
from users.utils import validate_format_password
from django.contrib import messages
from django.contrib.auth.models import User

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