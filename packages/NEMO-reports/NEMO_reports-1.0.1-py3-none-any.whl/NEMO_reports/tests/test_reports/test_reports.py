from NEMO.models import User
from django.test import TestCase
from django.urls import reverse

from NEMO_reports.tests.test_utilities import test_response_is_landing_page


class TestReports(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(
            username="test_user", first_name="Testy", last_name="McTester", badge_number=1
        )
        self.accounting, created = User.objects.get_or_create(
            username="test_accounting",
            first_name="Testy",
            last_name="McTester",
            badge_number=2,
            is_accounting_officer=True,
        )

    def test_master_url(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("reporting"), follow=True)
        test_response_is_landing_page(self, response)
        self.client.force_login(self.accounting)
        response = self.client.get(reverse("reporting"), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_active_users_report(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("reporting_active_users"), follow=True)
        test_response_is_landing_page(self, response)
        self.client.force_login(self.accounting)
        response = self.client.get(reverse("reporting_active_users"), follow=True)
        self.assertEqual(response.status_code, 200)
