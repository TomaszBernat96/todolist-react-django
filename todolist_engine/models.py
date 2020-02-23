from django.db import models

class Item(models.Model):
    class Meta:
        verbose_name='Todo item'
        verbose_prular_name='Todo items'
        ordering=['-add_timestamp']

    description = models.TextField()
    add_timestamp = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
