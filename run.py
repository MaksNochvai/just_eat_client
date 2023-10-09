from just_eat_client.client import JustEatClient

if __name__ == "__main__":
    client = JustEatClient()
    postcode = "00118"  # Замініть цей поштовий індекс на бажаний
    try:
        restaurants = client.by_postcode(postcode)
        print(restaurants)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
