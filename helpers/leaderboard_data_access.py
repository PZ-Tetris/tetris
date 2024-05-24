import requests
import os
import json
from contextlib import closing
from typing import List

from models.leaderboard_model import LeaderBoardModel
from dotenv import load_dotenv

load_dotenv()


class LeaderBoardDataAccess:
    """Data access class for leaderboard interaction
    """

    POST_URL = f'{os.getenv("FUNCTION_URL")}/AddScore?code={os.getenv("CODE")}'
    GET_URL = f'{os.getenv("FUNCTION_URL")}/GetScores?start=0&limit=1000&code={os.getenv("CODE")}'

    def insert(self, data: LeaderBoardModel):
        """Insert leaderboard data to the table

        Args:
            data (LeaderBoardModel): single leaderboard entry
        """

        req = requests.post(self.POST_URL, json={
            'Id': '',
            'Nick': data.nick,
            'Score': data.score
        })

    def get_all(self) -> List[LeaderBoardModel]:
        """Get all entries from the database

        Returns:
            List[LeaderBoardModel]: leaderboard data
        """
        dt = []
        req = requests.get(self.GET_URL)
        if req.status_code == 200:
            resp = req.json()
            message = resp['message']
            for m in json.loads(message):
                dt.append(LeaderBoardModel(
                    m['Id'], m['Nick'], m['Score']))
        return dt

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
