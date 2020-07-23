from django.db import models

# Create your models here.
class Todo(models.Model):
    isDone = models.BooleanField(null=True)
    content = models.CharField(max_length=255)