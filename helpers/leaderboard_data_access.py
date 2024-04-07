import sqlite3
from contextlib import closing
from typing import List

from models.leaderboard_model import LeaderBoardModel


class LeaderBoardDataAccess:
    """Data access class for leaderboard interaction
    """

    def __init__(self):
        self.connection = sqlite3.connect("db.db")
        self.create()

        # only for testing purposes - when game view implemented this initial call will be removed
        self.init_data()

    def check_not_exists(self, data_null=None):
        """Method for checking whether the table or data exists

        Args:
            data_null (boolean, optional): Check for no data inside Leaderboard table. Defaults to None.

        Returns:
            bool: _description_
        """
        data = self.get_all()
        return data is None or (data_null and (len(data) == 0))

    def create(self):
        if self.check_not_exists():
            with closing(self.connection.cursor()) as cursor:
                cursor.execute(
                    """CREATE TABLE Leaderboard (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Nick TEXT NOT NULL,
                        Score TEXT NOT NULL
                    );""")

    def init_data(self):
        """Initialize data (only for testing purposes)
        """
        if self.check_not_exists(True):
            people = [LeaderBoardModel(
                0, 'User1', 11), LeaderBoardModel(0, 'User2', 23)]
            for p in people:
                self.insert(p)

    def insert(self, data: LeaderBoardModel):
        """Insert leaderboard data to the table

        Args:
            data (LeaderBoardModel): single leaderboard entry
        """
        with closing(self.connection.cursor()) as cursor:
            cursor.execute(
                "INSERT INTO Leaderboard(Nick, Score) VALUES(?,?);", (data.nick, data.score))
            self.connection.commit()

    def get_all(self) -> List[LeaderBoardModel]:
        """Get all entries from the database

        Returns:
            List[LeaderBoardModel]: leaderboard data
        """
        try:
            with closing(self.connection.cursor()) as cursor:
                data = cursor.execute(
                    "SELECT Id, Nick, Score FROM Leaderboard;").fetchall()
                res = [LeaderBoardModel(d[0], d[1], d[2]) for d in data]
                return res
        except:
            return None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()
