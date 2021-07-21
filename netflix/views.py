from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    title = "Netflix Clone Application"
    response = requests.get('https://api.themoviedb.org/3/movie/550?api_key=3d0384b337f97fac152e1083e54e76e2')
    # transfor the response to json objects
    results = response.json()

    return render(request,'index.html',{"results":results,"title":title})