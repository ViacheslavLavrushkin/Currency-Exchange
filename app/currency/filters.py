import django_filters
from django.forms import DateInput
from django_filters.widgets import RangeWidget

from currency.models import ContactUs, Rate

from django_filters import rest_framework as filters, DateFromToRangeFilter


class RateFilter(filters.FilterSet):
    created_gte = django_filters.DateFilter(
        field_name='created',
        lookup_expr='date__gte',
        widget=DateInput(attrs={'type': 'date'}),
    )
    created_lte = django_filters.DateFilter(
        field_name='created',
        lookup_expr='date__lte',
        widget=DateInput(attrs={'type': 'date'}),
    )

    class Meta:
        model = Rate
        fields = {
            'buy': ['exact', ],
            'sale': ['exact', ],
            # 'created': ['lte', 'gte', ],
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
