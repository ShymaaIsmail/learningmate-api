from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import LearningCategory
from ..serializers import LearningCategorySerializer


class LearningCategoryAPIView(APIView):

    def get(self, request):
        learning_categories = LearningCategory.objects.all()
        serializer = LearningCategorySerializer(learning_categories, many=True)
        return Response(serializer.data)
