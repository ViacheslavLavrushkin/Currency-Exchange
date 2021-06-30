from annoying.functions import get_object_or_None

from currency.forms import ContactUsForm
from currency.forms import RateForm
from currency.forms import SourceForm
from currency.models import ContactUs
from currency.models import Rate
from currency.models import Source


from django.http import HttpResponse, HttpResponseRedirect
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


def contactus(request):
    queryset = ContactUs.objects.all()

    context = {
        'objects': queryset,
    }

    return render(request, 'contactus.html', context=context)


def source(request):
    queryset = Source.objects.all()

    context = {
        'objects': queryset,
    }

    return render(request, 'source.html', context=context)


def source_privatbank(request):

    rate = 1

    context = {
        'object': rate,
    }
    return render(request, 'source_privatbank.html', context=context)


def rate_create(request):

    if request.method == 'POST':
        form_data = request.POST
        form = RateForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/rate/list/')
    elif request.method == 'GET':
        form = RateForm()

    context = {
        'message': 'Rate Create',
        'form': form,
        'count': Rate.objects.count(),
    }
    return render(request, 'rate_create.html', context=context)


def rate_update(request, pk):
    instance = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        form_data = request.POST
        form = RateForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=instance)

    context = {
        'form': form,
    }
    return render(request, 'rate_update.html', context=context)


def rate_delete(request, pk):
    instance = get_object_or_None(Rate, pk=pk)
    if instance is not None:
        instance.delete()
    return HttpResponseRedirect('/currency/rate/list/')


def source_create(request):

    if request.method == 'POST':
        form_data = request.POST
        form = SourceForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/source/')
    elif request.method == 'GET':
        form = SourceForm()

    context = {
        'message': 'Source Create',
        'form': form,
        'count': Source.objects.count(),
    }
    return render(request, 'source_create.html', context=context)


def source_update(request, pk):
    instance = get_object_or_404(Source, pk=pk)

    if request.method == 'POST':
        form_data = request.POST
        form = SourceForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/source/')
    elif request.method == 'GET':
        form = SourceForm(instance=instance)

    context = {
        'form': form,
    }
    return render(request, 'source_update.html', context=context)


def source_delete(request, pk):
    instance = get_object_or_None(Source, pk=pk)
    if instance is not None:
        instance.delete()
    return HttpResponseRedirect('/currency/source/')


def contactus_create(request):

    if request.method == 'POST':
        form_data = request.POST
        form = ContactUsForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/contactus/')
    elif request.method == 'GET':
        form = ContactUsForm()

    context = {
        'message': 'ContactUs Create',
        'form': form,
        'count': ContactUs.objects.count(),
    }
    return render(request, 'contactus_create.html', context=context)
