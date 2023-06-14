import pandas as pd
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go


class DataVisualiser():

    def __init__(self, raw_data):
        self.raw_data = raw_data


    def create_season_history_line_graph(self):
        
        df = pd.DataFrame(data=self.raw_data['current'])

        rank = df[["event", "overall_rank"]]
        rank.set_index("event", inplace=True)

        df = pd.DataFrame(data=self.raw_data["chips"])
        chip = df[['name', 'event']]
        # chip.set_index("event", inplace=True)

        graph = px.line(rank).update_layout(xaxis_title="Gameweek", yaxis_title="Rank")
        graph['layout']['yaxis']['autorange'] = "reversed"

        graph.add_trace(go.Scatter(x=chip['event'],
                            y = chip['event'],
                            mode = 'markers',
                            name = 'chips',
                            hovertemplate = '<b>%{text}</b>',
                            text = chip['name'],
                            ))
        html_graph = plot(graph, output_type="div")
        return html_graph


    def create_points_on_the_bench_bar_chart(self):

        df = pd.DataFrame(data=self.raw_data['current'])
        points_on_the_bench = df[['points_on_bench', 'points', 'event']]
        points_on_the_bench.set_index("event", inplace=True)
        graph = px.bar(points_on_the_bench).update_layout(xaxis_title='Gameweek', yaxis_title='points on the bench')
        html_graph = plot(graph, output_type="div")
        return html_graph


    def create_team_value_line_graph(self):
        
        df = pd.DataFrame(data=self.raw_data['current'])
        team_value = df[["value", "event"]]
        team_value.loc[:, "value"] = team_value["value"].div(10)
        team_value.set_index("event", inplace=True)
        graph = px.line(team_value).update_layout(xaxis_title="Gameweek", yaxis_title="Team Value")
        html_graph = plot(graph, output_type="div")
        return html_graph


    def create_player_points_chart(self):

        df = pd.DataFrame(data=self.raw_data['history'])

        points_per_gw = df[["total_points", "round"]]
        points_per_gw = points_per_gw.groupby("round").sum().reset_index()
        points_per_gw.loc[:, "total_points"] = points_per_gw["total_points"].cumsum()
        points_per_gw.set_index("round", inplace=True)

        graph = px.line(points_per_gw).update_layout(xaxis_title="Gameweek", yaxis_title="Points")

        html_graph = plot(graph, output_type="div")
        return html_graph
    
    def goals_vs_xgoals(self):

        df = pd.DataFrame(data=self.raw_data['history'])

        g_vs_xg = df[["goals_scored", "expected_goals", "round"]]
        g_vs_xg.loc[:, "goals_scored"] = g_vs_xg["goals_scored"].cumsum()
        g_vs_xg.loc[:, "expected_goals"] = g_vs_xg["expected_goals"].astype(float).cumsum()
        # points_per_gw = points_per_gw.groupby("round").sum().reset_index()
        g_vs_xg.set_index("round", inplace=True)

        graph = px.line(g_vs_xg).update_layout(xaxis_title="Gameweek", yaxis_title="Goals/xG")
        html_graph = plot(graph, output_type="div")

        return html_graph