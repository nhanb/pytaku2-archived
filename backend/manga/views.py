from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from fundoshi import search_series, parse_series

from .models import Title
from .serializers import (
    SearchSerializer, TitleViewSerializer, TitleUpdateSerializer
)


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

            try:
                title = Title.objects.get(url=url)
                already_created = True
            except Title.DoesNotExist:
                already_created = False

            if not already_created:
                title_info = parse_series(url)
                title_info['url'] = url
                update_serializer = TitleUpdateSerializer(data=title_info)
                if update_serializer.is_valid(raise_exception=True):
                    update_serializer.save()
                return Response(update_serializer.validated_data)

            elif (now() - title.last_updated).days >= 1:
                title_info = parse_series(url)
                title_info['url'] = url
                update_serializer = TitleUpdateSerializer(title,
                                                          data=title_info)
                if update_serializer.is_valid():
                    update_serializer.save()
                return Response(update_serializer.validated_data)

            else:
                return Response(TitleUpdateSerializer(title).data)
