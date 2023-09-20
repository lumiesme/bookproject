from django.urls import path
from .import views

app_name = 'booksapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),  # Home View
    path('country_list', views.CountryListView.as_view(), name='country_list'),  # country list view
    path('country_create', views.CountryCreateView.as_view(), name='country_create'),  # country create view
    path('country_update <int:pk>', views.CountryUpdateView.as_view(), name='country_update'),  # country update view

    path('language_list', views.LanguageListView.as_view(), name='language_list'),  # language list view
    path('language_create', views.LanguageCreateView.as_view(), name='language_create'),  # language create view
    path('language_update <int:pk>', views.LanguageUpdateView.as_view(), name='language_update'),  # language create view

    path('author_list', views.AuthorListView.as_view(), name='author_list'),  # author list view
    path('author_create', views.AuthorCreateView.as_view(), name='author_create'),  # author create view
    path('author_update <int:pk>', views.AuthorUpdateView.as_view(), name='author_update'),  # author update view

    path('book_list', views.BookListView.as_view(), name='book_list'),  # book list view
    path('book_create', views.BookCreateView.as_view(), name='book_create'),  # book create view
    path('book_update <int:pk>', views.BookUpdateView.as_view(), name='book_update'),  # book update view
]