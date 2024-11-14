from django.db import models


class SoftDeleteMixin(models.Model):
    """Soft delete model mixin."""

    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
