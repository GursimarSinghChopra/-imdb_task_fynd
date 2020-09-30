from rest_framework import viewsets, filters
from imdb_app.serializers import MovieSerializer, GenreSerializer
from imdb_app.models import Movie, Genre
from rest_framework.permissions import IsAuthenticated


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MovieSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('name', 'director', 'score',
                     'popularity', 'genres__name')
    ordering_fields = search_fields
    ordering = '-popularity'


class MovieReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('name', 'director', 'score',
                     'popularity', 'genres__name')
    ordering_fields = search_fields
    ordering = '-popularity'


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GenreSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('name', 'movie__name')
    ordering_fields = search_fields
    ordering = '-name'


class GenreReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('name', 'movie__name')
    ordering_fields = search_fields
    ordering = '-name'


