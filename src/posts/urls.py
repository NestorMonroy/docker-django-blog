
from django.urls import path
from src.posts.views import posts as post_views

app_name = 'posts'

urlpatterns = [
    path('', post_views.AdListView.as_view() , name='all'),
]