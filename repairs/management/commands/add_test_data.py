from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from repairs.data import (
    locomotives_data, parts_data, places_work_data,
    types_repair_data,
)
from repairs.factories import (
    LocomotiveFactory, PartsFactory,
    PlacesToWorkFactory, TypeRepairFactory, WorksFactory,
)
from users.factories import UserFactory
from users.models import Role

User = get_user_model()


class Command(BaseCommand):
    help = 'Наполнить БД тестовыми данными'

    def handle(self, *args, **options):
        """Создание данных в БД"""
        for locomotive in locomotives_data:
            LocomotiveFactory(name=locomotive)
        for part in parts_data:
            PartsFactory(name=part)
        for places_work in places_work_data:
            PlacesToWorkFactory(name=places_work)
        for types_repair_dict in types_repair_data:
            type_repair = TypeRepairFactory(
                name=types_repair_dict['name'], hour=types_repair_dict['hour']
            )
            for work in types_repair_dict['work']:
                WorksFactory(name=work, type_repair=type_repair)
        for role in Role.choices:
            name = role[0].lower()
            UserFactory(
                username=f'user_{name}1',
                email=f'test_{name}1@mail.ru',
                password=make_password('11111')
            )
            UserFactory(
                username=f'user_{name}2',
                email=f'test_{name}2@mail.ru',
                password=make_password('11111')
            )
