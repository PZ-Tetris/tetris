import sqlite3
from contextlib import closing
from typing import List

from models.leaderboard_model import LeaderBoardModel


class LeaderBoardDataAccess:
    def __init__(self):
        self.connection = sqlite3.connect("db.db")
        self.create()

        # only for testing purposes - when game view implemented this initial call will be removed
        self.init_data()

    def check_not_exists(self, data_null=None):
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
        if self.check_not_exists(True):
            people = [LeaderBoardModel(
                0, 'User1', 11), LeaderBoardModel(0, 'User2', 23)]
            for p in people:
                self.insert(p)

    def insert(self, data: LeaderBoardModel):
        with closing(self.connection.cursor()) as cursor:
            cursor.execute(
                "INSERT INTO Leaderboard(Nick, Score) VALUES(?,?);", (data.nick, data.score))
            self.connection.commit()

    def get_all(self) -> List[LeaderBoardModel]:
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
