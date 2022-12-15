from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(deleted__isnull=True)


class SoftDeleteMixin(models.Model):

    deleted = models.DateTimeField(null=True, default=None, blank=True)
    deleted_by = models.ForeignKey(
        UserModel, related_name='+', null=True, default=None, blank=True,
        on_delete=models.SET_NULL,
    )

    stored = SoftDeleteManager()
    objects = models.Manager()

    def soft_delete(self, user=None):
        self.deleted = timezone.now()
        self.deleted_by_id = user.id
        self.save()

    def undelete(self):
        self.deleted = None
        self.deleted_by = None
        self.save()

    class Meta:
        abstract = True
