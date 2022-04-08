from django.urls import path
from .views import (
    GetBlogContent
)

urlpatterns = [
    path('get-blog-content', GetBlogContent.as_view(), name='get_blog_content'),
]   
