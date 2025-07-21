from django.urls import path
from . import views

app_name = 'blog'  # Optional, but recommended for namespacing
urlpatterns = [
    path('', views.post_list, name='post_list'),  # Example URL pattern
    # Add other URL patterns for your blog app here
]