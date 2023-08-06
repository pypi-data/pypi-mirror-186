import csv
import datetime
from datetime import timedelta
from typing import List, Union

from NEMO.models import AreaAccessRecord, ConsumableWithdraw, StaffCharge, TrainingSession, UsageEvent
from NEMO.utilities import (
    BasicDisplayTable,
    capitalize,
    export_format_datetime,
    extract_optional_beginning_and_end_dates,
)
from dateutil.relativedelta import relativedelta
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe

from NEMO_reports.customizations import ReportsCustomization
from NEMO_reports.decorators import accounting_or_manager_required
from NEMO_reports.templatetags.reports_tags import app_installed


class SummaryDisplayTable(BasicDisplayTable):
    def to_html(self):
        result = '<table id="summary-table" class="table table-bordered" style="margin-top: 20px;">'
        result += '<thead><tr class="success"><th colspan="2" class="text-center">Summary</th></tr></thead>'
        result += "<tbody>"
        for row in self.rows:
            if len(row) == 1 and "item" in row:
                result += f'<tr class="info"><td colspan="2" style="font-weight: bold">{row["item"]}</td></tr>'
            else:
                result += "<tr>"
                for key in row.keys():
                    result += f'<td>{ row.get(key, "") }</td>'
                result += "</tr>"
        result += "</tbody>"
        result += "</table>"
        return mark_safe(result)


class DataDisplayTable(BasicDisplayTable):
    def to_html(self):
        result = (
            '<table id="data-table" class="table table-bordered table-hover table-striped" style="margin-top: 20px;">'
        )
        result += '<thead><tr class="success">'
        for key, value in self.headers:
            result += f"<th>{value}</th>"
        result += "</tr></thead>"
        result += "<tbody>"
        for row in self.rows:
            result += "<tr>"
            for key, value in self.headers:
                result += f'<td>{self.formatted_value(row.get(key, ""), html=True) or ""}</td>'
            result += "</tr>"
        result += "</tbody>"
        result += "</table>"
        return mark_safe(result)

    def formatted_value(self, value, html: bool = False):
        if isinstance(value, bool) and html:
            if value:
                return '<span class="glyphicon glyphicon-ok success-highlight"></span>'
            else:
                return '<span class="glyphicon glyphicon-remove danger-highlight"></span>'
        return super().formatted_value(value)


# Create your views here.
@accounting_or_manager_required
def reports(request):
    return render(request, "NEMO_reports/reports.html", {"report_dict": report_dict})


def report_export(tables: List[BasicDisplayTable], key: str, start: datetime.date, end: datetime.date):
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    for table in tables:
        if table.headers:
            writer.writerow([capitalize(display_value) for key, display_value in table.headers])
            for row in table.rows:
                writer.writerow([table.formatted_value(row.get(key, "")) for key, display_value in table.headers])
            writer.writerow([])
    filename = f"{key}_data_{export_format_datetime(start, t_format=False)}_to_{export_format_datetime(end, t_format=False)}.csv"
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response


def get_date_range(request) -> (datetime.date, datetime.date):
    start, end = extract_optional_beginning_and_end_dates(request.GET, date_only=True)
    today = datetime.datetime.now().astimezone()  # Today's datetime in our timezone
    reports_default_daterange = ReportsCustomization.get("reports_default_daterange")
    if not start or not end:
        if reports_default_daterange == "this_year":
            start = today.replace(month=1, day=1)
            end = today.replace(month=12, day=31)
        elif reports_default_daterange == "this_month":
            start = today.replace(day=1)
            end = today + relativedelta(day=31)
        elif reports_default_daterange == "this_week":
            first_day_of_the_week = ReportsCustomization.get_int("reports_first_day_of_week")
            weekday = today.weekday() if first_day_of_the_week else today.isoweekday()
            start = today - timedelta(days=weekday)
            end = start + timedelta(days=6)
        elif reports_default_daterange == "yesterday":
            start = today - timedelta(days=1)
            end = today - timedelta(days=1)
        else:
            start = today
            end = today
    return start.date(), end.date()


def billing_installed():
    return app_installed("NEMO_billing")


def rate_category_enabled():
    if app_installed("NEMO_user_details") and app_installed("NEMO_billing.rates"):
        from NEMO_user_details.customizations import UserDetailsCustomization

        return UserDetailsCustomization.get_bool(
            "user_details_enable_rate_category"
        ) or UserDetailsCustomization.get_bool("user_details_require_rate_category")
    return False


def reporting_dictionary(key, dictionary):
    return {**report_dict.get(key), **dictionary}


def usage_events(start, end, only: List = None, values_list: str = None) -> Union[QuerySet, List]:
    queryset = UsageEvent.objects.only(*((only or []) + ["end"])).filter(end__date__gte=start, end__date__lte=end)
    return queryset if not values_list else queryset.values_list(values_list, flat=True)


def area_access(start, end, only: List = None, values_list: str = None) -> Union[QuerySet, List]:
    queryset = AreaAccessRecord.objects.only(*((only or []) + ["end"])).filter(end__date__gte=start, end__date__lte=end)
    return queryset if not values_list else queryset.values_list(values_list, flat=True)


def staff_charges(start, end, only: List = None, values_list: str = None) -> Union[QuerySet, List]:
    queryset = StaffCharge.objects.only(*((only or []) + ["end"])).filter(end__date__gte=start, end__date__lte=end)
    return queryset if not values_list else queryset.values_list(values_list, flat=True)


def consumable_withdraws(start, end, only: List = None, values_list: str = None) -> Union[QuerySet, List]:
    queryset = ConsumableWithdraw.objects.only(*((only or []) + ["date"])).filter(
        date__date__gte=start, date__date__lte=end
    )
    return queryset if not values_list else queryset.values_list(values_list, flat=True)


def training_sessions(start, end, only: List = None, values_list: str = None) -> Union[QuerySet, List]:
    queryset = TrainingSession.objects.only(*((only or []) + ["date"])).filter(
        date__date__gte=start, date__date__lte=end
    )
    return queryset if not values_list else queryset.values_list(values_list, flat=True)


def custom_charges(start, end, only: List = None, values_list: str = None) -> Union[QuerySet, List]:
    from NEMO_billing.models import CustomCharge

    queryset = CustomCharge.objects.only(*((only or []) + ["date"])).filter(date__date__gte=start, date__date__lte=end)
    return queryset if not values_list else queryset.values_list(values_list, flat=True)


report_dict = {
    "active_users": {
        "report_url": "reporting_active_users",
        "report_title": "Active users report",
        "report_description": "Lists active users in NEMO, meaning any user with recorded activity <b>ending</b> during the date range (Tool usage, Area access, Consumable withdraw, Training, Staff charges)",
    }
}
