from django.urls import path
from ..views.learning_categories_views import (
    LearningCategoryAPIView,
)

urlpatterns = [
    path('', LearningCategoryAPIView.as_view(), name='get-all-learning-categories'),
]
