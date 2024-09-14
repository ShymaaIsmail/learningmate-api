from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from learningmateapi.views.base_user_view import BaseUserView

from ..models import LearningPlan
from ..serializers import LearningPlanSerializer


class LearningPlanListView(BaseUserView):
    """
    API view to handle listing and creating learning plans for the authenticated user.
    This endpoint is secured with JWT authentication.
    """

    def get(self, request):
        """
        List all learning plans for the authenticated user.
        """
        learning_plans = LearningPlan.objects.filter(user=request.user)
        serializer = LearningPlanSerializer(learning_plans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new learning plan for the authenticated user.
        """
        serializer = LearningPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Associate the user with the learning plan
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LearningPlanDetailView(BaseUserView):
    """
    API view to handle retrieving, updating, and deleting a specific learning plan.
    This endpoint is secured with JWT authentication.
    """

    def get_object(self, user, pk):
        """
        Helper method to get the learning plan for the authenticated user.
        """
        return get_object_or_404(LearningPlan, pk=pk, user=user)

    def get(self, request, pk):
        """
        Retrieve a specific learning plan by ID.
        """
        learning_plan = self.get_object(request.user, pk)
        serializer = LearningPlanSerializer(learning_plan)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Update a specific learning plan by ID.
        """
        learning_plan = self.get_object(request.user, pk)
        serializer = LearningPlanSerializer(learning_plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific learning plan by ID.
        """
        learning_plan = self.get_object(request.user, pk)
        learning_plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)