from django.test import TestCase
from rest_framework.test import (
    APIClient,
    APITestCase,
    APISimpleTestCase,
)
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_create_user_success(self):
        url = reverse('user:register')
        data = {
            'email': 'testeruser@way.com',
            'password': 'tester123456',
            'first_name': 'test_first',
            'last_name': 'test_last',
            'display_name': 'test_display'
        }
        
        res = self.client.post(url, data)
        
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertNotIn('password', res.data)
        
    def test_using_existing_email_fails(self):
       url = reverse('user:register')
       data = {
            'email': 'testeruser@way.com',
            'password': 'tester123456',
            'first_name': 'test_first',
            'last_name': 'test_last',
            'display_name': 'test_display'
        }
       
       # create a user
       create_user(**data)
       
       # attemp to create another user with the same data (email)
       res = self.client.post(url, data)
       
       self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
       
    def test_password_too_short(self):
        url = reverse('user:register')
        data = {
            'email': 'testeruser@way.com',
            'password': '456',
            'first_name': 'test_first',
            'last_name': 'test_last',
            'display_name': 'test_display'
        }
        
        res = self.client.post(url, data)
       
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_created = get_user_model().objects.filter(email=data['email']).exists()
        self.assertEqual(user_created, False)
        
    def test_generate_token(self):
        token_url = reverse('user:login')
        
        user_data = {
            'email': 'testeruser@way.com',
            'password': 'tester123456',
            'first_name': 'test_first',
            'last_name': 'test_last',
            'display_name': 'test_display'
        }
        
        create_user(**user_data)
        
        login_data = {
            'email': 'testeruser@way.com',
            'password': 'tester123456'
        }
        
        res = self.client.post(token_url, login_data)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('access', res.data)
        
    def test_no_token_with_invalid_credential(self):
        token_url = reverse('user:login')
        
        create_user(email='testeruser@way.com', password='tester123456')
        login_data = {
            'email': 'testeruser@way.com',
            'password': 'tester654321'
        }
        
        res = self.client.post(token_url, login_data)
        
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('access', res.data)