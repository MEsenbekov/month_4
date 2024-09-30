from django.urls import path
from .views import ParserView, FilmListView

urlpatterns = [
    path('films/', FilmListView.as_view(), name='film_list'),
    path('parsing/', ParserView.as_view(), name='parser'),
]
