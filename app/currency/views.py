from currency.forms import ContactUsForm
from currency.forms import RateForm
from currency.forms import SourceForm
from currency.models import ContactUs
from currency.models import Rate
from currency.models import Source

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.shortcuts import render, get_object_or_404, reverse, redirect  # noqa


def hello_world(request):
    return HttpResponse('Hello World')


def index(request):
    return render(request, 'index.html')


def source_privatbank(request):

    rate = 1

    context = {
        'object': rate,
    }
    return render(request, 'source_privatbank.html', context=context)


class RateListView(ListView):
    template_name = 'rate_list.html'
    queryset = Rate.objects.all()


class RateDetailView(DetailView):
    template_name = 'rate_details.html'
    queryset = Rate.objects.all()
    form_class = RateForm


class RateCreateView(CreateView):
    queryset = Rate.objects.all()
    template_name = 'rate_create.html'
    success_url = reverse_lazy('currency:rate-list')
    form_class = RateForm


class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate-list')
    form_class = RateForm


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    success_url = reverse_lazy('currency:rate-list')


class SourceListView(ListView):
    template_name = 'source.html'
    queryset = Source.objects.all()


class SourceCreateView(CreateView):
    queryset = Source.objects.all()
    template_name = 'source_create.html'
    success_url = reverse_lazy('currency:source')
    form_class = SourceForm


class SourceUpdateView(UpdateView):
    queryset = Source.objects.all()
    template_name = 'source_update.html'
    success_url = reverse_lazy('currency:source')
    form_class = SourceForm


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    success_url = reverse_lazy('currency:source')


class CreateContactUs(CreateView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('index')
    form_class = ContactUsForm

    def save(self, commit=True):
        print('Form Save\n' * 10)
        return super().save(commit)
