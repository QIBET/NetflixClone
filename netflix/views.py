from django.shortcuts import render
from .models import Movie
import requests

def index(request):
    title = "Netflix Clone Application"

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
    return render(request, 'index.html', {"all_movies":all_movies,"title":title})

""" def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key=d3b72290034dd8b0a485d50b2ba0c46f&language=en-US&page=1&include_adult=false'
   
    search_movie_response=requests.get(search_movie_url)
    data=search_movie_response.json()
    searched_movies=data['results'] 

    if search_movie_response['results']:
        search_movie_list = search_movie_response['results']
        
    return render(request, 'search.html', search_movie_list """

def search_movies(request):
  
    if 'search_movie' in request.GET and request.GET['search_movie']:
        searched_term= request.GET.get('search_movie')
        search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key=d3b72290034dd8b0a485d50b2ba0c46f&language=en-US&page=1&include_adult=false'
        url = search_movie_url.format(type = 'movie', search_term = searched_term)
        results = requests.get(url)
        results_returned = results.json()
        title = results_returned['original_title']
        context = {
        'results':results_returned,
        'movie_title':title
        }

        return render(request, 'search_results.html',context)