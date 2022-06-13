from django.db import models


class Parts(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name="Запчасть"
    )

    class Meta:
        verbose_name = "Запчасть"
        verbose_name_plural = "Запчасти"

    def __str__(self):
        return self.name
