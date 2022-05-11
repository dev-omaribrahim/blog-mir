from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = "contact_app"


urlpatterns = [
    path("form/", views.ContactRequestFormView.as_view(), name="contact_form"),
    path("success/", TemplateView.as_view(template_name="contact_app/success_form.html"), name="success_form")
]