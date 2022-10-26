from django.db import models
from django.urls import reverse


class Status(models.TextChoices):
    """Статусы для заявок"""
    CREATED = 'CREATED', 'Новая заявка от клиента'
    CONFIRMED = 'CONFIRMED', 'Подтверждена техником'
    READY_TO_WORK = 'READY_TO_WORK', 'Готова к работе'
    PROGRESS = 'PROGRESS', 'В работе'
    VERIFICATION = 'VERIFICATION', 'Ремонт выполнен'
    TESTS = 'TESTS', 'На тестировании'
    RE_REPAIR = 'RE_REPAIR', 'На доработку'


class Repair(models.Model):
    """Заявка на ремонт"""

    users = models.ManyToManyField(
        to="users.User", related_name="repairs",
        verbose_name="Участники заявки"
    )
    description = models.TextField(verbose_name="Описание поломки")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CREATED,
    )
    time_to_work = models.DateTimeField(
        verbose_name="Время начала ремонта", null=True, blank=True
    )
    places_to_work = models.ForeignKey(
        "repairs.PlacesToWork", related_name="place_repairs",
        on_delete=models.PROTECT, verbose_name="Место для ремонта",
        null=True, blank=True
    )
    locomotive = models.ForeignKey(
        "repairs.Locomotive", related_name="locomotive_repairs",
        on_delete=models.PROTECT, verbose_name="Локомотив",
        null=True, blank=True
    )
    type_repair = models.ForeignKey(
        "repairs.TypeRepair", related_name="type_repairs",
        on_delete=models.PROTECT, verbose_name="Тип ремонта",
        null=True, blank=True
    )
    works = models.ManyToManyField(
        to="repairs.Works", verbose_name="Работы", related_name="work_repairs"
    )
    parts = models.ManyToManyField(
        to="repairs.Parts", verbose_name="Запчасти",
        related_name="part_repairs"
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"Заявка - {self.id}, статус - {self.status}"

    def get_absolute_url(self):
        return reverse("repairs:detail", kwargs={"pk": self.pk})
