from rest_framework import serializers
from currency.models import Rate, Bank


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
            'buy',
            'sale',
            'type',
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
            'buy',
            'sale',
            'created',
            'type',
            'bank',
        )