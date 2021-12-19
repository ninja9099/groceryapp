from django_filters import rest_framework as filters

from apps.grocery.constants import GroceryListStatus
from apps.grocery.models import GroceryList


class GroceryListFilter(filters.FilterSet):
    due_date_from = filters.DateTimeFilter(field_name='due_date', lookup_expr='gte')
    due_date_to = filters.DateTimeFilter(field_name='due_date', lookup_expr='lte')
    status = filters.ChoiceFilter(choices=GroceryListStatus.get_choices())

    class Meta:
        model = GroceryList
        fields = ['user', 'due_date']
