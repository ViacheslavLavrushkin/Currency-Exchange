from currency.views import (
    hello_world,
    rate_list, rate_details,
    rate_create, rate_update,
    rate_delete,
    contactus, contactus_create,
    source, source_create, source_update, source_privatbank,
    source_delete,
)  # noqa

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', hello_world),
    path('currency/rate/list/', rate_list),
    path('currency/rate/details/<int:pk>/', rate_details),
    path('currency/rate/create/', rate_create),
    path('currency/rate/update/<int:pk>/', rate_update),
    path('currency/rate/delete/<int:pk>/', rate_delete),
    path('currency/contactus/', contactus),
    path('currency/contactus/create/', contactus_create),
    path('currency/source/', source),
    path('currency/source/create/', source_create),
    path('currency/source/update/<int:pk>/', source_update),
    path('currency/source/delete/<int:pk>/', source_delete),
    path('currency/source/privatbank/', source_privatbank),
]
