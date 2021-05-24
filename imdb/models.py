from django.db import models
from django.urls import reverse
import datetime


class Director(models.Model):
    last = models.CharField(max_length=30)
    first = models.CharField(max_length=30)
    img = models.ImageField(null=True, blank=True, upload_to='directors/')

    def __str__(self):
        return f'{self.first} {self.last}'

    def avg_rating(self):
        rates = [m.rating for m in self.movies.all()]
        if not rates:
            return 0.0
        return round(sum(rates) / len(rates), 1)


    def best_movie(self):
        if not self.movies.all():
            return None
        elif len(self.movies.all()) == 1:
            return None
        else:
            return self.movies.all().order_by('-rating')[0]


    class Meta:
        ordering = ['last', 'first']


    def get_absolute_url(self):
        return reverse('imdb:director_detail', args=(self.id,))


class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField(null=True, blank=True)
    director = models.ForeignKey(Director, blank=True, null=True,
                                 on_delete=models.SET_NULL, related_name='movies')
    img = models.ImageField(null=True, blank=True, upload_to='movies/')
    plot = models.FileField(null=True, blank=True, upload_to='plots/', max_length=200)
    rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('imdb:movie_detail', args=(self.id,))

    class Meta:
        ordering = ['title']

class MovieComment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='comments')
    text = models.TextField()
    author = models.CharField(max_length=50)
    date_time = models.DateTimeField(default=datetime.datetime.now)


    def __str__(self):
        dt = self.date_time.strftime('%d.%m.%y %H:%M')
        return f'"{self.text}" by ({self.author}) ({dt})'

    class Meta:
        ordering = ['-date_time']