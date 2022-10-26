from django import forms

from repairs.models import Repair, Status


class WorkerForm(forms.ModelForm):
    """Форма для слесаря"""

    status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[
            item for item in Status.choices if item[0] in (
                'PROGRESS', 'TESTS'
            )
        ]
    )

    class Meta:
        model = Repair
        fields = (
            'status',
        )