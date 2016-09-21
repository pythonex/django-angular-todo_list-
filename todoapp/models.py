from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Todo(models.Model):
    title           = models.CharField(max_length=75)
    description     = models.TextField()
    is_completed    = models.BooleanField(default=False)

    def __str__(self):
        return self.title