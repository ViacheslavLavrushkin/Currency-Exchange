from currency.models import ContactUs
from currency.models import Rate
from currency.models import Bank

from django import forms


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'type',
            'sale',
            'buy',
            'sale',
            'bank',
        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = (
            'name',
            'url',
        )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'object',
            'email_from',
            'subject',
            'message',
        )
