from django.urls import path
from ..views.courses_view import CourseListView

urlpatterns = [
    path('<str:category_name>/', CourseListView.as_view(), name='course-list'),
]
