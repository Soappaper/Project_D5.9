from django.urls import path
from .views import NewsListView, NewDetailView, SearchNewsListView, NewAddCreateView, NewUpdateView, NewDeleteView
from django.contrib.auth.views import LoginView

urlpatterns = [
   path('', NewsListView.as_view()),
   path('<int:pk>', NewDetailView.as_view(), name='new'),
   path('search/', SearchNewsListView.as_view()),
   path('add/', NewAddCreateView.as_view(), name='new_add'),
   path('edit/<int:pk>', NewUpdateView.as_view(), name='new_edit'),
   path('delete/<int:pk>', NewDeleteView.as_view(), name='new_delete'),
   path('article/create/', NewAddCreateView.as_view(), name='article_create'),
   path('article/<int:pk>/edit', NewUpdateView.as_view(), name='article_edit'),
   path('article/<int:pk>/delete', NewDeleteView.as_view(), name='article_delete'),
   path('login/', LoginView.as_view(template_name="login.html"), name='login'),
]