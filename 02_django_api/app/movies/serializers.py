from movies.models import FilmWork
from rest_framework import serializers


class MovieSerialize(serializers.ModelSerializer):
    class Meta:
        model = FilmWork
        fields = ('id', 'title', 'description', 'creation_date', 'file_path', 'rating', 'type')
