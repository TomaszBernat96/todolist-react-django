from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=64)
    description = models.TextField(max_length=2048)
    add_timestamp = models.DateTimeField(default=timezone.now)
    done_timestamp = models.DateTimeField(blank=True)
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name='Todo item'
        verbose_name_plural='Todo items'
        ordering=['-add_timestamp', '-is_done']
        constraints = [
            models.UniqueConstraint(fields=['title', 'slug'], name='unique_title'),
            models.CheckConstraint(check=models.Q(done_timestamp__lt=models.F('add_timestamp')), name='done_ts_verification'),
        ]
