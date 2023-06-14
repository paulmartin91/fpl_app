from django.urls import path, re_path

from . import views

urlpatterns = [
    path("team/<int:team_id>/", views.team),
    re_path(r"^team/", views.team, {"team_id": None}, name="team"),

    path("league/<int:league_id>/", views.league),
    path("league/", views.league, name="league"),
    
    path("players/<int:player_id>/", views.players),
    re_path(r"^players/", views.players, {"player_id": None}, name="players"),
    
    path("", views.home, name="home")
]