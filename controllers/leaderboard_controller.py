from helpers.leaderboard_data_access import LeaderBoardDataAccess
from views.leaderboard_view import LeaderBoardView


class LeaderBoardController:
    def __init__(self):
        self.view = LeaderBoardView(self)
        self.model = None

    def get_data(self, ordering='DESC'):
        with LeaderBoardDataAccess() as data_access:
            data = data_access.get_all()
            return sorted(data, key=lambda d: -int(d.score) if ordering == 'DESC' else int(d.score))

    def sort_data_asc(self):
        self.view.recreate_tab('ASC')

    def sort_data_desc(self):
        self.view.recreate_tab('DESC')
