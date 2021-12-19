from django.urls import re_path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from apps.users.views import UserViewset

urlpatterns = [
    re_path(r'^api-token-auth/', obtain_jwt_token),
    re_path(r'^api-token-refresh/', refresh_jwt_token),
    re_path(r'^api-token-verify/', verify_jwt_token),
]

router = DefaultRouter()
router.register('users', UserViewset, basename='user')
urlpatterns += router.urls
