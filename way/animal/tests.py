from django.test import TestCase
from rest_framework.test import (
    APIClient,
    APITestCase,
    APISimpleTestCase,
)
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from django.utils import timezone
from .models import Animal
from .serializers import AnimalSerializer

def create_user(**data):
    return get_user_model().objects.create_user(**data)

def create_animal(user, **data):
    default_data = {
        'name': 'Test animal',
        'size': 'S',
        'last_seen_location': 'CA',
        'gender': 'Female',
        'description': 'Test description for Test animal',
        'species': 'Cat',
    }
    
    default_data.update(data)
    
    animal = Animal.objects.create(user=user, **default_data)
    return animal

# only authenticated users can create/update animal instances
# so there's no public animal tests
class AnimalTests(TestCase):
    def setUp(self):
        self.user = create_user(
            email='testeruser@way.com',
            password='tester123456',
            first_name='test_first',
            last_name='test_last',
            display_name='test_display'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        
    def test_create_animal(self):
        url = reverse('animal:animal-list')
        data = {
            'name': 'Test animal',
            'size': 'S',
            'last_seen_location': 'CA',
            'gender': 'Female',
            'description': 'Test description for Test animal',
            'species': 'Cat',
            
        }
        
        res = self.client.post(url, data)
        
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(res.data['tags']), 0)
        self.assertEqual(res.data['is_found'], False)
        values_using_default = ['user', 'image', 'date_created', 'date_updated', 'likes', 'views']
        for value in values_using_default:
            self.assertIn(value, res.data)
        
    def test_invalid_data_fail_to_create(self):
        url = reverse('animal:animal-list')
        data = {
            # deliberately not sending "name", one of the required fields
            # 'name': 'Test animal',
            'size': 'S',
            'last_seen_location': 'CA',
            'gender': 'Female',
            'description': 'Test description for Test animal',
            'species': 'Cat',
            
        }
        
        res = self.client.post(url, data)
        
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_only_owners_have_access_to_their_pets(self):
        other_user = create_user(email='testeruser2@way.com', password='123987456765')
        # print(other_user.id)
        
        create_animal(user=self.user)
        other_users_pet = create_animal(user=other_user)
        
        url = reverse('animal:animal-detail', args=(other_users_pet.id,))
        res = self.client.patch(url, {'species': 'Dog'})
        
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        
        test_res = self.client.get(url)
        self.assertEqual(test_res.data['species'], 'Cat')
        