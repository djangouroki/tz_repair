from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from repairs.factories import RepairFactory
from repairs.models import Repair, Status
from users.models import Role

User = get_user_model()


class TestListView(TestCase):
    """Тестируем view списка заявок"""

    def setUp(self) -> None:
        self.customer = User.objects.filter(role=Role.CUSTOMER).first()
        master = User.objects.filter(role=Role.MASTER).first()
        technician = User.objects.filter(role=Role.TECHNICIAN).first()
        worker = User.objects.filter(role=Role.WORKER).first()
        RepairFactory.create_batch(
            3, status=Status.CREATED, users=(self.customer, )
        )
        RepairFactory.create_batch(
            3, status=Status.CONFIRMED, users=(self.customer, technician)
        )
        RepairFactory.create_batch(
            3, status=Status.READY_TO_WORK,
            users=(self.customer, technician, master)
        )
        RepairFactory.create_batch(
            3, status=Status.PROGRESS,
            users=(self.customer, technician, master, worker)
        )
        RepairFactory.create_batch(
            3, status=Status.VERIFICATION,
            users=(self.customer, technician, master, worker)
        )
        RepairFactory.create_batch(
            3, status=Status.TESTS,
            users=(self.customer, technician, master, worker)
        )
        RepairFactory.create_batch(
            1, status=Status.RE_REPAIR,
            users=(self.customer, technician, master, worker)
        )

    def test_get_list_repairs_customer(self):
        """Получение списка заявок клиентом"""
        self.client.force_login(self.customer)
        response = self.client.get(reverse('repairs:list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context_data['paginator'].count,
            Repair.objects.filter(users=self.customer).count()
        )
