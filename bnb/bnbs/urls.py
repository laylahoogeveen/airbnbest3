
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.index, name="index"),
    path('<int:room_id>', views.accommodation, name='accommodation'),
    path("results", views.results, name="results"),
    path("more_filters", views.more_filters, name="more_filters"),

]

