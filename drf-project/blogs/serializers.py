from rest_framework import serializers
from .models import Blog, Comment

# Serializer for the Comment model
class CommentSerializer(serializers.ModelSerializer):
    """
    Serializes Comment model data.
    This will convert Comment model instances into JSON and vice versa.
    """
    class Meta:
        model = Comment
        fields = '__all__'  # Includes all fields in the Comment model


# Serializer for the Blog model
class BlogSerializer(serializers.ModelSerializer):
    """
    Serializes Blog model data.
    - Includes related comments using CommentSerializer.
    - 'read_only=True' ensures comments are retrieved but not created/updated through this serializer.
    """
    comments = CommentSerializer(many=True, read_only=True)  # Nested serializer for comments

    class Meta:
        model = Blog
        fields = '__all__'  # Includes all fields in the Blog model
