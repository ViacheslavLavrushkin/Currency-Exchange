from currency.models import Bank
from currency.models import ContactUs
from currency.models import Rate

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
            'code_name',
            'url',
            'original_url',
            'bank_logo'
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
