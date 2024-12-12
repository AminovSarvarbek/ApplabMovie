from django.shortcuts import render
from film.models import Category, Film

def home_view(request):
	categories = Category.objects.all().order_by('-id')
	all_films = Film.objects.all().order_by('-id')
	return render(request, 'home.html', {
		'categories':categories,
		'all_films':all_films
	})


def http404_view(request):
	return render(request, '404.html')