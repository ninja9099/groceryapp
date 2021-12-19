from __future__ import unicode_literals, absolute_import
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    created_ts = models.DateTimeField(_("Created Date"), auto_now_add=True)
    updated_ts = models.DateTimeField(_("Last Updated Date"), auto_now=True)
    created_by = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_created_related', null=True, blank=True,
                                   on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_updated_related', null=True,
                                   blank=True,
                                   on_delete=models.CASCADE)

    class Meta:
        abstract = True
