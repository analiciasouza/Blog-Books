from django.db import models

# Modelo de Categoria
class Tag(models.Model):
      name = models.CharField(max_length=255)
      