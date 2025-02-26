from django.contrib import admin

# Register your models here.
from .models.posts import Post
from .models.tag import Tag
from .models.category import Category

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)