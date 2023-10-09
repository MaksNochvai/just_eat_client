import requests
from decouple import config


class JustEatClient:
    def __init__(self):
        self.base_url = "https://uk.api.just-eat.io/restaurants/bypostcode/"
        self.api_key = config("JUST_EAT_API_KEY")

    def by_postcode(self, postcode):
        try:
            headers = {"Authorization": f"JE-API-KEY {self.api_key}"}
            response = requests.get(f"{self.base_url}{postcode}", headers=headers)
            response.raise_for_status()
            data = response.json()
            restaurants = []

            for restaurant_data in data:
                restaurant = {
                    "name": restaurant_data["name"],
                    "rating": restaurant_data["rating"],
                    "cuisines": restaurant_data["cuisines"],
                }
                restaurants.append(restaurant)

            return restaurants

        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"API request error: {str(e)}")
