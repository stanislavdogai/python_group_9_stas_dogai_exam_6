from django.urls import path

from webapp.views import home_page, first_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('first/', first_page, name='first_page')
]