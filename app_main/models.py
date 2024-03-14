from django.db import models
from utils.main_upload_paths import *

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RPGSystem(models.Model):
    name = models.CharField(max_length=255)
    ilustration = models.ImageField(upload_to=systems_ilustration_upload)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name