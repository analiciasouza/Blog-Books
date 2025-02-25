# Mapeamento blog.com/view
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home_view ),
    path('admin/', admin.site.urls),
]
