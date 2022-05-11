from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactRequest


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        exclude = ("date",) # exclude it since it already auto generated

    def send_email(self, subject, content):
        send_mail(
            subject,
            content,
            settings.EMAIL_HOST_USER,
            ['dev.omaribrahim@gmail.com', 'debug@mir.de'],
            fail_silently=False,
        )