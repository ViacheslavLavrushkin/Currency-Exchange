from currency.models import ContactUs, Rate

from django_filters import rest_framework as filters


class RateFilter(filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'buy': ('lt', 'lte', 'gt', 'gte', 'exact',),
            'sale': ('lt', 'lte', 'gt', 'gte', 'exact',),
            'type': ('in',),
            'created': ('date', 'lte', 'gte',),
        }
