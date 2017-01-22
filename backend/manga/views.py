from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from fundoshi import search_series, parse_series

from .serializers import SearchSerializer, TitleViewSerializer


class ListSearchResults(APIView):
    """
    View to search for title by name.
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        """
        Return a list of all matching results.
        """
        serializer = SearchSerializer(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            query = serializer.validated_data['query']
            results = search_series(query)
            return Response(results)


class TitleDetail(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        serializer = TitleViewSerializer(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            url = serializer.validated_data['url']
            title_info = parse_series(url)
            return Response(title_info)
