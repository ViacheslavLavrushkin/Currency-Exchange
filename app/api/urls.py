from django.urls import path

from api.views import RateViewSet, RateTypeChoicesView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rate')
urlpatterns = [
    path('choices/currency/types/', RateTypeChoicesView.as_view(), name='choices-currency-types'),
]
urlpatterns += router.urls
