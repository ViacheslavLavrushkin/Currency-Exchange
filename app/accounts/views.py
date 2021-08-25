from accounts.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView


class MyProfile(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    template_name = 'my-profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
    )

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(pk=self.request.user.pk)
    #     return queryset

    def get_object(self, queryset=None):
        return self.request.user


class PasswordReset(PasswordResetForm, UpdateView):
    queryset = User.objects.all()
    template_name = 'password_reset.html'
    success_url = reverse_lazy('index')
    fields = (
        'current password',
        'new password',
        'confirm new password',
    )
