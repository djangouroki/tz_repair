from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from repairs.factories import RepairFactory
from repairs.forms.master import MasterForm
from repairs.models import Parts, Repair, Status
from users.models import Role

User = get_user_model()


class TestDetailView(TestCase):
    """Тестируем view детальной заявки"""

    url_name = 'repairs:detail'

    def setUp(self) -> None:
        """Создаем заявки"""
        self.customer = User.objects.filter(role=Role.CUSTOMER).first()
        self.technician = User.objects.filter(role=Role.TECHNICIAN).first()
        self.master = User.objects.filter(role=Role.MASTER).first()
        RepairFactory.create_batch(
            3, status=Status.CREATED, users=(self.customer,)
        )
        RepairFactory.create_batch(
            3, status=Status.CONFIRMED, users=(
                self.customer, self.technician, self.master
            )
        )

    def test_post_update_repair(self):
        """Тестируем обновление заявки"""
        parts = Parts.objects.values_list('id', flat=True).order_by('id')[:3]
        worker = User.objects.filter(
            role=Role.WORKER
        ).values_list('id', flat=True).order_by('id')[:1]
        payload = {
            'status': Status.READY_TO_WORK,
            'parts': parts,
            'users': worker
        }

        repair = Repair.objects.filter(status__in=[Status.CONFIRMED]).first()
        self.client.force_login(self.master)

        path = reverse(self.url_name, kwargs={'pk': repair.pk})
        response = self.client.post(path, data=payload)

        repair.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(repair.status, Status.READY_TO_WORK)
        self.assertEqual(
            list(repair.parts.values_list('id', flat=True).order_by('id')),
            list(parts)
        )
        self.assertIn(
            worker[0],
            list(
                repair.users.values_list('id', flat=True).order_by('id')
            ),
        )

    def test_post_repair_404(self):
        """При обновлении не существующей заявки возвращается 404"""
        self.client.force_login(self.master)

        path = reverse(self.url_name, kwargs={'pk': 999999})
        response = self.client.post(path)

        self.assertEqual(response.status_code, 404)

    def test_get_detail_repair_master(self):
        """Получение детальной информации о заявке мастером"""
        self.client.force_login(self.master)
        repair = Repair.objects.filter(
            status__in=[
                Status.CONFIRMED,
                Status.TESTS,
            ]
        ).first()

        path = reverse(self.url_name, kwargs={'pk': repair.pk})
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['repair'], repair)
        self.assertIsInstance(response.context['form'], MasterForm)

    def test_get_detail_repair_customer(self):
        """Получение детальной информации о заявке клиентом"""
        self.client.force_login(self.customer)
        repair = Repair.objects.filter(users=self.customer).first()

        path = reverse(self.url_name, kwargs={'pk': repair.pk})
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['repair'], repair)
        self.assertEqual(response.context['form'], None)

    def test_get_repair_404(self):
        """При запросе не существующей заявки возвращается 404"""
        self.client.force_login(self.customer)

        path = reverse(self.url_name, kwargs={'pk': 999999})
        response = self.client.get(path)

        self.assertEqual(response.status_code, 404)
