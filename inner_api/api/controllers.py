from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from todolist_engine.models import Item

class ItemsManager(ListCreateAPIView, DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
