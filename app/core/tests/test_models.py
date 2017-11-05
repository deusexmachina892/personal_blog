import time

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@deus.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(
        email,
        password
    )


class ModelTest(TestCase):

    def setUp(self):
        """Setup for test"""
        self.user = get_user_model().objects.create_user(
            username='deus',
            password='testpass'
        )

    def test_post_str(self):
        """Test creating Post is successful"""
        post = models.Post.objects.create(
            title='My Post',
            slug='Technology',
            author=self.user,
            body='Test body',
            publish=time.time(),
            created=time.time(),
            updated='draft'
        )

        self.assertEqual(str(post), post.title)
