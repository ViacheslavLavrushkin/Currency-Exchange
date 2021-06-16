from currency.views import hello_world, rate_list, rate_details, rate_source, rate_privatbank

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello_world/', hello_world),
    path('currency/rate/list/', rate_list),
    path('currency/rate/details/<int:pk>/', rate_details),
    path('currency/rate/source/', rate_source),
    path('currency/rate/source/privatbank/', rate_privatbank),

]
