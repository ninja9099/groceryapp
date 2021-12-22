from django.db.models import Case, When
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters as search_filters, status
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from apps.grocery.constants import GroceryItemStatus, GroceryListStatus
from apps.grocery.filters import GroceryListFilter, GroceryItemsFilter
from apps.grocery.models import GroceryList, GroceryItems
from apps.grocery.permissions import IsFriedOrOwner
from apps.grocery.serializer import GroceryListSerializer, GroceryItemsSerializer


class GroceryListViewSet(viewsets.ModelViewSet):
    queryset = GroceryList.objects.all().order_by('-created_ts')
    serializer_class = GroceryListSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAdminUser | IsAuthenticatedOrReadOnly,)
    filter_backends = [search_filters.SearchFilter, DjangoFilterBackend]
    filterset_class = GroceryListFilter
    search_fields = ['user__username', 'status', 'due_date', 'reminder_interval']

    def get_permissions(self):
        permission_classes = [IsFriedOrOwner, ]
        if self.action == 'list':
            permission_classes = [IsAuthenticated, IsFriedOrOwner]
        if self.action == 'update':
            permission_classes = [IsFriedOrOwner, ]
        return [permission() for permission in permission_classes]

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super(GroceryListViewSet, self).update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_data.update({"user": request.user.id})
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['get'])
    def grocery_items(self, request, pk=None):
        grocery_list = self.get_object()
        grocery_items = GroceryItems.objects.filter(grocery_list=grocery_list)
        serializer = GroceryItemsSerializer(instance=grocery_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GroceryItemsViewSet(viewsets.ModelViewSet):
    queryset = GroceryItems.objects.all()
    serializer_class = GroceryItemsSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAdminUser | IsAuthenticatedOrReadOnly,)
    filter_backends = (search_filters.SearchFilter, DjangoFilterBackend)
    filterset_class = GroceryItemsFilter
    search_fields = ('name', 'quantity', 'unit_of_measure', 'status')

    def get_permissions(self):
        permission_classes = [IsFriedOrOwner, ]
        if self.action == 'list':
            permission_classes = [IsAuthenticated, IsFriedOrOwner]
        if self.action == 'update':
            permission_classes = [IsFriedOrOwner, ]
        return [permission() for permission in permission_classes]

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        item = super(GroceryItemsViewSet, self).update(request, *args, **kwargs)
        grocery_list_object = self.get_object().grocery_list
        grocery_list_pending_items = grocery_list_object.grocery_items\
            .filter(status=GroceryItemStatus.Pending).exists()
        if not grocery_list_pending_items:
            grocery_list_object.status = GroceryListStatus.Completed
        elif 'status' in request.data:
            grocery_list_object.status = GroceryListStatus.Partial
        grocery_list_object.save()
        return item
