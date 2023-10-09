from unittest.mock import patch, Mock

import pytest
from unittest import mock

from requests import RequestException

from just_eat_client.client import JustEatClient


@pytest.fixture
def mock_response():
    return [
        {
            "name": "Restaurant 1",
            "rating": 4.5,
            "cuisines": ["Italian", "Pizza"]
        },
        {
            "name": "Restaurant 2",
            "rating": 4.2,
            "cuisines": ["Chinese", "Sushi"]
        }
    ]


@mock.patch("just_eat_client.client.requests.get")
def test_by_postcode(mock_get, mock_response):
    mock_get.return_value.json.return_value = mock_response
    mock_get.return_value.status_code = 200

    client = JustEatClient()
    postcode = "00118"
    restaurants = client.by_postcode(postcode)

    assert restaurants == [
        {
            "name": "Restaurant 1",
            "rating": 4.5,
            "cuisines": ["Italian", "Pizza"]
        },
        {
            "name": "Restaurant 2",
            "rating": 4.2,
            "cuisines": ["Chinese", "Sushi"]
        }
    ]

    expected_url = f"https://uk.api.just-eat.io/restaurants/bypostcode/{postcode}"
    mock_get.assert_called_once_with(expected_url, headers=mock.ANY)


@patch('just_eat_client.client.requests.get')
def test_connection_error(mock_get):
    mock_get.side_effect = RequestException("Connection error")
    client = JustEatClient()
    postcode = "00118"
    with pytest.raises(RequestException, match="Connection error"):
        client.by_postcode(postcode)
