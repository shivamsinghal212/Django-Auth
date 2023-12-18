from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase


class AccountTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )

    def test_login_user_returns_200(self):
        """
        Ensure user should be able to login
        """
        url = reverse("login")
        data = {"username": "testuser", "password": "testpass"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("refresh", response.data)
        self.assertIn("access", response.data)

    def test_login_wrong_password_returns_401(self):
        """
        Ensure user should not be able to login with wrong password
        """
        url = reverse("login")
        data = {"username": "testuser", "password": "testpass1"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 401)

    def test_profile_returns_200(self):
        """
        Ensure user should be able to access profile
        """
        login_url = reverse("login")
        login_data = {"username": "testuser", "password": "testpass"}
        login_response = self.client.post(login_url, login_data, format="json")
        token = login_response.data["access"]

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        profile_url = reverse("profile")
        response = self.client.get(profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
