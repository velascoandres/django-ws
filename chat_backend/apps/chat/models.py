from django.db import models

# Create your models here.

class Mensaje(models.Model):
    de = models.CharField(max_length=30)
    para = models.CharField(max_length=30)
    contenido = models.CharField(max_length=30, blank=False)
