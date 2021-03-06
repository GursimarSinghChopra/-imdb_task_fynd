from rest_framework import serializers

from imdb_app.models import Movie, Genre


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('name', 'director', 'score', 'popularity', 'genres')
