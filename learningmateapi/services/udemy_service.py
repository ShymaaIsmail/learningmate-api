# services/udemy_service.py

import base64
from django.conf import settings
import requests

class UdemyService:
    """
    Service class to interact with the Udemy API.
    """
    BASE_URL = settings.UDEMY_API_CONFIG['BASE_URL']
    
    @staticmethod
    def get_auth_header():
        """Get Encoded Auth Header"""
        credentials = f"{settings.UDEMY_API_CONFIG['CLIENT_ID']}:{settings.UDEMY_API_CONFIG['CLIENT_SECRET']}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        return f"Basic {encoded_credentials}"

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
            'Authorization': UdemyService.get_auth_header(),
            'Content-Type': 'application/json'
        }

        params = {
            'page': 1,
            'page_size': 10,
            'categories': category_name,
            'language': 'en',
            'ordering': 'price-low-to-high'
        }
        url = f"{UdemyService.BASE_URL}/courses/"
        
        response = requests.get(url, headers=headers, params=params)

        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()