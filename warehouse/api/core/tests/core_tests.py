import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
@pytest.mark.management
@pytest.mark.receipt
@pytest.mark.receipt_accept
def test_process_works(api_client, product):
    data = {
        'request': [
            {
                'product': {
                    'id': product.id,
                },
                'quantity': 2,
            }
        ]
    }
    response = api_client.post(reverse('v1:pharmacy_cloud.management:results-process'),
                               data,
                               content_type='application/json')
    assert response.status_code == 200
