from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
# import requests

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def feed_index(request):
  posts = Post.objects.all()
  return render(request, 'feed/index.html', {
    'posts': posts
  })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
      
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def posts_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'main_app/post_details.html', { 
    'post': post
  })

class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  fields = '__all__'
  success_url = '/feed'
  
class PostDelete(LoginRequiredMixin, DeleteView):
  model = Post
  success_url = '/feed'
  
class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  fields = ['comment', 'brand', 'price', 'url', 'image']
  
  def get_queryset(self):
    sort = self.request.GET.get('sort', '')
    if sort:
      return Post.objects.order_by(sort)
    else:
      return Post.objects.all()
   
class CommentCreate(LoginRequiredMixin, CreateView):
  model = Comment
  fields = '__all__'

  def form_valid(self, form):
    post_id = self.kwargs['post_id']
    form.instance.post_id = post_id
    super().form_valid(form)
    return redirect('post_detail', post_id=post_id)