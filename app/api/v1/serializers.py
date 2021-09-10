from currency.models import Bank, ContactUs, Rate

from django.conf import settings
from django.core.mail import send_mail

from rest_framework import serializers


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_from',
            'subject',
            'message',
            'created',
        )


class ContactUsSendMailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_from',
            'subject',
            'message',
            'created',
        )

    def create(self, validate_data):

        instance = super(ContactUsSendMailSerializer, self).create(validate_data)
        send_mail(
            'From Django API created instance {}'.format(instance.pk),
            f'''
            'From': {validate_data['email_from']}
            'Topic': {validate_data['subject']}
            'Message': {validate_data['message']}
            ''',
            settings.EMAIL_HOST_USER,
            [validate_data['email_from']],
            fail_silently=False,
        )
        return instance


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = (
            'id',
            'name',
            'code_name',
        )


class RateSerializer(serializers.ModelSerializer):
    bank_object = BankSerializer(source='bank', read_only=True)

    class Meta:
        model = Rate
        fields = (
            'id',
            'type',
            'buy',
            'sale',
            'bank_object',
            'bank',
        )

        extra_kwargs = {
            'bank': {'write_only': True},
        }


class RateDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = (
            'id',
            'type',
            'buy',
            'sale',
            'created',
            'bank',
        )


class RateObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'type',
            'buy',
            'sale',
            'created',
        )


class BankDetailsSerializer(serializers.ModelSerializer):
    rate_set = RateObjectSerializer(many=True)

    class Meta:
        model = Bank
        fields = (
            'id',
            'name',
            'url',
            'original_url',
            'created',
            'bank_logo',
            'rate_set',
        )


class BankObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = (
            'id',
            'name',
            'code_name',
        )
