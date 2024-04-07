class LeaderBoardModel:
    def __init__(self, id, nick, score):
        self.id = id
        self.nick = nick
        self.score = score

    def __str__(self):
        return f'{self.nick} {self.score}'
