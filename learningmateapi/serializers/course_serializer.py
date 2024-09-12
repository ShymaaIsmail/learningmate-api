from django.conf import settings
from rest_framework import serializers

class CourseSerializer(serializers.Serializer):
    """
    Base serializer for course data.
    """
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    url = serializers.URLField()
    price = serializers.CharField(max_length=50)
    image_480x270 = serializers.URLField()
    headline = serializers.CharField()

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
    source = serializers.SerializerMethodField()

    def get_source(self, obj):
        """
        Return a fixed value for the 'source' field.

        Args:
            obj (dict): The course instance.

        Returns:
            str: The fixed source value.
        """
        return "Udemy"

    def to_representation(self, instance):
        """
        Convert the instance to a dictionary, including the 'source' field.

        Args:
            instance (dict): The instance to convert.

        Returns:
            dict: The serialized representation.
        """
        # Get the representation from the parent serializer
        representation = super().to_representation(instance)
        # Add the 'source' field to the representation
        representation['source'] = self.get_source(instance)
        if 'url' in representation and not representation['url'].startswith('http'):
            representation['url'] = settings.UDEMY_API_CONFIG['WEBSITE_URL'] + representation['url']
        return representation