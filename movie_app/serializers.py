from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class DirectorListSerializer(serializers.ModelSerializer):
    movies_count = MovieListSerializer(many=True)

    class Meta:
        model = Director
        fields = 'id name movies_count'.split()


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewListSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id rating title description duration reviews'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


