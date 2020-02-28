from django.db import models

# Create your models here.


class Item(models.Model):

    class Meta:
        verbose_name = 'Todo item'
        verbose_name_plural = 'Todo items'
        ordering = ['-add_timestamp', 'is_done']

    todo_description = models.TextField(null=False, blank=False)
    is_done = models.BooleanField(default=False)
    add_timestamp = models.DateTimeField(auto_now=True)
    done_timestamp = models.DateTimeField(null=False, blank=False)
