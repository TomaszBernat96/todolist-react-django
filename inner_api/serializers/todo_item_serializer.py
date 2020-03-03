from rest_framework import serializers
from todolist_engine.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CreateDeleteItemSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(min_value=1)
    
    class Meta:
        model = Item
        fields = ('user_id', 'title', 'description', 'add_timestamp', 'is_done', 'done_timestamp')
