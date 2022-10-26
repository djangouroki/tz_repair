from django.contrib.auth import get_user_model

from repairs.models import Status
from users.models import Role

User = get_user_model()


class RepairMixin:
    """Миксин для фильтрации заявок по роли пользователя"""

    @staticmethod
    def _get_repair_filter(user: User) -> dict:
        """Возвращаем фильтр для заявки для роли пользователя"""
        repair_filter = {
            Role.CUSTOMER: {
                'users': user
            },
            Role.TECHNICIAN: {
                'status__in': [
                    Status.CREATED,
                    Status.VERIFICATION,
                ]
            },
            Role.MASTER: {
                'status__in': [
                    Status.CONFIRMED,
                    Status.TESTS,
                ]
            },
            Role.WORKER: {
                'status__in': [
                    Status.RE_REPAIR,
                    Status.READY_TO_WORK,
                    Status.PROGRESS,
                ]
            }
        }
        return repair_filter.get(user.role)
