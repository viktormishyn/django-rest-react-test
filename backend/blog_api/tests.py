from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class PostTests(APITestCase):

    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        # reverse brings url, based on app_name ('blog_api') and path's name ('listcreate') from blog_api.urls.py
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_superuser(
            username='test_user1', password='12345678')
        # self.testuser1.is_stuff = True
        self.client.login(username=self.testuser1.username,
                          password='12345678')

        data = {'title': 'new', 'author': 1,
                'excerpt': 'new', 'content': 'new'}
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        root = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_update(self):

        client = APIClient()

        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user(
            username='test_user1', password='12345678')
        self.testuser2 = User.objects.create_user(
            username='test_user2', password='12345678')
        client.login(username=self.testuser2.username, password='12345678')
        test_post = Post.objects.create(
            category_id=1, title='Post Title', excerpt='Post Excerpt',
            content='Post Content', slug='post-title', author_id=1, status='published')

        client.login(username=self.testuser2.username, password='12345678')
        url = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})
        response = client.put(
            url, {
                "title": "New",
                "author": 1,
                "excerpt": "New",
                "content": "New",
                "status": "published"
            }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # only the author of the post is allowd to adit it
