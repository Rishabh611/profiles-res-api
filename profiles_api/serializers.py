from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name for API view"""
    name = serializers.CharField(max_length = 10)