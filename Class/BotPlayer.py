from Class.Player import Player


class BotPlayer(Player):

    def __init__(self, name):
        self.name = name
        super().__init__(self.name)

    def __str__(self):
        return super().__str__()
