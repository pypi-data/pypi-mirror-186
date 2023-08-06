from typing import Any
from django.views.generic import View
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls.exceptions import NoReverseMatch
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters


class AcceptJsonMixin:
    """
    Adds method to detect if JSON was requested in the Accept header
    """

    def json_response_requested(self: View) -> bool:
        """ does the request want JSON content back?"""
        if "HTTP_ACCEPT" in self.request.META:
            return self.request.META["HTTP_ACCEPT"] == "application/json"
        return False


def manifest(request: HttpRequest) -> HttpResponse:
    """Return a json encoded dictionary {name: path} for views offered
    by Django Accounts API

    :param request: the Django http request
    :type request: HttpRequest
    :return: json encoded name: path dictionary
    :rtype: HttpResponse
    """
    return JsonResponse(dict(
        login=reverse("django_accounts_api:login"),
        logout=reverse("django_accounts_api:logout"),
        password_change=reverse("django_accounts_api:password_change"),
    ))


def _user_details(user: DjangoUser) -> dict:
    """The details of the user to return on success"""
    return dict(
        id=user.pk,
        name=user.get_full_name(),
    )


def login_check(request) -> HttpResponse:
    """
    Deprecated (use Login view with Accept application/json)
    200 and details if logged in, 401 if not
    """
    user: DjangoUser = request.user
    if (user.is_authenticated):
        return JsonResponse(_user_details(user))
    else:
        return HttpResponse(status=401)


@method_decorator(sensitive_post_parameters(), name='dispatch')
class Login(AcceptJsonMixin, LoginView):
    '''
    Override the Django login view to be API friendly for json or partial html
    '''
    template_name = "django_accounts_api/login.html"

    def form_valid(self, form):
        """Override redirect behavior to return JSON user details"""
        _repressed_redirect = super().form_valid(form)
        return JsonResponse(
            _user_details(self.request.user),
            status=201
        )

    def form_invalid(self, form):
        """Override redirect behavior if json is requested return json errors"""
        if self.json_response_requested():
            return JsonResponse(dict(errors=form.errors), status=400)
        else:
            return super().form_invalid(form)

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        """Override the get behavior if json requested return user details"""
        if self.json_response_requested():
            if (request.user.is_authenticated):
                return JsonResponse(_user_details(request.user))
            else:
                return HttpResponse(status=401)
        else:
            return super().get(request, *args, **kwargs)


class Logout(LogoutView):
    ''' Override the Django logout view to NOT redirect on successful login
    GET - actually calls POST, but will error in Django 5
    POST - logs out, returns 200
    '''

    def post(self, request, *args, **kwargs):
        _repressed_redirect_or_render = super().post(request, *args, **kwargs)
        return HttpResponse(
            status=200
        )


@method_decorator(sensitive_post_parameters(), name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class PasswordChange(AcceptJsonMixin, PasswordChangeView):
    ''' Override the Django change password view to support API use
    GET - renders a partial change password form - can be accessed without auth
    '''
    template_name = "django_accounts_api/password_change.html"

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        """Django's PasswordChangeView is login required and redirects, we suppress this and 401"""
        if not request.user.is_authenticated:
            return HttpResponse(status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        """Override the get behavior if json requested return user details"""
        if request.user.is_authenticated:
            if (self.json_response_requested()):
                return JsonResponse(_user_details(request.user))
            else:
                return super().post(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        if self.json_response_requested():
            if self.request.user.is_authenticated:
                return super().post(*args, **kwargs)
        else:
            return super().post(*args, **kwargs)

    def form_invalid(self, form):
        """Override redirect behavior if json is requested return json errors"""
        if self.json_response_requested():
            return JsonResponse(dict(errors=form.errors), status=400)
        else:
            return super().form_invalid(form)

    def form_valid(self, form):
        try:
            _repressed_redirect = super().form_valid(form)
        except NoReverseMatch:
            pass
        return HttpResponse(status=200)
