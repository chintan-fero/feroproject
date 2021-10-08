from rest_framework import serializers
from Books.models import Book


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)


class BookSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=250)
    release_date = serializers.DateTimeField()
    book_genre = serializers.CharField(max_length=200)
    author = AuthorSerializer(read_only=True)
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.book_genre = validated_data.get('book_genre', instance.toy_category)
#        instance.author_name = validated_data.get('author_name', instance.author.name)
        instance.save()
        return instance
