# myapp/views.py
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.timezone import now
from learningmateapi.models.user import User
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UserAuthView(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'google_token': openapi.Schema(type=openapi.TYPE_STRING, description='Google OAuth2 token'),
            },
            required=['google_token'],
        ),
        responses={
            200: openapi.Response(
                description='Successful authentication',
                examples={
                    'application/json': {
                        'token': 'string'
                    }
                }
            ),
            400: openapi.Response(
                description='Invalid or missing token',
                examples={
                    'application/json': {
                        'error': 'Token is required'
                    }
                }
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        google_token = request.data.get('google_token')
        if not google_token:
            return Response({'error': 'google_token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Verify the Google token
            id_info = id_token.verify_oauth2_token(google_token, requests.Request())
            
            # Extract user information
            google_user_id = id_info['sub']
            email = id_info['email']
            name = id_info.get('name', '')
            given_name = id_info.get('given_name', '')
            family_name = id_info.get('family_name', '')

            # Create or update user record in the database
            user, created = User.objects.get_or_create(
                google_user_id=google_user_id,
                defaults={
                    'username': name ,
                    'email': email,
                    'first_name': given_name,
                    'last_name': family_name,
                }
            )
            if created:
                user.set_unusable_password()
            user.last_login = now()
            user.save()

            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            return Response({'token': str(refresh.access_token)}, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
