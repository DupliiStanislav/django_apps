from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.detail import DetailView
from .models import *
from django.views.generic.list import ListView
from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .forms import *
from .serializers import *

def index(request):
    context = {
        'all_movies': Movie.objects.all()[:4],
        'best_movies': Movie.objects.order_by('-rating')[:4],
        'directors': sorted(Director.objects.all(), key=lambda x: -x.avg_rating())[:4],
    }
    return render(request, 'imdb/index.html', context)


class MovieDetailView(DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MovieCommentCreateForm()
        return context

class DirectorDetailView(DetailView):
    model = Director


class MovieListView(ListView):
    model = Movie

class DirectorListView(ListView):
    model = Director


def best_movie_list(request):
    context = {
        'object_list': Movie.objects.order_by('-rating')[:8],
    }
    return render(request, 'imdb/best_movie_list.html', context)


def config(request):
    context = {
        'director_model_form': DirectorModelForm(),
        'movie_model_form': MovieModelForm(),
    }
    return render(request, 'imdb/config.html', context)


def add_new_director(request):
    form = DirectorModelForm(request.POST)
    saved = form.save(commit=False)
    saved.img = request.FILES['img']
    saved.save()
    return HttpResponseRedirect(reverse('imdb:director_list'))


def add_new_movie(request):
    form = MovieModelForm(request.POST)
    saved = form.save(commit=False)
    saved.img = request.FILES['img']
    saved.save()
    return HttpResponseRedirect(reverse('imdb:movie_list'))


def movie_comment_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    try:
        text = request.POST.get('text')
        author = request.POST.get('author')
        if text and author:
            new_comment = MovieComment(
                movie=movie,
                text=text, author=author,
            )
            new_comment.save()
    except:
        print('Problem with creating new comment')
    finally:
        return HttpResponseRedirect(movie.get_absolute_url())



def search(request):
    try:
        search = request.POST.get('search')
        # movies = [m for m in Movie.objects.all() if search.lower() in m.title.lower()]
        movies = Movie.objects.filter(title__icontains=search)
        directors = Director.objects.filter(Q(first__icontains=search) | Q(last__icontains=search))
        context = {
            'search': search,
            'movies': movies,
            'directors': directors,
        }
        return render(request, 'imdb/searching.html', context)
    except:
        print('WRONG!!')
        return redirect(reverse('imdb:index'))


#------------------------------------------------------------------


class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer2







