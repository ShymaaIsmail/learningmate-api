from django.urls import path
from ..views.auth_views import UserAuthView, UserLogoutView

urlpatterns = [
    path('login/', UserAuthView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
]
