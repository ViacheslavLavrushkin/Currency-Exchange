import uuid

from accounts.models import User
from accounts.tasks import send_registration_email
from accounts.tokens import account_activation_token


from django import forms
from django.conf import settings
from django.urls import reverse


class SignUpForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password1'] != cleaned_data['password2']:
                # self.add_error('password1', 'Passwords do not match.')
                raise forms.ValidationError('Passwords do not match.')
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        # instance.username = self.cleaned_data['email']
        instance.username = str(uuid.uuid4())
        instance.is_active = False
        # instance.password = self.cleaned_data['password1']  -- WRONG
        instance.set_password(self.cleaned_data['password1'])
        token_key = account_activation_token.make_token(instance)  # noqa

        if commit:
            instance.save()

        body = f"""
        Activate Your Account
        {settings.DOMAIN}{reverse('account:activate-account', args=(instance.username, ))}
        """
        send_registration_email.delay(body, instance.email)
        return instance
