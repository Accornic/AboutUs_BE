from datetime import datetime
from email.policy import default
from venv import create
from django.db import models
import uuid
from mdeditor.fields import MDTextField
import datetime

# Create your models here.
class BlogContent(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200,unique=True,blank=False,null=False)
    content = MDTextField()
    slug = models.SlugField(max_length = 200)
    created_by = models.CharField(max_length=200,unique=True,blank=False,null=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)