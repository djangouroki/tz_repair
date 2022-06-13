from django.db import models


class Works(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name="Работа"
    )
    type_repair = models.ForeignKey(
        "repairs.TypeRepair", verbose_name="Тип работы",
        on_delete=models.CASCADE, null=True, blank=True,
        related_name="works"
    )

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"

    def __str__(self):
        return self.name
