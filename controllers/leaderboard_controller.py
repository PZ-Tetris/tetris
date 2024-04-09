from helpers.leaderboard_data_access import LeaderBoardDataAccess
from views.leaderboard_view import LeaderBoardView


class LeaderBoardController:
    def __init__(self, previousView):
        self.view = LeaderBoardView(self)
        self.previousView = previousView
        self.model = None

    def get_data(self, ordering='DESC'):
        """Method for retrieving leaderboard data and sorting it accordingly to user choice

        Args:
            ordering (str, optional): ordering. Defaults to 'DESC'.

        Returns:
            LeaderBoardModel[]: leaderboard results
        """
        with LeaderBoardDataAccess() as data_access:
            data = data_access.get_all()
            return sorted(data, key=lambda d: -int(d.score) if ordering == 'DESC' else int(d.score))

    def sort_data_asc(self):
        """On click handler for sorting data in ASC order
        """
        self.view.recreate_tab('ASC')

    def sort_data_desc(self):
        """On click handler for sorting data in DESC order
        """
        self.view.recreate_tab('DESC')

    def back_to_main(self):
        self.previousView.present()
        self.view.clear()
        self.view.destroy()
