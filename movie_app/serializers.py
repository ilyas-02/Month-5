from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


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


class DirectorValidateSerializer(serializers.Serializer):
    director = serializers.CharField(min_length=5, max_length=100)


class DirectorObjectSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=100)
    description = serializers.CharField(required=False)
    duration = serializers.FloatField(min_value=1, max_value=1000)
    director = serializers.IntegerField(required=False, allow_null=True, default=None)
    director_obg = DirectorObjectSerializer()
    director_list = serializers.ListField(child=DirectorObjectSerializer())

    def validate_category(self, director):
        if Director.objects.filter(id=director).count() == 0:
            raise ValidationError('Director not found!')
        return director


class MovieObjectSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=False)
    movie = serializers.IntegerField(required=False, allow_null=True, default=None)
    movie_obg = MovieObjectSerializer()
    stars = serializers.FloatField(min_value=1, max_value=5)
    movie_list = serializers.ListField(child=MovieObjectSerializer())

    def validate_movie(self, movie):
        if Movie.objects.filter(id=movie).count() == 0:
            raise ValidationError('Movie not found!')
        return movie



