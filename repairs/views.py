from django.shortcuts import render
from django.views import View
from django.views.generic import FormView, ListView
from django.contrib.auth import get_user_model
from repairs.forms.customer import CustomerForm
from repairs.models import Status, Repair
from repairs.models.statuses import (
    statuses_for_list_technician,
    statuses_for_list_master, statuses_for_list_worker,
)
from users.models import Role

User = get_user_model()


class DetailRepair(View):

    template_name = "detail.html"

    def get(self, request, pk):
        return render(request, self.template_name)


class ListRepair(ListView):
    template_name = "repairs.html"
    model = Repair
    paginate_by = 5

    def get_queryset(self):
        """Воозвращаем заявки для пользователей по статусу заявки"""
        queryset = []
        user: User = self.request.user

        if user.role == Role.CUSTOMER:
            queryset = Repair.objects.filter(users=user)

        elif user.role == Role.TECHNICIAN:
            queryset = Repair.objects.filter(
                status__in=statuses_for_list_technician()
            )

        elif user.role == Role.MASTER:
            queryset = Repair.objects.filter(
                status__in=statuses_for_list_master()
            )

        elif user.role == Role.WORKER:
            queryset = Repair.objects.filter(
                status__in=statuses_for_list_worker()
            )
        return queryset


class CreateRepair(FormView):
    template_name = 'create_repair.html'
    form_class = CustomerForm
    success_url = '/repairs/'

    def form_valid(self, form):
        repair = form.save()
        repair.status = Status.CREATED
        repair.save()
        repair.users.add(self.request.user)
        return super().form_valid(form)
