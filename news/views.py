from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .filters import NewsFilter
from .forms import NewForm


class NewsListView(ListView):
    model = Post
    ordering = '-data_create'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


class SearchNewsListView(ListView):
    queryset = Post.objects.filter(types='NEWS')
    ordering = '-data_create'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewDetailView(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

class NewAddCreateView(CreateView):
    template_name = 'new_add.html'
    form_class = NewForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_types = 'NEWS'
        # post.author = ???
        return super().form_valid(form)

class NewUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'new_edit.html'
    form_class = NewForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class NewDeleteView(DeleteView):
    template_name = 'new_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    context_object_name = 'new'