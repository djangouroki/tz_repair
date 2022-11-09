from django.test import TestCase
from django.urls import reverse

from repairs.factories import LocomotiveFactory
from repairs.models import Repair
from users.factories import UserFactory
from users.models import Role


class TestCreateRepairView(TestCase):
    """Тестируем view создания заявки"""

    def test_create_repair_master(self):
        """Попытка создать заявку мастером"""

        payload = {
            'description': 'description',
            'locomotive': 1
        }
        master = UserFactory(role=Role.MASTER)
        self.client.force_login(master)

        response = self.client.post(reverse('repairs:create'), data=payload)

        self.assertTrue(response.status_code, 403)

    def test_create_repair_customer(self):
        """Создание заявки"""
        locomotive = LocomotiveFactory()
        description = 'description description description'
        payload = {
            'description': description,
            'locomotive': locomotive.id
        }
        customer = UserFactory()
        self.client.force_login(customer)

        response = self.client.post(reverse('repairs:create'), data=payload)

        repair = Repair.objects.filter(
            users=customer, description=description
        ).first()

        self.assertEqual(response.status_code, 302)
        self.assertTrue(repair)
        self.assertTrue(repair.locomotive_id, locomotive.id)

    def test_create_repair_anonymous(self):
        """Попытка создания формы анонимным пользователем"""
        locomotive = LocomotiveFactory()
        payload = {
            'description': 'description description description',
            'locomotive': locomotive.id
        }

        response = self.client.post(reverse('repairs:create'), data=payload)

        self.assertEqual(response.status_code, 302)
        self.assertIn('/users/login/', response.url)
