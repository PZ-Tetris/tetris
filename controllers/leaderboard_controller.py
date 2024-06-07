from helpers.leaderboard_data_access import LeaderBoardDataAccess
from views.leaderboard_view import LeaderBoardView, Column, Ordering


class LeaderBoardController:
    """Controller for leaderboard logic
    """
    def __init__(self, previousView):
        self.view = LeaderBoardView(self)
        self.previousView = previousView
        self.model = None

    def get_data(self, ordering: Ordering, column: Column):
        """Method for retrieving leaderboard data and sorting it accordingly to user choice

        Args:
            ordering (Ordering): order of sort
            column (Column): column for ordering

        Returns:
            LeaderBoardModel[]: leaderboard results
        """
        with LeaderBoardDataAccess() as data_access:
            data = data_access.get_all()

            match column:
                case Column.NICK:
                    return sorted(data, key=lambda d: d.nick, reverse=not ordering.value)
                case Column.SCORE:
                    return sorted(data, key=lambda d: int(d.score), reverse=ordering.value)
                case _:
                    print(f"ERROR: unexpected Column: {column}")
                    return data

    def sort_data(self, ordering: Ordering, column: Column):
        """On click handler for sorting data by column
        """
        self.view.recreate_tab(ordering, column)

    def back_to_main(self):
        """Method for returning to main page
        """
        self.previousView.present()
        self.view.clear()
        self.view.destroy()
