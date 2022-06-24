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


@api_view(['GET', 'POST'])
def director_list_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorListSerializer(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        director = Director.objects.create(**request.data)
        director.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': 'Director Created!',
                              'director': DirectorDetailSerializer(director).data})


@api_view(['GET', 'POST'])
def movie_list_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':

        movie = Movie.objects.create(**request.data)
        movie.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': 'Movie Created!',
                              'movie': MovieDetailSerializer(movie).data})


@api_view(['GET', 'POST'])
def review_list_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        review = Review.objects.create(**request.data)
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': 'Review Created!',
                              'review': ReviewDetailSerializer(review).data})


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = DirectorDetailSerializer(director).data
        return Response(data=data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        director.name = request.data.get('director', '')
        director.save()
        return Response(data=DirectorDetailSerializer(director).data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = MovieDetailSerializer(movie).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        movie.title = request.data.get('title', '')
        movie.description = request.data.get('description', '')
        movie.duration = request.data.get('duration', 0)
        movie.director_id = request.data.get('director')
        movie.save()
        return Response(data=MovieDetailSerializer(movie).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewDetailSerializer(review).data
        return Response(data=data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        review.text = request.data.get('text', '')
        review.movie_id = request.data.get('movie')
        review.stars = request.data.get('stars', 0)
        review.save()
        return Response(data=ReviewDetailSerializer(review).data)

