from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):

    class Meta:
        verbose_name = 'Todo item'
        verbose_name_plural = 'Todo items'
        ordering = ['-add_timestamp', 'is_done']

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    todo_title = models.TextField(null=False, blank=False)
    todo_description = models.TextField(null=False, blank=False)
    slug = models.CharField(max_length=256)
    add_timestamp = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    done_timestamp = models.DateTimeField(null=False, blank=False)
