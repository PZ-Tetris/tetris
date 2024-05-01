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
                return sorted(data, key=lambda d: int(d.score), reverse=(ordering == 'DESC'))
            else:
                return sorted(data, key=lambda d: d.nick, reverse=(ordering == 'ASC'))

    def sort_data(self, ordering, column):
        """On click handler for sorting data by column
        """
        self.view.recreate_tab(ordering, column)

    def back_to_main(self):
        self.previousView.present()
        self.view.clear()
        self.view.destroy()
