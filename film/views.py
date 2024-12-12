from django.shortcuts import render
from django.db.models import Q
from .models import Film
from main.utils import custom_http404

def detail_movie(request, film_id):
	try:
		film = Film.objects.get(id=film_id)
		suggest_films = Film.objects.filter(categories__in=film.categories.all()).exclude(id=film.id).distinct()
		return render(request, 'film/detail.html', {'film':film, 'suggest_films':suggest_films[0:4]})
	except Film.DoesNotExist:
		return custom_http404()


def search_movie(request):
    text = request.GET.get('search', '')  # Default to an empty string if no search term is provided
    films = Film.objects.filter(Q(title__icontains=text) | Q(description__icontains=text))

    return render(request, 'film/search.html', {'films': films, 'search_text': text})
