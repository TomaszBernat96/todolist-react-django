from django.contrib import admin
from .models import Item
# Register your models here.

admin.AdminSite.empty_value_display = '-'

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ('user', 'title', 'add_timestamp', 'is_done', 'done_timestamp')