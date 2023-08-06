from itertools import chain

from django.db import transaction, models
from django.utils.translation import gettext_lazy as _

from .managers import SoftRemovableManager, SoftRestorableManager


__all__ = (
    'SoftRemovableManager',
    'SoftRestorableManager',
    'SoftRemovableModel',
    'SoftRestorableModel',
)


class BaseSoftRemovableModel(models.Model):
    is_removed = models.BooleanField(_('Removed'), default=False, editable=False)

    objects = SoftRemovableManager()

    class Meta:
        abstract = True

    @property
    def _soft_remover_unique_fields(self):
        unique_fields = getattr(self._meta, '_soft_remover_unique_fields', None)
        if unique_fields is not None:
            return unique_fields

        def _transform_unique_fields(fields):
            if not fields:
                return set()
            if isinstance(fields[0], str):
                return {tuple(fields)}
            return set(fields)

        fieldset = _transform_unique_fields(self._meta.unique_together)
        fieldset |= _transform_unique_fields(getattr(getattr(self, 'MetaSoftRemover', None), 'restore_together', []))
        fieldset |= {(f.name,) for f in self._meta.fields if f.unique and not f.primary_key}
        if isinstance(self, SoftRemovableModel):
            fieldset = {tuple(set(f) - {'remver'}) for f in fieldset}
        self._meta._soft_remover_unique_fields = tuple(fieldset)
        return self._meta._soft_remover_unique_fields

    def delete(self, using=None, keep_parents=False):
        self.is_removed = True
        self.save(using=using)


class SoftRemovableModel(BaseSoftRemovableModel):
    remver = models.PositiveIntegerField(_('Removal version'), default=0, editable=False)

    objects = SoftRemovableManager()

    class Meta:
        abstract = True

    @property
    def _soft_remover_filter(self):
        return {field: getattr(self, field) for field in set(chain(*self._soft_remover_unique_fields))}

    def delete(self, using=None, keep_parents=False):
        self.remver = self.__class__.objects.removed().filter(**self._soft_remover_filter).count() + 1
        super().delete(using=using, keep_parents=keep_parents)


class SoftRestorableModel(BaseSoftRemovableModel):
    objects = SoftRestorableManager()

    class Meta:
        abstract = True

    @property
    def _soft_remover_filter(self):
        q = models.Q()
        for fields in self._soft_remover_unique_fields:
            cq = models.Q()
            for field in fields:
                cq &= models.Q(**{field: getattr(self, field)})
            q |= cq
        return q

    def restore(self, using=None):
        self.is_removed = False
        self.save(using=using)

    @transaction.atomic
    def save(self, *args, **kwargs):
        if not self.pk:
            _soft_remover_filter = self._soft_remover_filter
            if _soft_remover_filter:
                try:
                    instance = self.__class__.objects.removed().filter(_soft_remover_filter).order_by('-pk').first()
                    if instance is None:
                        raise self.DoesNotExist()
                    instance.restore()
                    self.pk = instance.pk
                    return
                except self.DoesNotExist:
                    ...
        super().save(*args, **kwargs)
