# from rest_framework import generics
from api.v1.filters import RateFilter
from api.v1.paginators import RatePagination
from api.v1.throttle import AnonUserRateThrottle
from currency.models import Rate
from api.v1.serializers import RateSerializer, RateDetailsSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters as rest_framework_filters

from django_filters import rest_framework as filters

from currency import choices


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().select_related('bank').order_by('-created')
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
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        return Response(choices.RATE_TYPE_CHOICES)

# class RateList(generics.ListCreateAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer
#
#
# class RateDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer

