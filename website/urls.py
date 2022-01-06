from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path("",views.home,name="home"),
  path("aboutus/",views.aboutus,name="aboutus"),
  path("posts/",views.posts,name="posts"),
  path("teams/",views.teams,name="teams"),
  path("teams19/",views.teams19,name="teams19"),
  path("teams21/",views.teams21,name="teams21"),
  path("events/",views.events,name="events"),
   path("events_single/",views.events_single,name="events_single"),
  path("e/<str:event_url>/", views.event_pages,name="event"),
  ]
