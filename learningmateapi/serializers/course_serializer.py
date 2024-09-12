# serializers.py

from rest_framework import serializers

class CourseSerializer(serializers.Serializer):
    """
    Base serializer for course data.
    """
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    url = serializers.URLField()
    price = serializers.CharField(max_length=50)
    rating = serializers.FloatField()
    image_url = serializers.URLField()
    description = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Course` instance, given the validated data.
        """
        return validated_data

    def update(self, instance, validated_data):
        """
        Update and return an existing `Course` instance, given the validated data.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        return instance


class UdemyCourseSerializer(CourseSerializer):
    """
    Serializer for Udemy-specific course data, inheriting from CourseSerializer.
    Adds a fixed 'source' field with value 'Udemy'.
    """
    source = serializers.CharField(default="Udemy")