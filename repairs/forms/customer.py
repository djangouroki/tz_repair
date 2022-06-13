from django import forms

from repairs.models import Repair, Locomotive


class CustomerForm(forms.ModelForm):

    description = forms.CharField(
        label="Описание поломки",
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    locomotive = forms.ModelChoiceField(
        label="Выберите локомотив",
        widget=forms.Select(attrs={"class": "form-control"}),
        queryset=Locomotive.objects.all()
    )

    class Meta:
        model = Repair
        fields = ('description', 'locomotive')
