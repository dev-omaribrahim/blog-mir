from django.test import TestCase
from django.shortcuts import reverse


class ViewTestCases(TestCase):
    def test_contact_page_success(self):
        url = reverse("contact_app:contact_form")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "contact_app/contact_form.html")

    def test_success_form_success(self):
        url = reverse("contact_app:success_form")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200),
        self.assertTemplateUsed(resp, "contact_app/success_form.html")