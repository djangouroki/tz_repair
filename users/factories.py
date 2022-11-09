import factory.fuzzy
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):

    email = factory.Sequence(lambda n: f'test_email_{n}@mail.ru')
    username = factory.Sequence(lambda n: f'test_username_{n}')

    class Meta:
        model = User
