from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorListSerializer, MovieListSerializer, ReviewListSerializer, \
                                    DirectorDetailSerializer, MovieDetailSerializer, ReviewDetailSerializer


@api_view(['GET', 'POST'])
def test_view(request):
    print(request.data)
    data = {
        'str': 'loren ipsum',
        'int': 111,
        'float': 99.9,
        'bool': True,
        'list': [
            1, 2, 3
        ]
    }
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def director_list_view(request):
    directors = Director.objects.all()
    serializer = DirectorListSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_list_view(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_list_view(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)
    data = DirectorDetailSerializer(director).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

    data = MovieDetailSerializer(movie).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(review).data
    return Response(data=data)

