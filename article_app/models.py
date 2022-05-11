from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from django.template.defaultfilters import slugify
from django.shortcuts import reverse
from django.utils import timezone


class Article(models.Model):
    """
        Article Model Fields:
        title => str article title
        slug => str slug not required by user, dynamically filled with title
        content => str for Article Text Content
        author => fk to custom made user in custom_user_app & registered in settings
        publication_datetime => date & time of Article publication
        is_online => True or False to mark the Article as published or not
        created_at => auto created field for time the article save in db
    """
    title = models.CharField(
        max_length=200, blank=False, null=False,
        verbose_name=_("Article Title")
    )

    slug = models.SlugField(
        max_length=255, blank=True, null=True,
        verbose_name=_("Slug")
    )

    content = models.TextField(
        blank=False, null=False, verbose_name=_("Article Content")
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="articles",
        on_delete=models.CASCADE, blank=False, null=False,
        verbose_name=_("Article Author")
    )

    publication_datetime = models.DateTimeField(
        default=timezone.now, verbose_name=_("Publish Date and Time")
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created at")
    )

    is_online = models.BooleanField(
        default=False, verbose_name=_("Make it Online")
    )

    class Meta:
        """
            ordering objects in Descending Order
            assign transitionable verbose name / plural
        """
        ordering = ("-publication_datetime",)
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def get_absolute_url(self):
        # build url dynamically with slug & id
        return reverse("article_app:article_detail", args=[self.slug, self.pk])

    def save(self, *args, **kwargs):
        # slugify the title for slug field on save
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        # represent Article by its title
        return self.title