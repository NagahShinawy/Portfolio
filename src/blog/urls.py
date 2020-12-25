from django.urls import path
from .views import blog_home, post_details

app_name = 'blog'

urlpatterns = [
    path('blog/', blog_home, name='blog_home'),
    path('blog/posts/', blog_home, name='blog_home'),
    path('blog/posts/<str:slug>', post_details, name='post_details'),
]