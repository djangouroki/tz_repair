from django.db import models


class TypeRepair(models.Model):

    name = models.CharField(max_length=150, verbose_name="Тип ремонта")
    hour = models.PositiveSmallIntegerField(
        verbose_name="Часов для ремонта"
    )

    class Meta:
        verbose_name = "Тип ремонта"
        verbose_name_plural = "Типы ремонтов"

    def __str__(self):
        return self.name
