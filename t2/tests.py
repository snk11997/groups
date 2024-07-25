from django.test import TestCase

# t2/tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import BlogPost
from .forms import BlogPostForm, UserRegistrationForm

class BlogPostTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = BlogPost.objects.create(title='Test Post', content='Test Content', author=self.user)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 't2/index.html')
        self.assertContains(response, 'Test Post')

    def test_view_post_view(self):
        response = self.client.get(reverse('view_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 't2/view_post.html')
        self.assertContains(response, 'Test Content')

    def test_create_post_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('create_post'), {
            'title': 'New Test Post',
            'content': 'New Test Content'
        })
        self.assertEqual(response.status_code, 302)  # Redirects to index
        self.assertEqual(BlogPost.objects.count(), 2)

    def test_edit_post_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('edit_post', args=[self.post.id]), {
            'title': 'Updated Test Post',
            'content': 'Updated Test Content'
        })
        self.assertEqual(response.status_code, 302)  # Redirects to index
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Test Post')
        self.assertEqual(self.post.content, 'Updated Test Content')

    def test_delete_post_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('delete_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)  # Redirects to index
        self.assertEqual(BlogPost.objects.count(), 0)

class UserTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirects to index
        self.assertEqual(User.objects.count(), 2)

    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': '12345'
        })
        self.assertEqual(response.status_code, 302)  # Redirects to index

    def test_logout_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirects to index

class BlogPostFormTests(TestCase):

    def test_valid_form(self):
        user = User.objects.create_user(username='testuser', password='12345')
        data = {'title': 'Test Post', 'content': 'Test Content', 'author': user.id}
        form = BlogPostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = BlogPostForm(data={})
        self.assertFalse(form.is_valid())

class UserRegistrationFormTests(TestCase):

    def test_valid_form(self):
        data = {'username': 'newuser', 'password': 'newpassword'}
        form = UserRegistrationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
