from django.contrib.auth import get_user_model

from apps.common.base_serializer import BaseSerializer
from .models import GroceryList, GroceryItems

User = get_user_model()


class GroceryListSerializer(BaseSerializer):
    class Meta:
        model = GroceryList
        fields = ('__all__')


class GroceryItemsSerializer(BaseSerializer):
    class Meta:
        model = GroceryItems
        fields = ('__all__')
