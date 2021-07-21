from django.shortcuts import render
from .models import Movie
import requests

def index(request):

    movie_url='https://api.themoviedb.org/3/movie/popular?api_key=d3b72290034dd8b0a485d50b2ba0c46f'
    
    response=requests.get(movie_url)
    data=response.json()
    movies=data['results'] 
 
    for movie in movies:
        movie_data=Movie(
            title=movie['title'],
            overview =movie['overview'],
            poster_path=movie['poster_path'],
            vote_average=movie['vote_average'],
            vote_count=movie['vote_count']
            )
        saved_data=movie_data.save()
        all_movies=Movie.objects.all()
    return render(request, 'index.html', {"all_movies":all_movies})