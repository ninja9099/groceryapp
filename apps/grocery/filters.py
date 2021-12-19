from django_filters import rest_framework as filters

from apps.grocery.constants import GroceryListStatus
from apps.grocery.models import GroceryList, GroceryItems


class GroceryListFilter(filters.FilterSet):
    due_date_from = filters.DateTimeFilter(field_name='due_date', lookup_expr='gte')
    due_date_to = filters.DateTimeFilter(field_name='due_date', lookup_expr='lte')
    due_date = filters.DateFilter(field_name='due_date')
    status = filters.ChoiceFilter(choices=GroceryListStatus.get_choices())

    class Meta:
        model = GroceryList
        fields = ['user', 'due_date']


class GroceryItemsFilter(filters.FilterSet):
    class Meta:
        model = GroceryItems
        fields = ['name', 'quantity', 'unit_of_measure','status']
