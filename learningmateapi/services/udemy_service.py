# services/udemy_service.py

from django.conf import settings
import requests

class UdemyService:
    """
    Service class to interact with the Udemy API.
    """
    BASE_URL = settings.UDEMY_API_CONFIG['BASE_URL']
    AUTH_HEADER = settings.UDEMY_API_CONFIG['AUTH_HEADER']

    @staticmethod
    def get_courses_by_category(category_name):
        """
        Fetch courses from the Udemy API based on the category name.

        Args:
            category_name (str): The category name to filter courses.

        Returns:
            dict: A dictionary containing the Udemy API response data.
        """
        headers = {
            'Authorization': f"Basic {UdemyService.AUTH_HEADER}",
            'Content-Type': 'application/json'
        }

        params = {
            'page': 1,
            'page_size': 5,
            'categories': category_name,
            'language': 'en',
            'ordering': 'price-low-to-high'
        }

        response = requests.get(f"{UdemyService.BASE_URL}/courses/", headers=headers, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()