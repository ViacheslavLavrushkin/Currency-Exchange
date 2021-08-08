from django.db.models import F

from currency.models import Analytics
from currency import choices


class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):


        '''
        path = '/foo/'
        method = 'GET'

        Analytics.objects.filter(method=method, path=path)
        Analytics.objects.update_or_create(method=method, path=path)
        '''
        request_method = choices.REQUEST_METHOD_CHOICES_MAPPER[request.method]
        Analytics.objects.update_or_create(
            request_method=request_method, path=request.path,
            defaults={'counter': F('counter') + 1}
        )
        # counter = Analytics.objects.filter(
        #     request_method=request_method, path=request.path).last()
        # if counter:
        #     counter.counter += 1
        #     counter.save()
        # else:
        #     Analytics.objects.create(
        #         request_method=request_method, path=request.path, counter=1)

        response = self.get_response(request)
        return response
