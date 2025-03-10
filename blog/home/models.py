from django.db import models

# Create your models here.

# Modelo de Categoria
class Category(models.Model):
      name = models.CharField(max_length=255)

# Modelo de post      
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True) 
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


