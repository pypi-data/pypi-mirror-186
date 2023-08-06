from django.db import models
from django.db.models.query import QuerySet


__all__ = (
    'SoftRemovableManager',
    'SoftRestorableManager',
)


class SoftRemovableQuerySet(QuerySet):
    def delete(self):
        self.update(is_removed=True)


class SoftRestorableQuerySet(SoftRemovableQuerySet):
    def restore(self):
        self.update(is_removed=False)


class SoftRemovableManager(models.Manager):
    def _get_query_set(self):
        return SoftRemovableQuerySet(self.model, using=self._db)

    def get_all(self):
        return self._get_query_set()

    def get_queryset(self):
        return self._get_query_set().filter(is_removed=False)

    def removed(self):
        return self._get_query_set().filter(is_removed=True)


class SoftRestorableManager(SoftRemovableManager):
    def _get_query_set(self):
        return SoftRestorableQuerySet(self.model, using=self._db)
