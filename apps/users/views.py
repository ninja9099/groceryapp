from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters as search_filters, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import (
    ListModelMixin as ListMixin,
    UpdateModelMixin as UpdateMixin,
    CreateModelMixin as CreateMixin
)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.users.permissions import IsAdminOrIsSelf
from apps.users.serializers import UserSerializer, PasswordSerializer, UserReadOnlySerializer

User = get_user_model()


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


class UserViewset(ListMixin, CreateMixin, UpdateMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser | IsAuthenticatedOrReadOnly,)
    filter_backends = (search_filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('first_name', 'last_name', 'username', 'email', 'about_me')
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['put'], permission_classes=[IsAdminOrIsSelf])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password1'])
            user.save()
            return Response({'message': _('Password has been set successfully')})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticatedOrReadOnly]
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser | IsAuthenticated | IsAdminOrIsSelf]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return self.serializer_class
        return UserReadOnlySerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request_data = request.data.copy()
        if 'email' in request_data.keys():
            request_data.pop('email')
        if 'username' in request_data.keys():
            request_data.pop('username')
        if instance.id != request.user.pk:
            raise ValidationError(_('Not allowed to update other users'))
        serializer = self.get_serializer(instance, data=request_data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
