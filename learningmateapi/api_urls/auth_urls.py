from django.urls import path
from ..views.auth_views import UserAuthView

urlpatterns = [
    path('login/', UserAuthView.as_view(), name='user_login'),
    path('logout/', UserAuthView.as_view(), name='user_logout'),
]
