from django.db import models

# Create your models here.
class Dictionary(models.Model):

     eng = models.CharField('English', max_length=128)
     uz = models.CharField('Uzbek', max_length=128)
