import pytest

from warehouse.account.models import User
from warehouse.core.models import (
    Product,
    Material,
    ProductMaterial,
    Warehouse
)


@pytest.fixture(scope='session')
def user_credentials():
    return {
        'username': 'tester',
        'password': 'test12345'
    }


@pytest.fixture(scope='session')
def user(django_db_setup, django_db_blocker, user_credentials):
    with django_db_blocker.unblock():
        user = User.objects.create(username=user_credentials['username'], is_superuser=True)
        user.set_password(user_credentials['password'])
        user.save()
        return user


@pytest.fixture(scope='session')
def public_user(django_db_setup, django_db_blocker, user_credentials):
    with django_db_blocker.unblock():
        user = User.objects.create(username=user_credentials['username'], is_superuser=True)
        user.set_password(user_credentials['password'])
        user.save()
        return user


@pytest.fixture(scope='module')
def product(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        product = Product.objects.create(name='Test', code='123456')
        return product


@pytest.fixture(scope='module')
def material(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        material = Material.objects.create(name='Test')
        return material


@pytest.fixture(scope='module')
def product_material(django_db_setup, django_db_blocker, product, material):
    with django_db_blocker.unblock():
        product_material = ProductMaterial.objects.create(product=product, material=material, quantity=5)
        return product_material


@pytest.fixture(scope='module')
def warehouse(django_db_setup, django_db_blocker, material):
    with django_db_blocker.unblock():
        warehouse = Warehouse.objects.create(material=material, reminder=5, price=300)
        return warehouse
