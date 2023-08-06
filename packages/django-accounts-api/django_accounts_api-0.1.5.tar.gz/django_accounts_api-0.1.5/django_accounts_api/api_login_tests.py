from django.forms import Form
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class APILoginTestCase(TestCase):
    """Basic tests of the content type json API login view"""

    def setUp(self) -> None:
        """Get the url and create a user"""
        self.url = reverse("django_accounts_api:login")
        self.user = User.objects.create_user("test", password="test")
        return super().setUp()

    def test_json_login_get_unauthed(self):
        """An unauthed get with accept json should return a 401"""
        response = self.client.get(
            self.url,
            HTTP_ACCEPT='application/json'
        )
        assert response.status_code == 401

    def test_json_login_get_authed(self):
        """An unauthed get with accept json should return a 401"""
        self.client.force_login(self.user)
        response = self.client.get(
            self.url,
            HTTP_ACCEPT='application/json'
        )
        assert response.status_code == 200

    def test_json_login_post_no_fields(self):
        """A post accept json without username and password should return 400 and the errors"""
        response = self.client.post(
            self.url, {},
            HTTP_ACCEPT='application/json'
        )
        assert response.status_code == 400
        response_json = response.json()
        assert 'username' in response_json['errors']
        assert 'password' in response_json['errors']

    def test_json_login_post_no_password(self):
        """A post without password should display an error"""
        response = self.client.post(
            self.url, dict(
                username='test'
            ),
            HTTP_ACCEPT='application/json'
        )
        assert response.status_code == 400
        response_json = response.json()
        assert 'password' in response_json['errors']
        assert len(response_json['errors']) == 1

    def test_json_login_post_incorrect(self):
        """A post with incorrect credentials should return an error"""
        response = self.client.post(
            self.url, dict(
                username='test',
                password="bad"
            ),
            HTTP_ACCEPT='application/json'
        )
        assert response.status_code == 400
        response_json = response.json()
        assert '__all__' in response_json['errors']
        assert len(response_json['errors']) == 1

    def test_json_login_post_correct(self):
        """A post with correct credentials should return a 201"""
        response = self.client.post(
            self.url, dict(
                username='test',
                password="test"
            ),
            HTTP_ACCEPT='application/json'
        )
        assert response.status_code == 201
        assert "name" in response.json()
