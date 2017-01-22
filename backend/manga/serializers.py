from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    query = serializers.CharField(required=True, max_length=200)
