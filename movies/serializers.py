from rest_framework import serializers

from movies.models import Movie, Director, Genre


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'director_name', 'preview', 'director', 'genre')


class MovieRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
