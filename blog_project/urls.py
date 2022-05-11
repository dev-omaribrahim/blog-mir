from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='root.html'), name="root"),
    path('admin/', admin.site.urls),
    path('article/', include("article_app.urls", namespace="article_app")),
    path('contact/', include("contact_app.urls", namespace="contact_app")),
]
