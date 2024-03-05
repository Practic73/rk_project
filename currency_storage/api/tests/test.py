from http import HTTPStatus
from rest_framework.test import APIClient, APITestCase

from rest_framework.authtoken.models import Token


class TestCurrency(APITestCase):
    LIST_URL = '/api/v1/currencies/'
    DETAIL_URL = '/api/v1/currency/'

    token = Token.objects.get(user__username='lauren')
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.key)
    anonim_user = APIClient()

    def test_get_auth_user_currencies(self):
        response = self.client.get(self.LIST_URL, format='json')
        self.assertEqual(response.status_code, HTTPStatus.HTTP_200_OK)

    def test_get_anonim_user_currencies(self):
        response = self.client.get(self.LIST_URL, format='json')
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_get_auth_user_currency(self):
        response = self.client.get(self.DETAIL_URL, format='json')
        self.assertEqual(response.status_code, HTTPStatus.HTTP_200_OK)

    def test_get_anonim_user_currencu(self):
        response = self.client.get(self.DETAIL_URL, format='json')
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)
