from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from questions.models import LikertAnswer, TextAnswer, Question

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser(username='admin', email='admin@example.com', password='admin123')
        self.user = User.objects.create_user(username='user', email='user@example.com', password='user123')


    def test_view_answers_view(self):
        # Log in as user
        self.client.login(username='user', password='user123')
        response = self.client.get(reverse('view_answers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'viewAnswers.html')

    def test_user_passes_test_decorator(self):
        # Try to access create_question view without logging in
        response = self.client.get(reverse('create_question'))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

