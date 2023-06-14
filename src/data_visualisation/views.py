from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# from .dataframes import div_plot
from .fpl_api import FPLService
from .visualisation import DataVisualiser

# Create your views here.

def team(request, team_id=None):


    if (not team_id): team_id = request.GET.get('team_id')

    if (not team_id): return render(request, "data_visualisation/team.html")

    FPLServiceTeam = FPLService(team_id=team_id)

    raw_data = FPLServiceTeam.get_season_rank_history()
    manager_data = FPLServiceTeam.get_manager_data()
    
    DataVisualiserTeam = DataVisualiser(raw_data)

    season_history_html_graph = DataVisualiserTeam.create_season_history_line_graph()
    points_on_the_bench = DataVisualiserTeam.create_points_on_the_bench_bar_chart()
    team_value = DataVisualiserTeam.create_team_value_line_graph()

    context = {
        "team_id": team_id,
        "team_name": manager_data['name'],
        "manager_name": f"{manager_data['player_first_name']} {manager_data['player_last_name']}",
        "manager_location": manager_data['player_region_name'],
        "data_visualised": {
            "Season History": season_history_html_graph,
            "Points on the Bench": points_on_the_bench,
            "Team Value": team_value
        }
    }
    return render(request, "data_visualisation/team.html", context)


def home(request):
    return render(request, "data_visualisation/home.html")


def league(request, league_id=None):
    
    context = {}

    return render(request, "data_visualisation/league.html", context)


def players(request, player_id=None):
    

    
    if (not player_id): player_id = request.GET.get('player_id')

    FPLServicePlayer = FPLService(player_id=player_id)

    if (player_id):

        raw_data = FPLServicePlayer.get_player_data()

        DataVisualiserPlayer = DataVisualiser(raw_data)

        player_points_chart = DataVisualiserPlayer.create_player_points_chart()
        g_vs_xg = DataVisualiserPlayer.goals_vs_xgoals()

        context = {
            "data_visualised": {
                "Player Points Chart": player_points_chart,
                "Goals .vs xG": g_vs_xg
            }
        }

    else:

        player_list = FPLService().get_player_list()

        context = {
            "player_list": player_list
        }

    return render(request, "data_visualisation/player.html", context)

