from rest_framework import serializers
from .models import Title, Chapter


class SearchSerializer(serializers.Serializer):
    query = serializers.CharField(required=True, max_length=200)


class TitleViewSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)


class ChapterSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    url = serializers.URLField(required=True)

    def create(self, validated_data):
        return Chapter.objects.create(**validated_data)


class TitleUpdateSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True)

    class Meta:
        model = Title
        fields = '__all__'
        read_only_fields = ('last_updated',)

    def create(self, validated_data):
        chapters = validated_data.pop('chapters', [])
        title = Title.objects.create(**validated_data)

        if chapters:
            Chapter.objects.bulk_create([
                Chapter(title=title, **chapter) for chapter in chapters
            ])

        title.save()
        return title

    # def update(self, instance, validated_data):
        # instance.email = validated_data.get('email', instance.email)
        # instance.content = validated_data.get('content', instance.content)
        # instance.created = validated_data.get('created', instance.created)
        # instance.save()
        # return instance
