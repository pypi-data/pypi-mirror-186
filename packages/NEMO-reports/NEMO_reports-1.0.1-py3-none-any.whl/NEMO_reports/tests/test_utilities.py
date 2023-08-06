from django.test import TestCase
from requests import Response


def test_response_is_landing_page(test_case: TestCase, response: Response):
    test_case.assertEqual(response.status_code, 200)
    test_case.assertEqual(response.request["PATH_INFO"], "/")
