from django.utils import timezone
import json
from django.db.models import Q


def get_format_date(date):
    return timezone.localtime(date).strftime("%Y-%m-%d %H:%M:%S")


def to_json(queryset):
    data = [i.json() for i in queryset]
    data = json.dumps(data, ensure_ascii=False)
    return data


def filtering(queryset, request):
    if request.GET.get('account_id', None):
        queryset = queryset.filter(
            Q(account_id=request.GET.get('account_id', None)))
    if request.GET.get('date_from', None):
        queryset = queryset.filter(
            Q(date__gte=request.GET.get('date_from', None)))
    if request.GET.get('date_to', None):
        queryset = queryset.filter(
            Q(date__lte=request.GET.get('date_to', None))
        )
    if request.GET.get('amount_to', None):
        queryset = queryset.filter(
            Q(amount__lte=request.GET.get('amount_to', None))
        )
    if request.GET.get('amount_from', None):
        queryset = queryset.filter(
            Q(amount__gte=request.GET.get('amount_from', None))
        )
    return queryset
