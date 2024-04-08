from datetime import timezone
from django.test import TestCase, Client
from memories.views import create_memory
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Memory

class CreateMemoryTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = Client()  # Create a test client

    def test_get_create_memory_view_authenticated(self):
        """Test that authenticated users can access the create memory form."""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('create_memory'))
        self.assertEqual(response.status_code, 200)  # OK
        self.assertTemplateUsed(response, 'createMemory.html')

    def test_post_create_memory_view_valid_data(self):
        """Test that valid form data successfully creates a memory."""
        self.client.login(username='testuser', password='password123')
        data = {
            'emotion': 'Happy',
            'text': 'This is a test memory!',
        }
        response = self.client.post(reverse('create_memory'), data)
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertEqual(response.url, '/')  # Redirect to home page
        memory = Memory.objects.get(user=self.user)
        self.assertEqual(memory.emotion, data['emotion'])
        self.assertEqual(memory.text, data['text'])


class ViewMemoriesTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = Client()
        # Create some test memories for the user
        Memory.objects.create(user=self.user, emotion='Sad', text='Test memory 1')
        Memory.objects.create(user=self.user, emotion='Happy', text='Test memory 2')


    def test_get_view_memories_view_authenticated(self):
        """Test that authenticated users can see their memories."""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('view_memories'))
        self.assertEqual(response.status_code, 200)  # OK
        self.assertTemplateUsed(response, 'viewMemories.html')
        # Assert that both test memories are rendered in the response
        self.assertContains(response, 'Test memory 1')
        self.assertContains(response, 'Test memory 2')



class InterationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.login(username='test_user', password='test_password')

    def test_memories_base_view(self):
        response = self.client.get(reverse('memories_base'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'memoriesBase.html')

    def test_view_memories_view(self):
        response = self.client.get(reverse('view_memories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'viewMemories.html')

    def test_create_memory_view_get(self):
        response = self.client.get(reverse('create_memory'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'createMemory.html')

