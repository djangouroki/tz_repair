from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from users.forms import UserCreationForm

User = get_user_model()


class TestRegisterView(TestCase):
    """Тестируем view регистрации пользователя"""

    def test_get(self):
        """Получение формы регистрации"""
        response = self.client.get(reverse('register'))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], UserCreationForm)

    def test_post_errors_form(self):
        """Тестируем регистрацию с ошибкой"""

        payload = {
            'username': 'username',
            'email': 'test_email@mail.ru',
            'password1': '11111',
        }

        response = self.client.post(reverse('register'), data=payload)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], UserCreationForm)
        self.assertIn('password2', response.context['form'].errors)

    def test_post_ok(self):
        """Тестируем что пользователь зарегистрировался"""

        email = 'test_email@mail.ru'

        payload = {
            'username': 'username',
            'email': email,
            'password1': 'L;fyuj123123',
            'password2': 'L;fyuj123123',
        }

        response = self.client.post(reverse('register'), data=payload)

        user = User.objects.get(email=email)

        self.assertEqual(user.email, email)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(user.is_authenticated)
