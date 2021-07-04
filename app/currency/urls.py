from currency.views import (
    CreateContactUs,
    RateCreateView, RateDeleteView, RateDetailView, RateListView, RateUpdateView,
    source, source_create, source_delete, source_privatbank, source_update,
)  # noqa

from django.urls import path

app_name = 'currency'

urlpatterns = [

    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/create/', RateCreateView, name='rate-create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view, name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view, name='rate-delete'),
#   path('contactus/', contactus, name='contactus'),
    path('contactus/create/', CreateContactUs.as_view(), name='contactus-create'),
    path('source/', source, name='source'),
    path('source/create/', source_create, name='source-create'),
    path('source/update/<int:pk>/', source_update, name='source-update'),
    path('source/delete/<int:pk>/', source_delete, name='source-delete'),
    path('source/privatbank/', source_privatbank, name='source-privatbank'),
]
