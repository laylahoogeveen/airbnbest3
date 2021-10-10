
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('bnb/<int:room_id>', views.accommodation, name='accommodation'),
    path("results", views.results, name="results"),
    path("more_filters", views.more_filters, name="more_filters"),

]

