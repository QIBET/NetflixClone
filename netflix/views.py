from django.shortcuts import render

# Create your views here.
def index(request):
    title = "Netflix Clone Application"

    return render(request,'index.html',{"title":title})