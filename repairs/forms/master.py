from django import forms
from django.contrib.auth import get_user_model

from repairs.models import Parts, Repair, Status
from users.models import Role

User = get_user_model()


class MasterForm(forms.ModelForm):
    """Форма для мастера"""

    parts = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        queryset=Parts.objects.all()
    )
    users = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        queryset=User.objects.filter(role=Role.WORKER)
    )
    status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[
            item for item in Status.choices if item[0] in (
                'READY_TO_WORK', 'RE_REPAIR', 'VERIFICATION'
            )
        ]
    )

    class Meta:
        model = Repair
        fields = (
            'parts',
            'users',
            'status',
        )
