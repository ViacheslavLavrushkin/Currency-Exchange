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
    path('bank/', SourceListView.as_view(), name='bank'),
    path('bank/create', SourceCreateView.as_view(), name='source-create'),
    path('bank/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('bank/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
    path('bank/privatbank/', source_privatbank, name='source-privatbank'),
]
