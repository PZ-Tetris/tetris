from helpers.leaderboard_data_access import LeaderBoardDataAccess
from views.leaderboard_view import LeaderBoardView


class LeaderBoardController:
    def __init__(self, previousView):
        self.view = LeaderBoardView(self)
        self.previousView = previousView
        self.model = None

    def get_data(self, ordering='DESC', col='score'):
        """Method for retrieving leaderboard data and sorting it accordingly to user choice

        Args:
            ordering (str, optional): ordering. Defaults to 'DESC'.

        Returns:
            LeaderBoardModel[]: leaderboard results
        """
        with LeaderBoardDataAccess() as data_access:
            data = data_access.get_all()

            if col == 'score':
                return sorted(data, key=lambda d: -int(d.score) if ordering == 'DESC' else int(d.score))
            else:
                return sorted(data, key=lambda d: d.nick if ordering == 'DESC' else d.nick)

    def sort_score_data_asc(self):
        """On click handler for sorting data by score in ASC order
        """
        self.view.recreate_tab('ASC')

    def sort_score_data_desc(self):
        """On click handler for sorting data by score in DESC order
        """
        self.view.recreate_tab('DESC')

    def sort_nick_data_asc(self):
        """On click handler for sorting data by nick in ASC order
        """
        self.view.recreate_tab('ASC', 'nick')

    def sort_nick_data_desc(self):
        """On click handler for sorting data by nick in DESC order
        """
        self.view.recreate_tab('DESC', 'nick')

    def back_to_main(self):
        self.previousView.present()
        self.view.clear()
        self.view.destroy()
