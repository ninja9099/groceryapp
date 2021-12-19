
from rest_framework.routers import DefaultRouter

from .views import GroceryListViewSet

urlpatterns = []

router = DefaultRouter()
router.register('', GroceryListViewSet, basename='grocery-list')
urlpatterns += router.urls
