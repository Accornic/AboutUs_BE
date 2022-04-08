from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import (
    BlogContent
)

# Register your models here.
admin.site.register(BlogContent, MarkdownxModelAdmin)