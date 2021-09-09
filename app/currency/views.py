from currency.forms import ContactUsForm
from currency.forms import RateForm
from currency.forms import SourceForm
from currency.models import Bank
from currency.models import ContactUs
from currency.models import Rate
from currency.tasks import send_email_in_background

from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.shortcuts import render, get_object_or_404, reverse, redirect  # noqa


def hello_world(request):
    return HttpResponse('Hello World')


def index(request):
    print('INDEX')  # noqa
    return render(request, 'index.html')


def source_privatbank(request):

    rate = 1

    context = {
        'object': rate,
    }
    return render(request, 'source_privatbank.html', context=context)


class RateListView(ListView):
    template_name = 'rate_list.html'
    queryset = Rate.objects.all().select_related('bank')


class RateDetailView(UserPassesTestMixin, DetailView):
    template_name = 'rate_details.html'
    queryset = Rate.objects.all()
    form_class = RateForm

    def test_func(self):
        return self.request.user.is_authenticated


class RateCreateView(CreateView):
    queryset = Rate.objects.all()
    template_name = 'rate_create.html'
    success_url = reverse_lazy('currency:rate-list')
    form_class = RateForm


class RateUpdateView(UserPassesTestMixin, UpdateView):
    queryset = Rate.objects.all()
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate-list')
    form_class = RateForm

    def test_func(self):
        return self.request.user.is_superuser


class RateDeleteView(UserPassesTestMixin, DeleteView):
    queryset = Rate.objects.all()
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


class SourceListView(ListView):
    template_name = 'source.html'
    queryset = Bank.objects.all()


class SourceCreateView(CreateView):
    queryset = Bank
    template_name = 'source_create.html'
    success_url = reverse_lazy('currency:source')
    form_class = SourceForm


class SourceUpdateView(UpdateView):
    queryset = Bank.objects.all()
    template_name = 'source_update.html'
    success_url = reverse_lazy('currency:source')
    form_class = SourceForm


class SourceDeleteView(DeleteView):
    queryset = Bank.objects.all()
    success_url = reverse_lazy('currency:source')


class CreateContactUs(CreateView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('index')
    form_class = ContactUsForm

    # def save(self, commit=True):
    #     print('Form Save\n' * 10)
    #     return super().save(commit)

    def form_valid(self, form):
        data = form.cleaned_data
        body = f'''
        From: {data['email_from']}
        Topic: {data['subject']}
        Message:
        {data['message']}
        '''

        send_email_in_background.delay(body)

        # from .tasks import print_hello_world
        # print_hello_world.delay()

        return super().form_valid(form)


# class RateListApi(View):
#     def get(self, request):
#         rates = Rate.objects.all()
#         results = []
#         for rate in rates:
#             results.append({
#                 'id': rate.id,
#                 'sale': float(rate.sale),
#                 'buy': float(rate.buy),
#                 'bank': rate.bank_id,
#             })
#         import json
#         return JsonResponse(results, safe=False)
        # return HttpResponse(json.dumps(results), content_type='application/json')
