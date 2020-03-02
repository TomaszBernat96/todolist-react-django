from django.urls import include, path
from inner_api.api.controllers import ItemsManager

urlpatterns = [
    path('items', ItemsManager.as_view(), name='itemsManager')
]