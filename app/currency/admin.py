from currency.models import Rate

from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from rangefilter.filters import DateTimeRangeFilter


class RateResource(resources.ModelResource):

    class Meta:
        model = Rate


class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource
    list_display = (
        'id',
        'buy',
        'sale',
        'type',
        'bank',
        'created',
    )
    list_filter = (
        ('created', DateTimeRangeFilter),
        'type',
        'bank',
        'created',
    )
    search_fields = (
        'type',
        'bank',
    )
    readonly_fields = (
        'buy',
        'sale',
    )

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Rate, RateAdmin)


# list_display = (
#     'id',
#     'recipient',
#     'book',
#     'created',
#     'status',
# )
# readonly_fields = ('recipient', 'book')
# list_filter = ('status', 'created', )
# search_fields = ('recipient__username', 'recipient__last_name')
# # list_select_related = ('recipient', 'book')  # objects.select_related('recipient', 'book')
#
# # def get_readonly_fields(self, request, obj=None):
# #     readonly_fields = super().get_readonly_fields()
#
# def has_delete_permission(self, request, obj=None):
#     return False
