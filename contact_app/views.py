from django.shortcuts import render
from django.views.generic.edit import FormView
from django.shortcuts import reverse
from django.urls import reverse_lazy
from .forms import ContactRequestForm


class ContactRequestFormView(FormView):
    template_name = "contact_app/contact_form.html"
    form_class = ContactRequestForm
    success_url = reverse_lazy("contact_app:success_form")

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        content_request = form.save()
        form.send_email(
            subject=content_request.name,
            content=content_request.content,
        )
        return super().form_valid(form)

