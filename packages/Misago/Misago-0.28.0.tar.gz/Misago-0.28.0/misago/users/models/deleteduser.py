from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class DeletedUser(models.Model):
    DELETED_BY_SELF = 1
    DELETED_BY_STAFF = 2
    DELETED_BY_SYSTEM = 3

    DELETED_BY_CHOICES = (
        (DELETED_BY_SELF, _("By self")),
        (DELETED_BY_STAFF, _("By staff")),
        (DELETED_BY_SYSTEM, _("By system")),
    )

    deleted_on = models.DateTimeField(default=timezone.now, db_index=True)
    deleted_by = models.PositiveIntegerField(choices=DELETED_BY_CHOICES, db_index=True)

    class Meta:
        ordering = ["-id"]
