from django.urls import path
from .views import (
	home_view,
	http404_view
)

app_name = 'main'
urlpatterns = [
	path('', home_view, name='home'),
	path('404', http404_view, name='404'),
]