from django.test import TestCase
from django.template.defaultfilters import slugify
from article_app.models import Article
from custom_user_app.models import User


class ModelTestCases(TestCase):
    def setUp(self) -> None:
        User.objects.create(
            email="test@admin.com",
            username="test_user",
            first_name="test",
            last_name="admin",
            password="8080ta"
        )
        Article.objects.create(
            title="Article Title 1",
            content="Article Content",
            author_id=1,
            is_online=True
        )

    def test_creation_success(self):
        obj = Article.objects.get(id=1)
        self.assertIsInstance(obj, Article)
        self.assertEqual(obj.__str__(), obj.title)

    def test_slugify_success(self):
        obj = Article.objects.get(id=1)
        self.assertEqual(obj.slug, slugify(obj.title))