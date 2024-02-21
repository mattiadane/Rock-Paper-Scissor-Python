class Player:

    def __init__(self, name):
        self.name = name
        self.hand = ["Rock", "Paper", "Scissor"]

    def __str__(self):
        return "%s" % self.name

    def play(self, index):
        return self.hand[index]
