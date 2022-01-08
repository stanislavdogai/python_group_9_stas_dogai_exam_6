from django.urls import path

from webapp.views import home_page, create_book_view, book_update, book_delete

urlpatterns = [
    path('', home_page, name='home_page'),
    path('create/', create_book_view, name='create_page'),
    path('book/<int:pk>/update', book_update, name="book_update"),
    path('book/<int:pk>/delete', book_delete, name="book_delete")
]