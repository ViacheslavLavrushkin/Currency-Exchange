from currency import choices, consts
from currency.filters import RateFilter
from currency.forms import ContactUsForm
from currency.forms import RateForm
from currency.forms import SourceForm
from currency.models import Bank
from currency.models import ContactUs
from currency.models import Rate
from currency.tasks import send_email_in_background

from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.cache import cache
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
from django.shortcuts import render, get_object_or_404, reverse, redirect  # noqa

from django_filters.views import FilterView


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


class RateListView(FilterView):
    template_name = 'rate_list.html'
    queryset = Rate.objects.all().select_related('bank')
    paginate_by = 25
    filterset_class = RateFilter


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


def get_latest_rates():
    if consts.CACHE_KEY_LATEST_RATES in cache:
        return cache.get(consts.CACHE_KEY_LATEST_RATES)

    object_list = []
    for bank in Bank.objects.all():
        for ct_value, ct_display in choices.RATE_TYPE_CHOICES:
            latest_rate = Rate.objects\
                .filter(type=ct_value, bank=bank). order_by('-created').first()
            if latest_rate is not None:
                object_list.append(latest_rate)

    cache.set(consts.CACHE_KEY_LATEST_RATES, object_list, 60 * 60 * 8)
    return object_list


# @method_decorator(cache_page(60 * 60 * 8), name='dispatch')
class LatestRates(TemplateView):
    template_name = 'latest_rates.html'

    def get_context_data(self, **kwargs):
        context = super(). get_context_data(**kwargs)
        context['object_list'] = get_latest_rates()
        return context


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


class ContactUsListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus.html'


class ContactUsCreate(CreateView):
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


class ContactUsUpdateView(UpdateView):
    queryset = ContactUs.objects.all()
    form_class = ContactUsForm
    template_name = 'contactus_update.html'
    success_url = reverse_lazy('index')


class ContactUsDetailView(DetailView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_details.html'


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    success_url = reverse_lazy('index')

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
#          return HttpResponse(json.dumps(results), content_type='application/json')
