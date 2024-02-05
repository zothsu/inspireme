from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Feed, Post
from django.views.generic.edit import CreateView
# import requests

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def feed_index(request):
  return render(request, 'feed/index.html')

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

def posts_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'feed/index.html', { 
    'post': post
   })

class PostCreate(CreateView):
  model = Post
  fields = '__all__'