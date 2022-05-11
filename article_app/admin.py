from django.contrib import admin
from article_app.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """read only, because of it is auto generated field"""
    readonly_fields = ('created_at',)
