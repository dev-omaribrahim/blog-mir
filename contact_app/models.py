from django.db import models
from django.utils.translation import gettext as _


class ContactRequest(models.Model):
    """
        Contact Request Fields:
        email => sender email
        name => sender name
        date => sending date
    """

    email = models.EmailField(
        max_length=254, blank=False, null=False,
        verbose_name=_("Email")
    )

    name = models.CharField(
        max_length=255, blank=False, null=False,
        verbose_name=_("Name")
    )

    content = models.TextField(
        blank=False, null=False, verbose_name=_("Content")
    )

    date = models.DateField(
        auto_now_add=True, verbose_name=_("Contact Request Date")
    )

    class Meta:
        """
            ordering objects in Descending Order
            assign transitionable verbose name / plural
        """
        ordering = ("-date",)
        verbose_name = _("Contact Request")
        verbose_name_plural = _("Contact Requests")

    def __str__(self):
        # represent Contact Request by its Sender Name
        return self.name