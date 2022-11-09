import factory.fuzzy

from repairs.data import locomotives_data, parts_data, places_work_data
from repairs.models import (
    Locomotive, Parts, PlacesToWork, Repair, Status, TypeRepair,
    Works,
)


class TypeRepairFactory(factory.django.DjangoModelFactory):
    """Фабрика для типов ремонта"""

    name = factory.fuzzy.FuzzyChoice(['ТО2', 'ТО3', 'ТР1', 'ТР2', 'ТР3'])
    hour = factory.fuzzy.FuzzyInteger(5, 12)

    class Meta:
        model = TypeRepair


class WorksFactory(factory.django.DjangoModelFactory):
    """Фабрика работ"""

    name = factory.fuzzy.FuzzyChoice(places_work_data)
    type_repair = factory.SubFactory(TypeRepairFactory)

    class Meta:
        model = Works


class PlacesToWorkFactory(factory.django.DjangoModelFactory):
    """Фабрика для мест ремонта"""

    name = factory.fuzzy.FuzzyChoice(places_work_data)

    class Meta:
        model = PlacesToWork


class PartsFactory(factory.django.DjangoModelFactory):
    """Фабрика запчастей"""

    name = factory.fuzzy.FuzzyChoice(parts_data)

    class Meta:
        model = Parts


class LocomotiveFactory(factory.django.DjangoModelFactory):
    """Фабрика локомотивов"""

    name = factory.fuzzy.FuzzyChoice(locomotives_data)

    class Meta:
        model = Locomotive


class RepairFactory(factory.django.DjangoModelFactory):
    """Фабрика заявки"""

    description = factory.Faker('paragraph')
    status = factory.fuzzy.FuzzyChoice(Status.values)
    places_to_work = factory.SubFactory(PlacesToWorkFactory)
    locomotive = factory.SubFactory(LocomotiveFactory)
    type_repair = factory.SubFactory(TypeRepairFactory)

    class Meta:
        model = Repair

    @factory.post_generation
    def parts(self, create, parts, **kwargs):
        if create and parts:
            self.parts.add(*parts)

    @factory.post_generation
    def works(self, create, works, **kwargs):
        if create and works:
            self.works.add(*works)

    @factory.post_generation
    def users(self, create, users, **kwargs):
        if create and users:
            self.users.add(*users)
