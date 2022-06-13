from django.db import models


class PlacesToWork(models.Model):

    name = models.CharField(max_length=100, verbose_name="Место ремонта")

    class Meta:
        verbose_name = "Место ремонта"
        verbose_name_plural = "Места ремонта"

    def __str__(self):
        return self.name
