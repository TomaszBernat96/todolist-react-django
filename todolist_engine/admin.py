from django.contrib import admin
from todolist_engine.models import Item

# Register your models here.


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('is_done', 'add_timestamp', 'todo_title', 'done_timestamp')
