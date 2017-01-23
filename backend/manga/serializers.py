from rest_framework import serializers
from .models import Title, Chapter


class SearchSerializer(serializers.Serializer):
    query = serializers.CharField(required=True, max_length=200)


class TitleViewSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)


class ChapterViewSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = '__all__'
        read_only_fields = ('last_updated',)


class ChapterSerializer(serializers.ModelSerializer):
    title = serializers.PrimaryKeyRelatedField(queryset=Title.objects.all())
    title_data = serializers.SerializerMethodField()
    adjacent_chapters = serializers.SerializerMethodField()

    def get_title_data(self, obj):
        title = obj.title
        return {
            'url': title.url,
            'name': title.name,
        }

    def get_adjacent_chapters(self, obj):
        chapters = obj.title.chapters
        prev, next = None, None

        # Application-level query. Longest title that I know of has around
        # 900-something chapters (good job Aoyama sensei) so it's not that bad.
        for index, chapter in enumerate(chapters):
            if chapter['url'] == obj.url:
                if index > 0:
                    prev = chapters[index - 1]
                if index < len(chapters) - 1:
                    next = chapters[index + 1]
                break

        return {
            'previous': prev,
            'next': next,
        }

    class Meta:
        model = Chapter
        fields = '__all__'
        read_only_fields = ('last_updated',)
