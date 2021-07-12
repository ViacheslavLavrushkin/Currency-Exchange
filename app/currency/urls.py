from currency.views import (
    CreateContactUs,
    RateCreateView, RateDeleteView, RateDetailView, RateListView, RateUpdateView,
    SourceCreateView, SourceDeleteView, SourceListView, SourceUpdateView, source_privatbank,
)  # noqa

from django.urls import path

app_name = 'currency'

urlpatterns = [

    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('contactus/create/', CreateContactUs.as_view(), name='contactus-create'),
    path('source/', SourceListView.as_view(), name='source'),
    path('source/create', SourceCreateView.as_view(), name='source-create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
    path('source/privatbank/', source_privatbank, name='source-privatbank'),
]
