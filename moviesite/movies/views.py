from django.shortcuts import render
# Create your views here.
from.models import Movie

def about_view(request):

	return render(request,"about.html")

def index(request):
    movie_all=Movie.objects.all()
    return render(request,'index.html',{'movies':movie_all})
    