from django.core.management.base import BaseCommand
from repairs.management.commands.test_data import (
    locomotives_data, parts_data, users_data, types_repair_data,
    places_work_data,
)
from repairs.models import Locomotive, Parts, PlacesToWork, TypeRepair, Works
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()


class Command(BaseCommand):
    help = 'Наполнить БД тестовыми данными'

    def handle(self, *args, **options):
        for locomotive in locomotives_data:
            Locomotive.objects.get_or_create(name=locomotive)

        for part in parts_data:
            Parts.objects.get_or_create(name=part)

        for place in places_work_data:
            PlacesToWork.objects.get_or_create(name=place)

        for user_data in users_data:
            User.objects.get_or_create(
                email=user_data[3],
                defaults={
                    "first_name": user_data[0],
                    "last_name": user_data[1],
                    "username": user_data[2],
                    "role": user_data[4],
                    "password": make_password(user_data[5]),
                }
            )

        for type_ in types_repair_data:
            type_repair, _ = TypeRepair.objects.get_or_create(
                name=type_.get("name"),
                hour=type_.get("hour")
            )
            for work in type_["work"]:
                Works.objects.get_or_create(
                    name=work,
                    type_repair=type_repair
                )
