from django.test import TestCase, override_settings
from django.shortcuts import reverse
from django.core import mail
from django.conf import settings
from contact_app.forms import ContactRequestForm


class FormTestCases(TestCase):
    """
        test if the form is valid and check redirection and
        send mail after it is valid
    """
    # override settings so i can use mail box
    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_valid_form(self):
        data = {
            "email": "admin@gmail.com",
            "name": "admin",
            "content": "Test"
        }
        form = ContactRequestForm(data=data)
        self.assertTrue(form.is_valid())
        resp = self.client.post(reverse("contact_app:contact_form"), data, follow=True)
        self.assertRedirects(resp, reverse("contact_app:success_form"), status_code=302)

        mail.outbox = []
        mail.send_mail(
            'Subject here', 'Here is the message.',
            settings.EMAIL_HOST_USER, ['dev.omaribrahim@gmail.com'],
            fail_silently=False
        )

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')

    def test_invalid_form(self):
        """
            test every case that make it fail
        """
        invalid_email = {
            "email": "admin@gm",
            "name": "admin",
            "content": "Test"
        }
        invalid_name = {
            "email": "admin@gmail.com",
            "name": "",
            "content": "Test"
        }
        invalid_content = {
            "email": "admin@gmail.com",
            "name": "admin",
            "content": ""
        }
        invalid_email_form = ContactRequestForm(data=invalid_email)
        invalid_name_form = ContactRequestForm(data=invalid_name)
        invalid_content_form = ContactRequestForm(data=invalid_content)
        self.assertFalse(invalid_email_form.is_valid())
        self.assertFalse(invalid_name_form.is_valid())
        self.assertFalse(invalid_content_form.is_valid())
