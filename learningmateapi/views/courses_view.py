import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from learningmateapi.serializers.course_serializer import UdemyCourseSerializer
from learningmateapi.views.base_user_view import BaseUserView
from ..services.udemy_service import UdemyService


class CourseListView(APIView):
    """
    API view to handle fetching a list of courses from the Udemy API based on the category name.
    This endpoint is secured with JWT authentication.
    """

    def get(self, request, category_name):
        """
        Handles GET requests to fetch courses by category name.

        Args:
            request (HttpRequest): The HTTP request object.
            category_name (str): The category name to fetch courses for.

        Returns:
            Response: A DRF Response object containing the list of courses or an error message.
        """
        try:
            # Use the UdemyService to get the courses for the given category name
            courses = UdemyService.get_courses_by_category(category_name)
            # Serialize the courses data using UdemyCourseSerializer
            serializer = UdemyCourseSerializer(courses['results'], many=True)
            
            # Return the serialized data
            return Response(serializer.data, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            # Return a bad request response with the error message if the API call fails
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)