from django.urls import path
from .views import (
	detail_movie,
	search_movie
)

app_name = 'film'
urlpatterns = [
	path('<int:film_id>', detail_movie, name='detail_movie'),
	path('search', search_movie, name='search'),
]