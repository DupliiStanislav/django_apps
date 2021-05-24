from  django.urls import path
from .views import *

app_name = 'imdb'

urlpatterns = [
    path('', index, name='index'),
    path('movie/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('director/<int:pk>', DirectorDetailView.as_view(), name='director_detail'),
    path('movie/comment/<int:pk>/', movie_comment_create, name='movie_comment_create'),
    path('movies/all/', MovieListView.as_view(), name='movie_list'),
    path('directors/all/', DirectorListView.as_view(), name='director_list'),
    path('movies/best/', best_movie_list, name='best_movie_list'),
    path('search/', search, name='search'),
    path('config/', config, name='config'),
    path('add/director/', add_new_director, name='add_new_director'),
    path('add/movie/', add_new_movie, name='add_new_movie'),
    path('api/movies/all/', MovieListAPIView.as_view(), name='api_movie_list'),
    path('api/movie/<int:pk>/', MovieDetailAPIView.as_view(), name='api_movie_detail'),
]