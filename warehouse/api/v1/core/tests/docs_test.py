import pytest
from django.urls import reverse


@pytest.mark.django_db
@pytest.mark.api_docs
@pytest.mark.api_docs_v1
def test_api_docs_public_access_success(tenant_public_api_client):
    response = tenant_public_api_client.get(path=reverse('openapi-schema-v1', urlconf='warehouse.public_urls'),
                                            format='json')
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.api_docs
@pytest.mark.api_docs_v1
def test_api_docs_public_access_unauthorized(tenant_public_api_client):
    tenant_public_api_client.logout()
    response = tenant_public_api_client.get(path=reverse('openapi-schema-v1', urlconf='warehouse.public_urls'),
                                            format='json')
    assert response.status_code == 401


@pytest.mark.django_db
@pytest.mark.api_docs
@pytest.mark.api_docs_v1
def test_api_docs_public_not_superuser_forbidden(tenant_public_api_client, public_user):
    public_user.is_superuser = False
    public_user.save()
    response = tenant_public_api_client.get(path=reverse('openapi-schema-v1', urlconf='warehouse.public_urls'),
                                            format='json')
    assert response.status_code == 403


@pytest.mark.django_db
@pytest.mark.api_docs
@pytest.mark.api_docs_v1
def test_api_docs_tenant_access_not_found(tenant_test_api_client):
    response = tenant_test_api_client.get(path=reverse('openapi-schema-v1', urlconf='warehouse.public_urls'),
                                          format='json')
    assert response.status_code == 404
