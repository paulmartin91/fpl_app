import requests


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
        player_data = [
            {
                "first_name": player['first_name'],
                "second_name": player['second_name'],
                "id": player['id']
            } for player in data['elements']
        ]

        return player_data
   

    def get_player_data(self):
        res = requests.get(f"https://fantasy.premierleague.com/api/element-summary/{self.player_id}/")
        data = res.json()

        return data

        