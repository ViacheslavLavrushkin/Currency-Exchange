from currency.models import Rate
from currency.models import Source

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404  # noqa


def hello_world(request):
    return HttpResponse('Hello World')


def rate_list(request):
    queryset = Rate.objects.all()

    context = {
        'objects': queryset,
    }

    return render(request, 'rate_list.html', context=context)


def rate_details(request, pk):

    # try:
    #     rate = Rate.objects.get(pk=pk)
    # except Rate.DoesNotExist:
    #     raise Http404(f"Rate does not exist with id {pk}")

    rate = get_object_or_404(Rate, pk=pk)

    context = {
        'object': rate,
    }
    return render(request, 'rate_details.html', context=context)


def rate_source(request):
    queryset = Source.objects.all()

    context = {
        'objects': queryset,
    }

    return render(request, 'rate_source.html', context=context)


def rate_privatbank(request):

    rate = 1

    context = {
        'object': rate,
    }
    return render(request, 'rate_privatbank.html', context=context)
