from django.test import TestCase
from django.shortcuts import reverse
from article_app.models import Article
from custom_user_app.models import User


class ViewsTestCases(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="test@admin.com",
            username="test_user",
            first_name="test",
            last_name="admin",
            password="8080ta"
        )
        self.published_article = Article.objects.create(
            title="Article Title 1",
            content="Article Content",
            author_id=1,
            is_online=True
        )
        self.unpublished_article = Article.objects.create(
            title="Article Title 2",
            content="Article Content 2",
            author_id=1,
            is_online=False
        )

    def test_article_view_list_success(self):
        """
        check if view work fine:
         - check status code
         - check it is the correct template
         - check list view contain only the published articles
        """
        url = reverse("article_app:article_list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'article_app/article_list.html')
        self.assertContains(resp, self.published_article.title)
        self.assertNotContains(resp, self.unpublished_article.title)

    def test_article_detail_view(self):
        """
            - check status code
            - check the correct template
            - make sure that if you try to access a detail view
              for unpublished article it gives you 404 not found
        """
        resp_published_article = self.client.get(reverse(
            "article_app:article_detail",
            args=[self.published_article.slug, self.published_article.pk]
        ))
        resp_unpublished_article = self.client.get(reverse(
            "article_app:article_detail",
            args=[self.unpublished_article.slug, self.unpublished_article.pk]
        ))
        self.assertEqual(resp_published_article.status_code, 200)
        self.assertTemplateUsed(resp_published_article, 'article_app/article_detail.html')
        self.assertEqual(resp_unpublished_article.status_code, 404)