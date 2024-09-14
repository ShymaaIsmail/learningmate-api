from rest_framework import serializers
from ..models import LearningPlan

class LearningPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningPlan
        fields = ['id', 'user', 'name', 'title', 'start_date', 'end_date', 'description', 'course_links', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']