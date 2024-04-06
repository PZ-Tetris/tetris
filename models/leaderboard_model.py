class LeaderBoardModel:
    def __init__(self, id, nick, score):
        self.id = id
        self.nick = nick
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: int):
        self.__id = value

    @property
    def nick(self):
        return self.__nick

    @nick.setter
    def nick(self, value: str):
        self.__nick = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value: int):
        self.__score = value

    def __str__(self):
        return f'{self.nick} {self.score}'
