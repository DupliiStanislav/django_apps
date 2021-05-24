from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField
from .models import *

class MovieSerializer(ModelSerializer):
    director = StringRelatedField(read_only=True)
    class Meta:
        model = Movie
        fields = ('title', 'id', 'rating', 'director', 'year')


class MovieSerializer2(ModelSerializer):
    # director = StringRelatedField()
    director = SlugRelatedField(slug_field='last', read_only=True)
    class Meta:
        model = Movie
        fields = ('title', 'director', 'year', 'rating')
