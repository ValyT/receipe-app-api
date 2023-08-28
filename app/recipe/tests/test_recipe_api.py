"""
Tests for recepie APIs
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


from core.models import Recipe

from recipe.serializers import RecipeSerializer


RECIPES_URL = reverse('recipe:recipe-list')


def create_recipe(user, **params):
    """Create and return sample recipe"""
    defaults = {
        'title': 'Sample recipe title',
        'time_minutes': 33,
        'price': Decimal('6.66'),
        'description': 'Sample desc',
        'link': 'http://example.com/recipe.pdf'
    }
    defaults.update(params)

    recipe = Recipe.objects.create(user=user, **defaults)
    return recipe


class PublicRecipeApiTests(TestCase):
    """Unauthenticated recipe api request tests"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_req(self):
        """Test authentification required to call API"""
        res = self.client.get(RECIPES_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipeApiTests(TestCase):
    """Test recipe API requests that require authentication"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpass123',
            name='Test Name',
            )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrive_recepies(self):
        """Test retriving list of recepies"""
        create_recipe(user=self.user)
        create_recipe(user=self.user)

        res = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_recepies_seen_limited_to_user(self):
        """Test of recepies limited by user"""
        other_user = get_user_model().objects.create_user(
            email='other@example.com',
            password='testotherpass123',
            name='other Name',
            )
        create_recipe(user=other_user)
        create_recipe(user=self.user)

        res = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.filter(user=self.user)
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
