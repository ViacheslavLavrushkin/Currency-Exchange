from currency.views import index

import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# from api.views import RateList, RateDetails


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('rates/', RateList.as_view()),
    # path('rates/<int:pk>', RateDetails.as_view()),

    path('api/', include('api.urls')),
    path('', index, name='index'),
    path('auth/', include('django.contrib.auth.urls')),
    path('currency/', include('currency.urls')),
    path('accounts/', include('accounts.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT))
urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
