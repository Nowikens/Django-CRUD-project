from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm
# Create your views here.



class IndexView(LoginRequiredMixin, ListView, FormMixin):
    model = Post
    form_class = PostForm
    template_name = 'posts/index.html'
    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        
        return ListView.get(self, request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        
        if self.form.is_valid():
            self.new_post = self.form.save(commit=False)
            self.author = self.request.user
            self.new_post.author = self.author
            self.new_post.save()
            
        return self.get(request, *args, **kwargs)
        
        
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['form'] = PostForm()
        context['posts'] = Post.objects.all().order_by('-date_posted')
        return context



class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/update.html'
    fields = ['content',]


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = None
    
    def get_success_url(self):
        return reverse('posts:index')
    
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    
    
    
    
    
    
    
    
    
    
    