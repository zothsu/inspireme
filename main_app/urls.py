from django.urls import path
from . import views
    
urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('feed/', views.feed_index, name='index'),
    path('posts/<int:post_id>/', views.posts_detail, name='post_detail'), 
    path('posts/create/', views.PostCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('posts/<int:post_id>/addcomment/', views.CommentCreate.as_view(), name='comment'),
    path('posts/<int:post_id>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
  ]