
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('bnb/<int:room_id>', views.bnb, name='accommodation'),
    path("results", views.results, name="results"),
    # path('text/<str:author>/<str:text>/<int:book_num>', views.results, name='results'),
]

