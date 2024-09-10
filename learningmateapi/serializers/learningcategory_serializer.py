from rest_framework import serializers
from ..models import LearningCategory


class LearningCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningCategory
        fields = ['id', 'name']
