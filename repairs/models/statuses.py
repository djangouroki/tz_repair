from django.db import models


class Status(models.TextChoices):
    CREATED = 'CREATED', 'Новая заявка от клиента'
    CONFIRMED = 'CONFIRMED', 'Подтверждена техником'
    READY_TO_WORK = 'READY_TO_WORK', 'Готова к работе'
    PROGRESS = 'PROGRESS', 'В работе'
    VERIFICATION = 'VERIFICATION', 'Ремонт выполнен'
    TESTS = 'TESTS', 'На тестировании'
    RE_REPAIR = 'RE_REPAIR', 'На доработку'


def statuses_for_list_worker():
    return [
        Status.READY_TO_WORK, Status.PROGRESS, Status.RE_REPAIR
    ]


def statuses_for_list_master():
    return [
        Status.CONFIRMED, Status.TESTS
    ]


def statuses_for_list_technician():
    return [
        Status.CREATED, Status.VERIFICATION
    ]
