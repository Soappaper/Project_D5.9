from django.urls import path
from .views import NewsListView, NewDetailView


urlpatterns = [
   path('', NewsListView.as_view()),
   path('<int:pk>', NewDetailView.as_view(), name='new'),

]