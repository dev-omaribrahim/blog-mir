from django.test import TestCase
from contact_app.models import ContactRequest


class ModelTestCases(TestCase):
    def setUp(self) -> None:
        self.contact_request = ContactRequest.objects.create(
            email="admin@gmail.com",
            name="admin",
            content="Test"
        )

    def test_creation_success(self):
        self.assertIsInstance(self.contact_request, ContactRequest)
        self.assertEqual(self.contact_request.__str__(), self.contact_request.name)