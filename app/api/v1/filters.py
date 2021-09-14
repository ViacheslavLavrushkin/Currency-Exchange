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


class ContactUsFilter(filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = {
            'email_from': ('icontains', 'istartswith', 'iendswith', 'exact'),
            'subject': ('icontains', 'istartswith', 'iendswith', 'exact'),
            'message': ('icontains', 'istartswith', 'iendswith', 'exact'),
            'created': ('date', 'lte', 'gte'),
        }
