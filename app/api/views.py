# from rest_framework import generics
from api.paginators import RatePagination
from currency.models import Rate
from api.serializers import RateSerializer, RateDetailsSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from currency import choices


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    # serializer_class = RateSerializer
    pagination_class = RatePagination
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

