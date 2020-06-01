from django.test import TestCase, Client
from django.utils import timezone

from django.urls import reverse

from .models import Post
from django.contrib.auth.models import User


# Create your tests here.


# -------------------------------------- APP POSTS ------------------------#

# testing views
class TestViews(TestCase):
    def setUp(self):
        self.new_author = User.objects.create(username='samsung')
        self.new_post = Post.objects.create(
                title = "test post",
                content = "test post content",
                author = User.objects.get(username='samsung')
        )
    
    def test_homepage(self):
        client = Client()
        response = client.get('/accounts/register/', follow=True).status_code
        self.assertEqual(response, 200)
    



# testing forms


# testing models
class TestModels(TestCase):
    
    def setUp(self):
        self.new_author = User.objects.create(username='samsung')
        self.new_post = Post.objects.create(
                title = "test post",
                content = "test post content",
                author = User.objects.get(username='samsung')
        )
        
    def test_new_post(self):
        self.assertEqual(self.new_post.author.username, 'samsung')
        self.assertEqual(self.new_post.title, 'test post')
        self.assertEqual(self.new_post.content, 'test post content')
    