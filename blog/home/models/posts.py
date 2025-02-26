from django.db import models
from .category import Category
from .tag  import Tag
# Modelo de post      
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True) 
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag)
