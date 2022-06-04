from django.db import models

# Create your models here.
class BreakoutModel(models.Model):
    room_number = models.CharField(max_length = 128)
    message = models.TextField()