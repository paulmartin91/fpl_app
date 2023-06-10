import requests


class FPLService():

    def __init__(self, team_id):
        self.team_id = team_id

    
    def get_season_rank_history(self):
        res = requests.get(f'https://fantasy.premierleague.com/api/entry/{self.team_id}/history/')
        data = res.json()

        return data

    def get_manager_data(self):
        res = requests.get(f'https://fantasy.premierleague.com/api/entry/{self.team_id}/')
        data = res.json()

        return data
        