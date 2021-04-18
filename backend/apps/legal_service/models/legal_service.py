from django.db import models
from django.utils.translation import gettext as _
from apps.services.models import (
    DateCreatedMixin,
    DateUpdatedMixin,
)


class LegalService(
    DateUpdatedMixin,
    DateCreatedMixin,
    models.Model,
):
    """
    Модель Услуг
    """

    picture = models.ImageField(
        verbose_name=_("Картинка"), blank=True, null=True
    )
    title = models.CharField(
        verbose_name=_("Заголовок"), max_length=255, blank=True, null=True
    )
    description = models.TextField(
        verbose_name=_("Краткое описание"), blank=True, null=True
    )
    is_published_landing = models.BooleanField(
        verbose_name=_("Услуга опубликована"), default=False
    )

    class Meta:
        verbose_name = _("Услуга")
        verbose_name_plural = _("Услуги")
        ordering = ["title", "-date_created"]

    def __str__(self):
        title = "???" if self.title is None else self.title
        return (
            f"'{title}' "
            + f"(дата создания: {self.date_created}, "
            + f"дата последнего редактирования: {self.date_updated})"
        )
