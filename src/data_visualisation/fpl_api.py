import requests
import pandas as pd

class FPLService():

    def __init__(self, team_id=None, player_id=None):
        self.team_id = team_id
        self.player_id = player_id

    
    def get_season_rank_history(self):
        res = requests.get(f'https://fantasy.premierleague.com/api/entry/{self.team_id}/history/')
        data = res.json()

        return data


    def get_manager_data(self):
        res = requests.get(f'https://fantasy.premierleague.com/api/entry/{self.team_id}/')
        data = res.json()

        return data
    

    def get_player_list(self):
        res = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
        data = res.json()

        df_players = pd.DataFrame(data=data['elements'])
        df_teams = pd.DataFrame(data=data['teams'])
        df_players = df_players.merge(df_teams, left_on='team_code', right_on='code').sort_values(by=['name', 'first_name', 'second_name'])       

        players_grouped = {}

        for index, row in df_players[['first_name', 'second_name', 'id_x', 'name']].iterrows():

            player_object = {
                "first_name": row['first_name'],
                "second_name": row['second_name'],
                "id": row['id_x']
            }

            if (players_grouped.get(row['name'])):
                players_grouped[row['name']].append(player_object)
            else:
                players_grouped[row['name']] = [player_object]

        return players_grouped

        # return dict(tuple(df_players[['first_name', 'second_name', 'id_x', 'name']].groupby('name')))
   

    def get_player_data(self):
        res = requests.get(f"https://fantasy.premierleague.com/api/element-summary/{self.player_id}/")
        data = res.json()

        return data

        