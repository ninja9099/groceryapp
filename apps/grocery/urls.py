
from rest_framework.routers import DefaultRouter

from .views import GroceryListViewSet, GroceryItemsViewSet

urlpatterns = []

router = DefaultRouter()
router.register('grocery-list', GroceryListViewSet, basename='grocery-list')
router.register('grocery-items', GroceryItemsViewSet, basename='grocery-items')
urlpatterns += router.urls
