from django.urls import path

from NEMO_reports.views import reporting, reporting_active_users

urlpatterns = [
    path("reporting/", reporting.reports, name="reporting"),
    path("reporting/active_users", reporting_active_users.active_users, name="reporting_active_users"),
]
