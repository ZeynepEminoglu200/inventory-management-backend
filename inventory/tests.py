from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item, Category, StockLog


class ItemAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='Test1234!'
        )
        self.category = Category.objects.create(name='Electronics')
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'Test1234!'
        }, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_item(self):
        data = {
            'name': 'Laptop',
            'description': 'Dell laptop',
            'quantity': 10,
            'category': self.category.id
        }
        response = self.client.post('/api/items/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(StockLog.objects.count(), 1)

    def test_cannot_create_negative_stock(self):
        data = {
            'name': 'Keyboard',
            'description': 'Mechanical keyboard',
            'quantity': -1,
            'category': self.category.id
        }
        response = self.client.post('/api/items/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('quantity', response.data)

    def test_user_only_sees_their_own_items(self):
        Item.objects.create(
            owner=self.user,
            name='Laptop',
            description='Owned item',
            quantity=5,
            category=self.category
        )

        other_user = User.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='Other1234!'
        )
        Item.objects.create(
            owner=other_user,
            name='Printer',
            description='Other user item',
            quantity=3,
            category=self.category
        )

        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_item_creates_stock_log(self):
        item = Item.objects.create(
            owner=self.user,
            name='Monitor',
            description='Office monitor',
            quantity=10,
            category=self.category
        )

        response = self.client.put(f'/api/items/{item.id}/', {
            'name': 'Monitor',
            'description': 'Office monitor updated',
            'quantity': 7,
            'category': self.category.id
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(StockLog.objects.filter(item=item, change_amount=-3).exists())