from django.urls import reverse 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.



class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    
    def get_success_url(self):
        return reverse('posts:index')
    

    

    
    
class LoginUser(LoginView):
    template_name = 'accounts/login.html'


class LogoutUser(LogoutView, LoginRequiredMixin):
    template_name = 'posts/index.html'


class DeleteUser(DeleteView, LoginRequiredMixin):
    model = User
    template_name = 'accounts/confirm.html'
    def get_success_url(self):
        return reverse('posts:index')
