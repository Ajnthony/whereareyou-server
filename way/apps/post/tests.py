from django.test import TestCase
from rest_framework.test import (
    APIClient,
    APITestCase,
    APISimpleTestCase,
)
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from .models import Post, Category
from .serializers import PostSerializer

def create_user(**data):
    return get_user_model().objects.create_user(**data)

def create_category(**data):
    default_data = {
        'name': 'test-category',
        'is_active': True,
    }
    
    default_data.update(data)
    
    category = Category.objects.create(**data)
    return category

def create_post(user, category, **data):
    default_data = {
        'title' : 'Test post title',
        'content': 'Test post content',
        'slug': 'test-post-title',
        'category': category,
    }
    
    default_data.update(data)
    
    post = Post.objects.create(user=user, **default_data)
    return post
    

class PublicPostApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_get_all_posts_list(self):
        me = create_user(email='testeruser1@way.com', password='tester1123456', display_name='tester_1')
        not_me = create_user(email='testeruser2@way.com', password='tester2123456', display_name='tester_2')
        another_not_me = create_user(email='testeruser3@way.com', password='tester3123456', display_name='tester_3')
        
        new_category = create_category()
        
        create_post(user=me, category=new_category, slug='test-post-title')
        create_post(user=not_me, category=new_category, slug='test-post-title-not-me')
        create_post(user=another_not_me, category=new_category, slug='test-post-title-another-not-me')
        
        url = reverse('post:posts-list')
        res = self.client.get(url)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 3)

class PrivatePostApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email='tester_user@way.com', password='tester123456', display_name='tester_display')
        self.client.force_authenticate(self.user)
        
    def test_update_access_to_owned_posts_only(self):
        not_me = create_user(email='testeruser2@way.com', password='tester2123456', display_name='tester_2')

        new_category = create_category()
        
        create_post(user=self.user, category=new_category, slug='test-post-title')
        not_my_post = create_post(user=not_me, category=new_category, slug='test-post-title-not-me')
        
        url = reverse('post:post-item', args=(not_my_post.id,))
        
        res = self.client.patch(url, {'content': 'Updated test post content'})
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(not_my_post.content, 'Test post content')
        
class CategoryApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_get_only_active_categories(self):
        create_category() # with default value
        create_category(name='test-category-2', is_active=False)
        create_category(name='test-category-3')
        create_category(name='test-category-4')
        create_category(name='test-category-5', is_active=False)
        
        url = reverse('post:category')
        res = self.client.get(url)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 3)