from django.contrib import admin
from .models import ContactRequest


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    """ make all fields read only """
    readonly_fields = ("email", "name", "content", "date")
