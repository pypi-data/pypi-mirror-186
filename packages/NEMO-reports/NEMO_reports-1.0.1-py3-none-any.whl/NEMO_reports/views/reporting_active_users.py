from NEMO.models import Discipline, User
from django.db.models import QuerySet
from django.shortcuts import render

from NEMO_reports.decorators import accounting_or_manager_required
from NEMO_reports.views.reporting import (
    DataDisplayTable,
    SummaryDisplayTable,
    area_access,
    billing_installed,
    consumable_withdraws,
    custom_charges,
    get_date_range,
    rate_category_enabled,
    report_export,
    reporting_dictionary,
    staff_charges,
    training_sessions,
    usage_events,
)


@accounting_or_manager_required
def active_users(request):
    start, end = get_date_range(request)
    user_ids = set("")
    if request.GET.get("tool_usage") == "on":
        user_ids.update(set(usage_events(start, end, only=["user_id"], values_list="user_id")))
    if request.GET.get("area_access") == "on":
        user_ids.update(set(area_access(start, end, only=["customer_id"], values_list="customer_id")))
    if request.GET.get("staff_charges") == "on":
        user_ids.update(set(staff_charges(start, end, only=["customer_id"], values_list="customer_id")))
    if request.GET.get("consumables") == "on":
        user_ids.update(set(consumable_withdraws(start, end, only=["customer_id"], values_list="customer_id")))
    if request.GET.get("training") == "on":
        user_ids.update(set(training_sessions(start, end, only=["trainee_id"], values_list="trainee_id")))
    if billing_installed() and request.GET.get("custom_charges") == "on":
        user_ids.update(set(custom_charges(start, end, only=["customer_id"], values_list="customer_id")))
    active_user_qs: QuerySet = User.objects.filter(id__in=user_ids)
    data = DataDisplayTable()
    data.headers = [
        ("first", "First name"),
        ("last", "Last name"),
        ("username", "Username"),
        ("email", "Email"),
        ("active", "Active"),
        ("access_expiration", "Access expiration"),
    ]
    if Discipline.objects.exists():
        data.add_header(("discipline", "Discipline"))
    if rate_category_enabled():
        data.add_header(("rate_category", "Rate category"))
    for user in active_user_qs:
        data.add_row(
            {
                "first": user.first_name,
                "last": user.last_name,
                "username": user.username,
                "email": user.email,
                "active": user.is_active,
                "access_expiration": user.access_expiration,
                "discipline": user.discipline,
                "rate_category": user.details.rate_category
                if rate_category_enabled() and hasattr(user, "details")
                else None,
            }
        )
    summary = SummaryDisplayTable()
    if active_user_qs:
        summary.add_header(("item", "Item"))
        summary.add_header(("value", "Value"))
        summary.add_row({"item": "Active users", "value": active_user_qs.count()})
        if Discipline.objects.exists():
            summary.add_row({"item": "By discipline"})
            for discipline in Discipline.objects.all():
                summary.add_row(
                    {"item": f"{discipline.name}", "value": active_user_qs.filter(discipline=discipline).count()}
                )
        if rate_category_enabled():
            from NEMO_billing.rates.models import RateCategory

            summary.add_row({})
            summary.add_row({"item": "By billing rate"})
            for rate_category in RateCategory.objects.all():
                summary.add_row(
                    {
                        "item": f"{rate_category.name}",
                        "value": active_user_qs.filter(details__rate_category=rate_category).count(),
                    }
                )
    if request.GET.get("export"):
        return report_export([summary, data], "active_users", start, end)
    dictionary = {
        "start": start,
        "end": end,
        "tool_usage": request.GET.get("tool_usage"),
        "area_access": request.GET.get("area_access"),
        "training": request.GET.get("training"),
        "consumables": request.GET.get("consumables"),
        "staff_charges": request.GET.get("staff_charges"),
        "custom_charges": request.GET.get("custom_charges"),
        "data": data,
        "summary": summary,
    }
    return render(request, "NEMO_reports/report_active_users.html", reporting_dictionary("active_users", dictionary))
