from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from fundoshi import search_series

from .serializers import SearchSerializer


class ListSearchResults(APIView):
    """
    View to search for series by name.
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        """
        Return a list of all matching results.
        """
        serializer = SearchSerializer(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            query = serializer.validated_data['query']
            results = [r for r in search_series(query)]
            return Response(results)
