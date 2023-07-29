from django.views.generic import ListView, DetailView
from .models import Post



class NewsListView(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'news'

class NewDetailView(DetailView):
    model = Post
    template_name = 'news/new.html'
    context_object_name = 'new'
