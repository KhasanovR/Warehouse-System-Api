import base64

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets, authentication, HTTP_HEADER_ENCODING, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory

from warehouse.api.v1.core import DjangoModelPermissions

User = get_user_model()
factory = APIRequestFactory()


def basic_auth_header(username, password):
    credentials = ('%s:%s' % (username, password))
    base64_credentials = base64.b64encode(credentials.encode(HTTP_HEADER_ENCODING)).decode(HTTP_HEADER_ENCODING)
    return 'Basic %s' % base64_credentials


class BasicViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [DjangoModelPermissions]

    def list(self, request, *args, **kwargs):
        return Response({'action': 'list'})

    @action(methods=['get'], detail=False)
    def custom_list(self, request, *args, **kwargs):
        return Response({'action': 'custom_list'})

    @action(methods=['get'], detail=False)
    def custom_undefined_list(self, request, *args, **kwargs):
        return Response({'action': 'custom_undefined_list'})


list_view = BasicViewSet.as_view(actions={
    'get': 'list',
})

custom_list_view = BasicViewSet.as_view(actions=dict(BasicViewSet.custom_list.mapping))

custom_undefined_list_view = BasicViewSet.as_view(actions=dict(BasicViewSet.custom_undefined_list.mapping))


@pytest.fixture(scope='module')
def user_with_perms(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        user = User.objects.create_user('permly_user', 'permly_user@email.com', 'password')
        user.user_permissions.set([
            Permission.objects.get(codename='view_user', content_type=ContentType.objects.get_for_model(User)),
            Permission.objects.create(codename='custom_list_user', content_type=ContentType.objects.get_for_model(User))
        ])
        return user, basic_auth_header('permly_user', 'password')


@pytest.fixture(scope='module')
def user_without_perms(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        user = User.objects.create_user('permless_user', 'permless_user@email.com', 'password')
        return user, basic_auth_header('permless_user', 'password')


@pytest.mark.django_db
def test_list_permissions_unauthorized_when_no_credentials_provided():
    request = factory.get('/', format='json')
    response = list_view(request)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_list_action_success_when_user_is_superuser(user_credentials, user):
    request = factory.get('/', format='json', HTTP_AUTHORIZATION=basic_auth_header(user_credentials['username'],
                                                                                   user_credentials['password']))
    response = list_view(request)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'action': 'list'}


@pytest.mark.django_db
def test_list_action_success_when_user_has_permissions(user_with_perms):
    user, creds = user_with_perms
    request = factory.get('/', format='json', HTTP_AUTHORIZATION=creds)
    response = list_view(request)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'action': 'list'}


@pytest.mark.django_db
def test_list_action_forbidden_when_user_does_not_have_permissions(user_without_perms):
    user, creds = user_without_perms
    request = factory.get('/', format='json', HTTP_AUTHORIZATION=creds)
    response = list_view(request)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_custom_list_action_success_when_user_has_permissions(user_with_perms):
    user, creds = user_with_perms
    request = factory.get('/', format='json', HTTP_AUTHORIZATION=creds)
    response = custom_list_view(request)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'action': 'custom_list'}


@pytest.mark.django_db
def test_custom_list_action_forbidden_when_user_does_not_have_permissions(user_without_perms):
    user, creds = user_without_perms
    request = factory.get('/', format='json', HTTP_AUTHORIZATION=creds)
    response = custom_list_view(request)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_custom_undefined_list_action_forbidden_when_no_permission_is_created_for_that_action(user_with_perms):
    user, creds = user_with_perms
    request = factory.get('/', format='json', HTTP_AUTHORIZATION=creds)
    response = custom_undefined_list_view(request)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    # that's why every new created action in the ViewSet should be added as a new permission to the corresponding model
