from django.urls import path
from . import views
    
urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('feed/', views.feed_index, name='index'),
  ]