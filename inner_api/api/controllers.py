from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from todolist_engine.models import Item
from inner_api.serializers.todo_item_serializer import ItemSerializer

class ItemsManager(ListCreateAPIView, DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
