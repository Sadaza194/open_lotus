from django.test import TestCase, Client
from django.urls import reverse

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
