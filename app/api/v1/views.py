# from rest_framework import generics
from api.v1.filters import ContactUsFilter, RateFilter
from api.v1.paginators import ContactUsPagination, RatePagination
from api.v1.serializers import BankDetailsSerializer, BankSerializer, ContactUsSendMailSerializer, ContactUsSerializer,\
    RateDetailsSerializer, RateSerializer
from api.v1.throttle import AnonUserRateThrottle

from currency import choices
from currency.models import Bank, ContactUs, Rate

from django_filters import rest_framework as filters

from rest_framework import filters as rest_framework_filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().select_related('bank').order_by('created')
    # serializer_class = RateSerializer
    pagination_class = RatePagination
    filterset_class = RateFilter
    throttle_classes = [AnonUserRateThrottle]

    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter
    )
    ordering_fields = ['id', 'created', 'type', 'sale', 'buy']

    def get_serializer_class(self):
        if 'pk' in self.kwargs:
            return RateDetailsSerializer
        return RateSerializer


class RateTypeChoicesView(APIView):
    def get(self, request, format=None):  # noqa
        """
        Return a list of all users.
        """
        return Response(choices.RATE_TYPE_CHOICES)


class BankListView(viewsets.ModelViewSet):
    queryset = Bank.objects.all().prefetch_related('rate_set').order_by('id')

    def get_serializer_class(self):
        if 'pk' in self.kwargs:
            return BankDetailsSerializer
        return BankSerializer


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all().order_by('created')
    pagination_class = ContactUsPagination
    # serializer_class = ContactUsSerializer
    throttle_classes = [AnonUserRateThrottle]
    filterset_class = ContactUsFilter
    filter_backends = (filters.DjangoFilterBackend,
                       rest_framework_filters.OrderingFilter,
                       rest_framework_filters.SearchFilter,
                       )
    ordering_fields = ['id', 'email_from', 'subject', 'message', 'created']
    search_fields = ['id', 'email_from', 'subject', 'message', 'created']

    def get_serializer_class(self):
        # breakpoint()
        if 'create' in self.action:
            return ContactUsSendMailSerializer
        return ContactUsSerializer

# class RateList(generics.ListCreateAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer
#
#
# class RateDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer
