from django.urls import path
from . import views


app_name = "article_app"


urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article_list"),
    path("<slug:slug>/<int:pk>/", views.ArticleDetailView.as_view(), name="article_detail")
]