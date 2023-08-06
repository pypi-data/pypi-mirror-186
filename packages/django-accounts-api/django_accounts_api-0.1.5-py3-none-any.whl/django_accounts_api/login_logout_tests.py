from django.forms import Form
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginCheckTestCase(TestCase):
    """Basic tests of the login check endpoint"""

    def setUp(self) -> None:
        """Get the url and create a user"""
        self.url = reverse("django_accounts_api:login_check")
        self.user = User.objects.create_user("test")
        return super().setUp()

    def test_get_login_not_authenticated(self):
        """Just hitting this endpoint with no login should return 401"""
        response = self.client.get(self.url)
        assert response.status_code == 401

    def test_get_login_authenticated(self):
        """hitting this endpoint with login should return 200"""
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        assert response.status_code == 200
        assert "name" in response.json()


class LogoutTestCase(TestCase):
    """Basic tests of the logout endpoint"""

    def setUp(self) -> None:
        """Get the url and create a user"""
        self.url = reverse("django_accounts_api:logout")
        self.user = User.objects.create_user("test")
        self.client.force_login(self.user)
        return super().setUp()

    def test_get_logout(self):
        """Just getting this endpoint with no login should return 200"""
        response = self.client.get(self.url)
        assert response.status_code == 200

    def test_post_logout(self):
        """posting to this endpoint with login should return 200"""
        test = self.client.force_login(self.user)
        response = self.client.post(self.url)
        assert response.status_code == 200


class LoginViewTestCase(TestCase):
    """Basic tests of the partial HTML login view"""

    def setUp(self) -> None:
        """Get the url and create a user"""
        self.url = reverse("django_accounts_api:login")
        self.user = User.objects.create_user("test", password="test")
        return super().setUp()

    def test_get_login(self):
        """An unauthed get should return a form"""
        response = self.client.get(self.url)
        assert response.status_code == 200
        assert "Content-Type" in response.headers
        assert response.headers["Content-Type"].startswith("text/html")
        assert "form" in response.context

    def test_post_login_empty_form(self):
        """A post without username and password should display errors"""
        response = self.client.post(
            self.url, {})
        assert response.status_code == 200
        assert "form" in response.context
        form: Form = response.context["form"]
        assert 'username' in form.errors
        assert 'password' in form.errors
        assert "Content-Type" in response.headers
        assert response.headers["Content-Type"].startswith("text/html")

    def test_post_login_no_password(self):
        """A post without password should display an error"""
        response = self.client.post(
            self.url, dict(
                username='test'
            ))
        assert response.status_code == 200
        assert "form" in response.context
        form: Form = response.context["form"]
        assert 'password' in form.errors
        assert len(form.errors) == 1
        assert "Content-Type" in response.headers
        assert response.headers["Content-Type"].startswith("text/html")

    def test_post_login_incorrect(self):
        """A post with incorrect credentials should display an error"""
        response = self.client.post(
            self.url, dict(
                username='test',
                password="bad"
            ))
        assert response.status_code == 200
        assert "form" in response.context
        form: Form = response.context["form"]
        assert '__all__' in form.errors
        assert len(form.errors) == 1
        assert "Content-Type" in response.headers
        assert response.headers["Content-Type"].startswith("text/html")

    def test_post_login_correct(self):
        """A post with incorrect credentials should return a 201"""
        response = self.client.post(
            self.url, dict(
                username='test',
                password="test"
            ))
        assert response.status_code == 201
        assert "name" in response.json()
        assert "Content-Type" in response.headers
        assert response.headers["Content-Type"].startswith("application/json")


class LoginFlowTestCase(TestCase):
    """A flow test of the login endpoints"""

    def setUp(self) -> None:
        """Get the url and create a user"""
        self.logout_url = reverse("django_accounts_api:logout")
        self.check_url = reverse("django_accounts_api:login_check")
        self.url = reverse("django_accounts_api:login")
        self.user = User.objects.create_user("test", password="test")
        return super().setUp()

    def test_login_logout_flow(self):
        """ user should be unauthed, login, then be authed, then hit log out, then be unauthed"""
        response = self.client.get(self.check_url)
        assert response.status_code == 401
        response = self.client.post(
            self.url, dict(
                username='test',
                password="test"
            ))
        assert response.status_code == 201
        response = self.client.get(self.check_url)
        assert response.status_code == 200
        response = self.client.post(self.logout_url)
        assert response.status_code == 200
        response = self.client.get(self.check_url)
        assert response.status_code == 401
