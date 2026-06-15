from django import forms
from . import models
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone')

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de Erro',
                code='invalid'
            )
        )

        return super().clean()
