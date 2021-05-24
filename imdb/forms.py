from django.forms import Form, Textarea, CharField, ModelForm
from .models import *

class MovieCommentCreateForm(Form):
    author = CharField(label='author', max_length=50)
    text = CharField(label='comment', max_length=200, widget=Textarea)


class DirectorModelForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'


class MovieModelForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
