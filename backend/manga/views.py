from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from fundoshi import search_series, parse_series, parse_chapter

from .models import Title, Chapter
from .serializers import (
    SearchSerializer, TitleViewSerializer, TitleSerializer,
    ChapterViewSerializer, ChapterSerializer
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
                update_serializer = TitleSerializer(data=title_info)
                if update_serializer.is_valid(raise_exception=True):
                    update_serializer.save()
                return Response(update_serializer.validated_data)

            elif title.is_old:
                title_info = parse_series(url)
                title_info['url'] = url
                update_serializer = TitleSerializer(title, data=title_info)
                if update_serializer.is_valid():
                    update_serializer.save()
                return Response(update_serializer.validated_data)

            else:
                return Response(TitleSerializer(title).data)


class ChapterDetail(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=True):
        serializer = ChapterViewSerializer(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            url = serializer.validated_data['url']
            try:
                chapter = Chapter.objects.get(url=url)
                if not chapter.is_old:
                    return Response(ChapterSerializer(chapter).data)
                else:
                    return _update_chapter(chapter)
            except ObjectDoesNotExist:
                return _create_chapter(url)


def _create_chapter(url):
    chapter_data = parse_chapter(url)
    chapter_data['url'] = url
    title = Title.objects.get(url=chapter_data.series_url).pk
    chapter_data['title'] = title
    chapter_serializer = ChapterSerializer(data=chapter_data)
    if chapter_serializer.is_valid(raise_exception=True):
        chapter_serializer.save()
        return Response(chapter_serializer.data)


def _update_chapter(chapter):
    chapter_data = parse_chapter(chapter.url)
    chapter_serializer = ChapterSerializer(chapter,
                                           data=chapter_data,
                                           partial=True)
    if chapter_serializer.is_valid(raise_exception=True):
        chapter_serializer.save()
        return Response(chapter_serializer.data)
