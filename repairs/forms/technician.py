from django import forms

from repairs.models import PlacesToWork, Repair, Status, TypeRepair


class TechnicianForm(forms.ModelForm):
    """Форма для работы с заявкой для техника"""

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    time_to_work = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control'})
    )
    places_to_work = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=PlacesToWork.objects.all()
    )
    type_repair = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=TypeRepair.objects.all()
    )
    status = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
        choices=[
            item for item in Status.choices if item[0] == 'CONFIRMED'
        ]
    )

    class Meta:
        model = Repair
        fields = (
            'description',
            'time_to_work',
            'places_to_work',
            'type_repair',
            'status',
        )
