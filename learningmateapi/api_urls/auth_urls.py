from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from ..views.auth_views import UserAuthView

urlpatterns = [
    path('user/login/', UserAuthView.as_view(), name='user_login'),
    path('user/logout/', UserAuthView.as_view(), name='user_logout'),
]
