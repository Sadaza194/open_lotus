from django.test import TestCase, Client
from django.contrib.auth.models import User
from journal.models import Journal
from django.urls import reverse
from datetime import date

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.journal = Journal.objects.create(user=self.user, text='This is a test journal', date=date.today())

    def test_journal_base(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('journal_base'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'journalBase.html')

    def test_view_journals(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('view_journals'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'viewJournals.html')

    def test_create_journal_POST(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('create_journal'), {
            'text': 'This is another test journal',
            'date': '2024-04-08'
        })
        self.assertEqual(response.status_code, 302)  # Redirects to home
        self.assertEqual(Journal.objects.last().text, 'This is another test journal')
